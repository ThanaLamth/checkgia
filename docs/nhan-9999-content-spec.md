# Content Spec For `/vang/nhan-9999`

Related doc:

- `docs/nhan-9999-seo-fixes.md`

Date: 2026-06-17

## Objective

Turn `/vang/nhan-9999` from a mostly template-driven live-price page into a page that helps users make a better buy or sell decision.

The page already has:

- hero price block
- source comparison table
- historical anchors
- chart area
- calculators
- FAQ

The page still lacks:

- decision-oriented KPIs
- spread-first trading context
- source-level freshness interpretation
- unit-aware conversion in-page
- page-specific explanation for why sellers differ

## User Questions To Answer

The page should answer these quickly:

1. What is the cheapest sell price right now?
2. Is that price fresh enough to trust?
3. Which seller has the best spread, not just the lowest sell price?
4. Has price gone up or down versus yesterday, 7 days, 30 days, and 1 year?
5. How much money do I need for `1 chỉ`, `2 chỉ`, `5 chỉ`, and `1 lượng`?
6. Why do `Mi Hồng`, `PNJ`, and `DOJI` differ?
7. Which source should I check before going to a store?

## Proposed Page Structure

Recommended order:

1. Hero
2. Decision KPIs
3. Source table
4. Spread and freshness analysis
5. Inline unit conversion
6. Historical context
7. Brand-specific interpretation
8. Calculators
9. Short FAQ

## Block 1: Hero

Purpose:

- show the current headline number
- show whether the number is trustworthy right now

Must show:

- lowest current sell price
- best source name
- buy price
- sell price
- absolute timestamp
- freshness state

Recommended microcopy:

- `Giá bán thấp nhất hiện tại`
- `Thời gian cập nhật hiển thị riêng cho từng nguồn`
- `Nguồn cũ hơn ngưỡng kỳ vọng sẽ được cảnh báo`

Avoid:

- broad claim like `cập nhật mới nhất` without source nuance
- empty SSR placeholders

## Block 2: Decision KPIs

Purpose:

- compress the most important context into 4 cards

Cards:

1. `So với hôm qua`
2. `So với 7 ngày`
3. `So với 30 ngày`
4. `So với 1 năm`

Optional future cards:

- `Biên độ 30 ngày`
- `Biên độ 1 năm`
- `Đóng cửa gần nhất`

Data needed:

- current best sell price
- close price for `D-1`
- reference prices for `D-7`, `D-30`, `D-365`
- absolute and percentage delta

Output format:

- `+120.000 đ/chỉ`
- `+0,80%`

## Block 3: Source Table

Purpose:

- compare real choices, not just abstract averages

Keep:

- source
- buy price
- sell price
- delta vs previous snapshot
- freshness

Add:

- spread in `đ/chỉ`
- freshness badge
- region if known
- source link

Freshness badge states:

- `Mới`
- `Chậm`
- `Cũ`

Suggested thresholds:

- `Mới`: within expected refresh window
- `Chậm`: older than expected but same day
- `Cũ`: previous day or older

## Block 4: Spread And Freshness Analysis

Purpose:

- explain the real cost of trading

Title:

- `Chi phí vào ra vị thế`

What to show:

- rank sellers by spread
- absolute spread per seller
- note that lowest sell price is not always best after spread is considered
- point out stale sources

Suggested layout:

- top summary sentence
- 3 short seller cards or rows

Suggested summary logic:

- `Mi Hồng đang có giá bán thấp nhất, nhưng người mua nên nhìn thêm spread và độ tươi dữ liệu trước khi ra quyết định.`

## Block 5: Inline Unit Conversion

Purpose:

- reduce friction for users who think in transaction sizes

Title:

- `Nếu mua hôm nay`

Tabs or chips:

- `1 chỉ`
- `2 chỉ`
- `5 chỉ`
- `1 lượng`

For each selection:

- total cash needed at each seller
- resale value if sold immediately at current buy price
- implied spread loss

This is more useful than pushing users to a generic calculator first.

## Block 6: Historical Context

Purpose:

