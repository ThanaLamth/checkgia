# Content Spec For `/vang`

Related docs:

- `docs/vang-dev-prompt.md`
- `docs/vang-qa-checklist.md`
- `docs/checkgia-vs-cuthongthai-framework-mapping.md`

Date: 2026-06-18

## Objective

Turn `/vang` into a clearer gold hub that helps users choose the right next click quickly.

The page should not behave like a thin list page.

It should do three jobs well:

1. explain what gold prices and views the site covers
2. route users to the correct page type
3. surface enough context for Google and users to understand the section without needing to open many child pages

## User Intents To Serve

The page should help these users immediately:

1. users who want the latest overall gold overview
2. users who want a specific product page like `Nhẫn trơn 9999`
3. users who want a specific brand page like `PNJ`, `DOJI`, or `SJC`
4. users who want a historical date page
5. users who do not yet know which gold page they need

## What `/vang` Must Answer

Within the first screen and a short scroll, the page should answer:

1. this section tracks which gold products and sellers?
2. where should users click for product-level comparison?
3. where should users click for brand-level pricing?
4. where should users click for historical prices?
5. how fresh are the underlying source updates?

## Proposed Page Structure

Recommended order:

1. Hero and intro
2. Quick route block
3. Product grid
4. Brand grid
5. Historical paths or date context
6. Short section on freshness and source behavior
7. Short FAQ

## Block 1: Hero And Intro

Purpose:

- define the gold section clearly
- give users and Google a strong section summary

Must show:

- a plain-language H1 like `Giá vàng hôm nay`
- one short summary paragraph explaining:
  - the page tracks multiple gold products and sellers in Vietnam
  - update times may differ by source
  - users can drill down by product, brand, or date

Recommended microcopy:

- `Theo dõi giá vàng từ nhiều nguồn chính thức tại Việt Nam`
- `Mỗi nguồn có nhịp cập nhật riêng, nên thời gian hiển thị cần được đọc theo từng bảng giá`

Avoid:

- hype copy
- slang
- generic filler that does not help a user choose a next step

## Block 2: Quick Route Block

Purpose:

- reduce decision friction
- make the page function as a strong navigation hub

Suggested title:

- `Bạn đang cần xem loại nào?`

Include 3 clear route cards:

1. `Theo sản phẩm`
2. `Theo thương hiệu`
3. `Theo ngày lịch sử`

Each card should explain:

- what the page type is for
- an example click target
- when the user should choose that path

Example guidance:

- choose product pages when comparing buy and sell prices across sellers
- choose brand pages when following one seller consistently
- choose historical pages when checking trend by date

## Block 3: Product Grid

Purpose:

- route users into the highest-value comparison pages

Must include:

- `Nhẫn trơn 9999`
- major product pages already available in the site

For each product card:

- product name
- one-line explanation of why someone would open it
- direct internal link

Recommended card copy pattern:

- `So sánh giá mua, giá bán và spread giữa nhiều nguồn`

Prioritize cards that likely match commercial or comparison intent first.

## Block 4: Brand Grid

Purpose:

- serve users who search by store or brand name

Must include:

- `PNJ`
- `DOJI`
- `SJC`
- other major gold brands already tracked

For each brand card:

- brand name
- one-line use case
- direct internal link

Recommended use case copy:

- `Theo dõi bảng giá của thương hiệu này theo thời gian`

## Block 5: Historical Date Context

Purpose:

- explain that the site has history pages, not only live pages

Must show:

- short explanation of what date pages are for
- links to recent or important date pages if available

Recommended title:

- `Xem lại theo ngày`

Recommended copy:

- `Nếu bạn muốn đối chiếu biến động theo từng ngày, hãy mở các trang lịch sử để xem lại mốc giá cũ`

## Block 6: Freshness And Source Behavior

Purpose:

- set correct expectations about pricing freshness
- reduce overclaim risk

Must explain:

- sellers update independently
- timestamps should be read per source
- an older timestamp can still be useful, but should be marked clearly

Suggested bullets:

- `Không phải mọi nguồn đều cập nhật cùng lúc`
- `Giá rẻ nhất nên được đọc cùng thời gian cập nhật của chính nguồn đó`
- `Nguồn cũ hơn ngưỡng kỳ vọng cần được đánh dấu`

Avoid:

- absolute promises like `luôn mới nhất`
- vague claims that hide timestamp nuance

## Block 7: FAQ

Purpose:

- close a few practical questions without bloating the page

Keep this section short.

Recommended questions:

1. `Trang giá vàng này khác gì trang theo thương hiệu?`
2. `Khi nào nên xem trang theo sản phẩm thay vì theo cửa hàng?`
3. `Vì sao thời gian cập nhật giữa các nguồn khác nhau?`

Requirements:

- neutral Vietnamese
- no slang
- no unrelated fintech language

## Internal Linking Requirements

The hub should strengthen internal routing toward:

- product pages
- brand pages
- history pages

Priority order:

1. high-value product pages
2. major brand pages
3. recent historical pages

## Content Rules

Do:

- keep copy concise and directive
- make intent-based navigation obvious
- ensure visible HTML contains the key explanatory text

Do not:

- stuff the page with generic FAQ
- copy boilerplate explanations across all gold pages
- turn `/vang` into a shallow keyword page

## Definition Of Done

The hub spec is implemented well when:

1. `/vang` clearly explains the section in the intro
2. users can choose product vs brand vs history quickly
3. internal links are visible and prominent
4. freshness expectations are explained without overclaiming
5. FAQ is short, neutral, and useful
