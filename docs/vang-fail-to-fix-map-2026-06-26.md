# Vang Fail-To-Fix Map

Related docs:

- `docs/vang-release-audit-2026-06-25.csv`
- `docs/vang-hub-content-draft-2026-06-26.md`
- `docs/vang-content-followup-handoff-2026-06-26.md`

Date: 2026-06-26

## Purpose

This file maps the current `/vang` release-audit failures to specific fixes.

Use it when handing the next implementation round to engineering or content.

## 1. Hub Intro Prominence

### Audit Failure

- `hub intro prominence`

### Current Problem

- The intro exists, but it is too weak visually.
- It does not read like the main explanatory content of a hub page.

### Fix Direction

- Replace the current intro with the new intro from:
  - `docs/vang-hub-content-draft-2026-06-26.md`
- Increase prominence in UI:
  - do not render it as tiny muted helper text
  - place it directly below H1
  - give it clearer spacing and stronger readability

### Done When

- A first-time visitor can immediately understand:
  - what the page covers
  - that it tracks multiple sources
  - that users can continue by product, brand, or historical date

## 2. Quick Route Block Spec

### Audit Failure

- `quick route block spec`

### Current Problem

- `/vang` still lacks a strong route-guidance block that frames the three main browsing paths clearly.

### Fix Direction

- Add a dedicated block immediately after the intro.
- Use the title:
  - `Bạn đang cần xem loại nào?`
- Add 3 route cards:
  - `Theo sản phẩm`
  - `Theo thương hiệu`
  - `Theo ngày lịch sử`
- Follow the copy direction in:
  - `docs/vang-hub-content-draft-2026-06-26.md`

### Done When

- The top part of the page clearly shows three main ways to browse the gold section.

## 3. Route Card Clickability

### Audit Failure

- `route cards clickability`

### Current Problem

- Route cards behave more like descriptive text than actual navigation controls.

### Fix Direction

- Make each route card clickable.
- Recommended behavior:
  - `Theo sản phẩm` -> jump to the product section
  - `Theo thương hiệu` -> jump to the brand section
  - `Theo ngày lịch sử` -> jump to the history section
- Use anchor links or direct navigation where appropriate.
- Keep the call-to-action explicit.

### Done When

- Users no longer need to manually scroll and hunt for the correct section.

## 4. Route Microcopy

### Audit Failure

- `route microcopy`

### Current Problem

- Users do not get a short explanation for when to choose each path.

### Fix Direction

- Add one short explanatory line to each route card.
- Follow the draft wording:
  - `Theo sản phẩm`: use when comparing the same gold type across multiple stores
  - `Theo thương hiệu`: use when following a specific system or familiar store
  - `Theo ngày lịch sử`: use when comparing price movement across time

### Done When

- Each route card includes:
  - a clear label
  - a clear use case
  - a clear next action

## 5. Section Wording Clarity

### Audit Failure

- `section wording clarity`

### Current Problem

- Current labels are less intent-clear than they should be for a hub page.

### Fix Direction

- Rename section headings:
  - `Tất cả vàng` -> `Theo sản phẩm`
  - `Mỗi tiệm riêng` -> `Theo thương hiệu`
  - `Giá vàng ngày trước` -> `Theo ngày lịch sử`
  - `Câu hỏi hay gặp` -> `Câu hỏi thường gặp`

### Done When

- Section headings immediately reflect user intent and browsing path.

## 6. Freshness And Source Behavior

### Audit Failure

- not always listed as a separate fail line, but still a follow-up requirement from the hub review

### Current Problem

- The page does not yet explain clearly enough how to read update timing across different sources.

### Fix Direction

- Add a short standalone content block.
- Include these ideas:
  - not every source updates at the same time
  - the cheapest price should be read together with that source’s update time
  - the data is for reference and comparison, not investment advice
- Follow the copy direction in:
  - `docs/vang-hub-content-draft-2026-06-26.md`

### Done When

- Users can understand why price comparison without update-time context is incomplete.

## Source Files To Implement From

- `docs/vang-hub-content-draft-2026-06-26.md`
- `docs/vang-content-followup-handoff-2026-06-26.md`
- `docs/vang-hub-content-spec.md`

## What Engineering Should Return

After updating `/vang`, return:

1. changed file list
2. staging URL
3. short note for each block updated
