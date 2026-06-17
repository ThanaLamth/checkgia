# AIO Update Checklist For `/vang/nhan-9999`

Date: 2026-06-17

Target URL:

- `https://checkgia.com/vang/nhan-9999`

Goal:

- improve readiness for Google AI features
- keep recommendations aligned with current Google Search Central guidance
- separate `Google-official requirements` from `cross-platform AI heuristics`

Primary sources checked live:

- `https://developers.google.com/search/docs/appearance/ai-features`
- `https://developers.google.com/search/docs/fundamentals/creating-helpful-content`
- `https://developers.google.com/search/docs/crawling-indexing/javascript/javascript-seo-basics`
- `https://developers.google.com/search/docs/appearance/structured-data/faqpage`

## 1. Official Google Position

### What Google explicitly says

- To appear as a supporting link in AI Overviews or AI Mode, a page must be:
  - indexed
  - eligible to show a snippet in Google Search
  - compliant with Search technical requirements
- There are `no additional technical requirements`
- Existing SEO best practices still matter:
  - crawling allowed
  - content easily found through internal links
  - good page experience
  - important content available in textual form
  - structured data matches visible content

### What this means for Checkgia

- do not chase fake `AIO-only` technical hacks
- focus on:
  - rendered HTML
  - trust
  - answer clarity
  - page-specific usefulness

## 2. Verdict

Current status:

- `partially aligned`

Reason:

- the page is indexable and content-rich
- but the most important transactional content is still not rendered clearly enough in the hero
- some schema and FAQ patterns add noise rather than improving AI/Search usefulness

## 3. Must Update Now

### A. Server-render the hero values

Status:

- `Google-official requirement adjacent`

Issue:

- the live HTML still shows `—` in the hero for:
  - best price
  - buy price
  - sell price

Why it matters:

- Google says it uses the rendered HTML to index content
- if important content is not visible in rendered HTML, Google may not index it correctly

Fix:

- SSR these fields directly in the hero:
  - `bestSourceName`
  - `bestSellPrice`
  - `bestBuyPrice`
  - `bestUpdatedAt`
  - freshness state

Acceptance check:

- fetching the HTML should show real numbers in the hero, not placeholders

### B. Add a direct answer block above the table

Status:

- `reasonable heuristic`

Issue:

- the page has data, but the answer is still too implicit

Why it matters:

- AI systems and users both benefit from direct, short, factual summaries

Fix:

- add 2 to 4 short lines in visible HTML:
  - lowest current sell price
  - best source
  - spread summary
  - freshness summary

Example:

- `Giá bán thấp nhất hiện tại là 15.100.000 đ/chỉ tại Mi Hồng.`
- `Spread thấp nhất hôm nay là ...`
- `Tất cả nguồn hiện cập nhật trong vòng ...`

Acceptance check:

- a user can understand the page's main conclusion without parsing the whole table

### C. Fix freshness wording

Status:

- `Google-official trust alignment`

Issue:

- broad freshness claims can weaken perceived reliability if sources refresh at different times

Fix:

- prefer wording like:
  - `Thời gian cập nhật hiển thị riêng cho từng nguồn`
  - `Nguồn cũ hơn ngưỡng kỳ vọng sẽ được cảnh báo`
- avoid broad statements that imply all sources update equally

Acceptance check:

- page-level wording never overstates freshness relative to source-level timestamps

### D. Remove low-value schema

Status:

- `Google-officially supported cleanup`

Issue:

- `FAQPage` rich result is no longer shown in Google Search results
- `Dataset` structured data is for Dataset Search, not Google Search

Fix:

- remove:
  - `FAQPage`
  - `Dataset`
- keep:
  - `Product`
  - `AggregateOffer`
  - `BreadcrumbList`
  - sitewide `Organization`

Acceptance check:

- page source no longer contains `FAQPage` or `Dataset`

### E. Rewrite FAQ tone

Status:

- `reasonable heuristic` with trust impact

Issue:

- current FAQ tone includes:
  - `mày`
  - `Tao`
  - `magic link`
  - `cross threshold`

Why it matters:

- the page is money-adjacent
- casual slang lowers trust

Fix:

- rewrite in neutral Vietnamese
- keep FAQ short and utility-focused

Acceptance check:

- FAQ reads like product help, not slangy marketing copy

## 4. Should Update Soon

### A. SSR historical KPI row

Status:

- `reasonable heuristic`

Add:

- `So với hôm qua`
- `So với 7 ngày`
- `So với 30 ngày`
- `So với 1 năm`

Why:

- creates answer-shaped context for AI features and classic Search

### B. Add spread-first interpretation

Status:

- `reasonable heuristic`

Add a short section:

- why lowest sell price is not always best
- why spread matters
- when stale data should be discounted

### C. Add inline transaction-size conversion

Status:

- `reasonable heuristic`

Add:

- `1 chỉ`
- `2 chỉ`
- `5 chỉ`
- `1 lượng`

Why:

- this makes the page more directly useful than generic calculators alone

## 5. Nice To Have

### A. Normalize entity names in schema

- `mi-hong` -> `Mi Hồng`
- keep human-readable seller names in structured data

### B. Add source links per seller

- useful for user trust
- useful as a cross-platform AI heuristic

### C. Add one page-specific interpretation block

Suggested title:

- `Cách đọc chênh lệch giá Nhẫn trơn 9999`

## 6. Explicit Separation

### Google-official AI feature guidance

Use these as hard anchors:

- no extra technical requirements for AI Overviews / AI Mode
- page must be indexed and snippet-eligible
- important content should be available in text
- structured data should match visible content

### Cross-platform AI visibility heuristics

Use these as practical improvements, not Google policy:

- concise answer block
- KPI summary row
- spread explanation
- transaction-size conversion
- source trust labels

## 7. Final Priority Order

1. SSR hero values
2. fix freshness wording
3. remove `FAQPage` and `Dataset`
4. rewrite FAQ tone
5. add direct answer block
6. add historical KPI row
7. add spread interpretation
8. add inline unit conversion

## 8. Definition Of Done

The page is ready for a better AIO posture when:

1. hero values are visible in rendered HTML
2. freshness is stated honestly at source level
3. low-value schema is removed
4. FAQ becomes neutral and shorter
5. the page contains a direct textual answer before the detailed table
6. the page explains spread and historical context without forcing users to infer everything themselves