- make the history section answer clear questions

Keep:

- `hôm qua`
- `7 ngày`
- `30 ngày`
- `90 ngày`
- `1 năm`

Improve:

- show actual delta next to each historical card
- state whether each comparison uses best sell price, median, or source-specific series

Recommended labels:

- `So với hôm qua`
- `So với 7 ngày`
- `So với 30 ngày`
- `So với 90 ngày`
- `So với cùng kỳ năm trước`

## Block 7: Brand-Specific Interpretation

Purpose:

- create page-specific value that templates cannot

Title:

- `Cách đọc chênh lệch giá Nhẫn trơn 9999`

Keep this section short and concrete.

Include:

- sellers update independently
- each seller may target a different margin or spread
- freshness matters as much as raw sell price
- users buying short-term should care more about spread
- users comparing market direction should care more about multi-day moves

Suggested subheads:

- `Khi nào nên ưu tiên giá bán thấp nhất`
- `Khi nào nên ưu tiên spread hẹp`
- `Khi nào cần bỏ qua nguồn quá cũ`

## Block 8: Calculators

Purpose:

- keep action flow inside the gold topic

Keep links to:

- `Vàng → xăng`
- `Vàng → USD`
- `USD → VND`

But the calculators should come after:

- current price
- source comparison
- spread interpretation

Reason:

- calculators are secondary actions
- they should not appear before the page answers the main transaction question

## Block 9: FAQ

Purpose:

- handle only real product usage questions

Keep FAQ short:

- `Giá trên trang lấy từ đâu?`
- `Bao lâu cập nhật một lần theo từng nguồn?`
- `Vì sao các tiệm chênh nhau?`
- `Nên nhìn giá bán hay spread?`
- `Có thể đặt cảnh báo giá không?`

Tone rules:

- neutral Vietnamese
- no slang
- no `mày`, `tao`
- no mixed product jargon like `cross threshold`

## Data Contract Needed

The page will need this data server-side:

- `bestSourceName`
- `bestSellPrice`
- `bestBuyPrice`
- `bestUpdatedAt`
- `sourceRows[]`
- `spreadPerSource`
- `freshnessStatePerSource`
- `delta1d`
- `delta7d`
- `delta30d`
- `delta90d`
- `delta365d`
- `range30d`
- `range365d`
- `unitConversions[]`
- `sourceLinkPerSeller`
- `regionPerSeller` if available

## Suggested Rendering Rules

- Render hero and KPI data in HTML
- Never hide primary numeric content behind client-only components
- If any source is stale, still render it but visually downgrade it
- If only one source is fresh, say so explicitly

## Success Criteria

The page is improved when:

1. A user can compare cheapest sell price, best spread, and freshness without scrolling into charts.
2. A user can estimate transaction cost for `1 chỉ` and `1 lượng` from the page itself.
3. The page contains one section that is specific to `Nhẫn trơn 9999`, not generic to all products.
4. The history section shows deltas, not only dates.
5. FAQ becomes shorter and more trustworthy.

## Minimal Version

If engineering time is limited, implement in this order:

1. decision KPIs
2. spread and freshness block
3. inline unit conversion
4. page-specific interpretation block

## Example Above-The-Fold Flow

Order:

1. hero
2. KPI row
3. source table
4. spread summary

Example:

- Hero: `Giá bán thấp nhất hiện tại: 15.150.000 đ/chỉ`
- KPI 1: `So với hôm qua: -350.000 đ/chỉ`
- KPI 2: `So với 7 ngày: +1.150.000 đ/chỉ`
- KPI 3: `So với 30 ngày: +1.650.000 đ/chỉ`
- KPI 4: `So với 1 năm: +4.250.000 đ/chỉ`
- Spread summary: `Mi Hồng đang rẻ nhất để mua, nhưng spread thấp nhất hôm nay là ...`

## Notes For Implementation

- Do not solve this by adding more generic FAQ text.
- Do not solve this by adding more schema.
- Do not let chart widgets replace summary interpretation.
- Treat this as a transaction-decision page first, an SEO page second.
