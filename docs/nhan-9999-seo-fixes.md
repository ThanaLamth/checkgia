# Fix Plan For `/vang/nhan-9999`

Date audited: 2026-06-17
Target URL: `https://checkgia.com/vang/nhan-9999`

## Goal

Improve the page so it is:

- more stable for Google indexing
- more accurate about data freshness
- less dependent on low-value schema/template content
- more useful for users comparing ring gold prices

## Priority 1: SSR The Main Price Block

Problem:

- The main hero price block has shown placeholder values like `—` in HTML during some responses.
- For a live-price page, the main price, best source, buy/sell values, and update time are core content.

Required changes:

- Server-render the hero numbers from the same payload used for the comparison table.
- Do not let the hero depend on client hydration to show the first meaningful values.
- If data is stale, still render the latest known numbers in HTML and add a stale notice.

Expected output in HTML:

- best sell price
- best source name
- buy price
- sell price
- absolute timestamp
- per-source freshness summary

## Priority 2: Fix Freshness Messaging

Problem:

- The page title and description claim broad freshness.
- Actual source freshness varies by seller, for example one source may be updated within 1 hour while another is 1 day old.
- The page already warns when data is older than expected, which makes the broader freshness claim look inconsistent.

Required changes:

- Replace generic copy like `Cập nhật mỗi 10 phút` with wording that reflects source-level freshness.
- Keep the page-level update summary, but make it explicit that each source updates on its own schedule.
- Show stale thresholds clearly.

Recommended copy direction:

- `So sánh giá Nhẫn trơn 9999 từ các nguồn chính thức. Thời gian cập nhật hiển thị riêng cho từng nguồn.`
- `Dữ liệu có thể lệch giữa các thương hiệu; luôn kiểm tra timestamp trước khi giao dịch.`

## Priority 3: Remove Low-Value Structured Data

Problem:

- `FAQPage` schema is no longer useful as a Google Search rich result lever.
- `Dataset` schema does not help standard Google Search for this use case.

Required changes:

- Remove `FAQPage` JSON-LD from this page template.
- Remove `Dataset` JSON-LD from this page template.
- Keep `Product` and `BreadcrumbList`.

Keep:

- `Product`
- `AggregateOffer`
- `BreadcrumbList`
- `Organization` sitewide

## Priority 4: Clean FAQ And Tone

Problem:

- Current FAQ copy uses casual tone like `mày`, `Tao`, `magic link`, `cross threshold`.
- For a money-adjacent page, this weakens perceived trust.

Required changes:

- Rewrite FAQ in neutral Vietnamese.
- Keep only FAQs that help users interpret the data or use alerts correctly.
- Remove wording that sounds like internal product slang.

Examples:

- `Tao có thể đặt alert giá vàng không?` -> `Có thể đặt cảnh báo giá vàng không?`
- `Khi giá cross threshold mày đặt` -> `Khi giá vượt ngưỡng bạn đã thiết lập`

## Priority 5: Increase Page-Specific Value

Problem:

- The page already has history blocks, calculators, and FAQ.
- The unique value for this exact URL is still too template-like.

Required changes:

- Add one short explanatory block specific to `Nhẫn trơn 9999`.
- Explain why `Mi Hồng`, `PNJ`, and `DOJI` may differ.
- Explain how to read spread `mua vào / bán ra`.
- Explain when to compare 1 day, 7 day, 30 day, and 1 year views.

Suggested section title:

- `Cách đọc chênh lệch giá Nhẫn trơn 9999`

Suggested bullets to cover:

- each seller updates independently
- spread matters, not just lowest sell price
- older timestamps should be treated with caution
- short-term and long-term comparisons answer different user questions

## Priority 6: Normalize Seller Entities

Problem:

- Structured data currently uses seller names like `mi-hong` instead of human-readable entities.

Required changes:

- Convert seller display names in schema to proper entities:
  - `Mi Hồng`
  - `PNJ`
  - `DOJI`

## Suggested Acceptance Checks

After implementation, confirm:

1. The HTML response contains real hero price values, not placeholders.
2. The title and meta description do not overstate freshness.
3. `FAQPage` and `Dataset` JSON-LD are gone.
4. `Product` and `BreadcrumbList` JSON-LD still validate.
5. FAQ tone is neutral and user-facing.
6. The page includes one short section with page-specific interpretation, not just template widgets.

## Suggested Commit Split

If implementing later in code, split roughly like this:

1. `fix(vang): server-render hero pricing for product pages`
2. `fix(seo): remove faq and dataset schema from gold product pages`
3. `fix(copy): align freshness and faq wording on nhan-9999`
4. `feat(content): add interpretation block for nhan-9999`
