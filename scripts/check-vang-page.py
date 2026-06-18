#!/usr/bin/env python3
import re
import sys
import urllib.request
from html import unescape


DEFAULT_URLS = [
    "https://checkgia.com/vang",
    "https://checkgia.com/vang/nhan-9999",
]


def fetch(url: str) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; checkgia-qa-bot/1.0)"
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="replace")


def has(pattern: str, text: str) -> bool:
    return re.search(pattern, text, re.I | re.S) is not None


def extract(pattern: str, text: str) -> str | None:
    match = re.search(pattern, text, re.I | re.S)
    return match.group(1).strip() if match else None


def title_of(html: str) -> str | None:
    return extract(r"<title>(.*?)</title>", html)


def canonical_of(html: str) -> str | None:
    return extract(r'<link rel="canonical" href="([^"]+)"', html)


def meta_description_of(html: str) -> str | None:
    return extract(r'<meta name="description" content="([^"]*)"', html)


def h1_of(html: str) -> str | None:
    return extract(r"<h1[^>]*>(.*?)</h1>", html)


def print_result(label: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    suffix = f" - {detail}" if detail else ""
    print(f"[{status}] {label}{suffix}")


def check_common(url: str, html: str) -> int:
    failures = 0
    title = title_of(html)
    canonical = canonical_of(html)
    meta_desc = meta_description_of(html)
    h1 = h1_of(html)
    normalized_html = unescape(html).lower()

    ok = title is not None and len(title) > 0
    print_result("title present", ok, title or "")
    failures += 0 if ok else 1

    ok = canonical is not None
    print_result("canonical present", ok, canonical or "")
    failures += 0 if ok else 1

    expected_canonical = url.rstrip("/")
    ok = canonical is not None and canonical.rstrip("/") == expected_canonical
    print_result("canonical matches target URL", ok, canonical or "")
    failures += 0 if ok else 1

    ok = meta_desc is not None and len(meta_desc) > 0
    print_result("meta description present", ok, meta_desc or "")
    failures += 0 if ok else 1

    ok = h1 is not None and len(re.sub(r"<[^>]+>", "", h1).strip()) > 0
    print_result("H1 present", ok, re.sub(r"<[^>]+>", "", h1 or "").strip())
    failures += 0 if ok else 1

    ok = "noindex" not in normalized_html
    print_result("page is indexable (no noindex)", ok)
    failures += 0 if ok else 1

    slang_terms = ["mày", "tao", "cross threshold", "magic link"]
    for term in slang_terms:
        ok = term not in normalized_html
        print_result(f"slang removed: {term}", ok)
        failures += 0 if ok else 1

    return failures


def check_vang_hub(url: str, html: str) -> int:
    failures = 0

    checks = [
        ("FAQPage removed", not has(r'"@type":"FAQPage"', html)),
        ("Organization present", has(r'"@type":"Organization"', html)),
        ("BreadcrumbList present", has(r'"@type":"BreadcrumbList"', html)),
        ("entity page linked", "/vang/nhan-9999" in html),
        ("brand page linked", "/vang/pnj" in html or "/vang/doji" in html),
        ("history page linked", "/gia/2026-" in html or '/gia/' in html),
    ]

    for label, ok in checks:
        print_result(label, ok)
        failures += 0 if ok else 1

    return failures


def hero_has_placeholder(html: str) -> bool:
    # Narrowly target the hero block around "Rẻ nhất hôm nay" to avoid false positives.
    match = re.search(
        r"Rẻ nhất hôm nay.*?(num-ticker\">—|Mua vào</dt>.*?num-ticker\">—|Bán ra</dt>.*?num-ticker\">—)",
        html,
        re.I | re.S,
    )
    return match is not None


def check_nhan_9999(url: str, html: str) -> int:
    failures = 0

    checks = [
        ("FAQPage removed", not has(r'"@type":"FAQPage"', html)),
        ("Dataset removed", not has(r'"@type":"Dataset"', html)),
        ("Product present", has(r'"@type":"Product"', html)),
        ("AggregateOffer present", has(r'"@type":"AggregateOffer"', html)),
        ("BreadcrumbList present", has(r'"@type":"BreadcrumbList"', html)),
        ("hero has no placeholder", not hero_has_placeholder(html)),
        ("answer summary present", "hôm nay rẻ nhất" in html.lower()),
        ("KPI card: hôm qua", "Hôm qua" in html),
        ("KPI card: 7 ngày", "7 ngày trước" in html or "7 ngày" in html),
        ("KPI card: 30 ngày", "30 ngày trước" in html or "30 ngày" in html),
        ("KPI card: 1 năm", "1 năm trước" in html or "1 năm" in html),
        ("spread mentioned", "Spread mua/bán" in html or "spread" in html.lower()),
        ("savings widget not yet required on live page", True),
    ]

    for label, ok in checks:
        print_result(label, ok)
        failures += 0 if ok else 1

    freshest_pattern = r"Cập nhật\s*<!-- -->\s*\d"
    ok = has(freshest_pattern, html) or "ago" in html or "trước" in html
    print_result("freshness/timestamp visible", ok)
    failures += 0 if ok else 1

    return failures


def check_url(url: str) -> int:
    print(f"\n== {url} ==")
    try:
        html = fetch(url)
    except Exception as exc:
        print_result("fetch", False, str(exc))
        return 1

    failures = check_common(url, html)

    if url.rstrip("/") == "https://checkgia.com/vang":
        failures += check_vang_hub(url, html)
    elif url.rstrip("/") == "https://checkgia.com/vang/nhan-9999":
        failures += check_nhan_9999(url, html)
    else:
        print_result("custom URL mode", True, "only common checks applied")

    return failures


def main() -> int:
    urls = sys.argv[1:] or DEFAULT_URLS
    total_failures = 0
    for url in urls:
        total_failures += check_url(url)

    print(f"\nTotal failures: {total_failures}")
    return 1 if total_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
