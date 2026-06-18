# Detailed Outline For `/vang/nhan-9999`

Date: 2026-06-18

Target page:

- `https://checkgia.com/vang/nhan-9999`

Purpose:

- turn the first content outline into a more execution-ready structure
- clarify what content each section actually needs
- help content, product, and dev align on the same page shape

Related docs:

- `docs/nhan-9999-content-spec.md`
- `docs/nhan-9999-aio-update-checklist.md`
- `docs/nhan-9999-savings-widget-spec.md`

## 1. Hero

### Content needed

- clear entity name:
  - `Nhẫn trơn 9999`
- current lowest sell price
- source name for the lowest current sell price
- current buy price and sell price for the hero source
- absolute update timestamp
- short freshness note if any source is older than expected

### Content goal

- answer immediately:
  - current price
  - where it is cheapest
  - whether the data is fresh enough

## 2. Decision KPI Row

### Content needed

- change vs yesterday:
  - absolute difference
  - percentage difference
- change vs 7 days
- change vs 30 days
- change vs 1 year

Optional if data is ready:

- 30-day range
- 1-year range

### Content goal

- show whether price is rising or falling across the time windows users actually care about

## 3. Source Comparison Table

### Content needed

- seller / brand name
- buy price
- sell price
- spread:
  - `sell - buy`
- change vs previous snapshot
- timestamp per source
- badges:
  - cheapest
  - lowest spread
  - stale data

### Content goal

- let users compare real store options, not only abstract averages

## 4. Spread And Freshness Summary

### Content needed

- one sentence stating which source is cheapest to buy from
- one sentence stating which source has the best spread
- one sentence calling out stale or caution-worthy sources
- one short explanatory line:
  - cheapest sell price is not always the best choice

### Content goal

- reduce the need for users to infer conclusions from the table on their own

## 5. Transaction Conversion Widget

### Content needed

- presets:
  - `1 chỉ`
  - `2 chỉ`
  - `5 chỉ`
  - `1 lượng`
- total purchase cost by source
- immediate resale value using current buy price
- instant spread loss in money terms

### Content goal

- turn price data into real transaction math

## 6. Section: `Nếu chưa mua vàng hôm nay`

### Content needed

- input:
  - amount of money or preset gold quantity
  - deposit term
- output:
  - estimated deposit interest
  - total cash after the term
  - equivalent gold amount at current price
- one neutral note:
  - this is a reference comparison, not a gold price forecast

### Content goal

- help users compare `buy now` versus `wait briefly`

## 7. Entity-Specific Interpretation Block

### Content needed

- why `Mi Hồng`, `PNJ`, and `DOJI` differ
- why spread differs across sellers
- when to prioritize the lowest sell price
- when to prioritize the narrowest spread
- when a stale timestamp should reduce confidence

### Content goal

- create unique value for this exact page instead of repeating a generic template

## 8. History And Context

### Content needed

- comparison points:
  - yesterday
  - 7 days
  - 30 days
  - 90 days
  - 1 year
- for each comparison point:
  - reference close or historical price
  - difference versus current price
- one short context note:
  - historical data describes the past, not the future

### Content goal

- help users read direction and magnitude, not just dates

## 9. Related Tools

### Content needed

- `Vàng → xăng`
- `Vàng → USD`
- `USD → VND`
- `Lãi suất tiết kiệm đầy đủ`

Each link should have:

- one short use-case line

### Content goal

- provide a sensible next step after the user reads the gold page

## 10. Short FAQ

### Content needed

- where the prices come from
- how often each source updates
- why seller prices differ
- whether to focus on sell price or spread
- whether price alerts are available

### Content goal

- answer real user questions
- avoid using FAQ as SEO filler

## 11. Final Notes

This outline should be used as:

- the bridge between the page spec and the actual copy draft

Recommended next step:

- create a separate content draft file with example wording for each section
