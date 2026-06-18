# Savings Comparison Widget Spec For `/vang/nhan-9999`

Date: 2026-06-18

Target page:

- `https://checkgia.com/vang/nhan-9999`

Goal:

- add a small decision-support widget
- help users compare `mua vàng ngay` vs `tạm gửi tiết kiệm`
- keep the page focused on the gold-buying intent

## 1. Why This Widget Should Exist

Users on a ring-gold price page are often deciding between:

- buy now
- wait
- hold cash briefly

A small savings widget can help with that decision if it stays narrow.

This is useful because it:

- supports the transaction decision
- adds practical value beyond price display
- creates a stronger `content -> tool` flow

It should not:

- turn the gold page into a banking page
- replace the dedicated savings-rate surface
- introduce a large multi-bank comparison table here

## 2. Placement

Recommended position:

- after:
  - hero
  - KPI row
  - source table
  - spread / freshness analysis
- before:
  - generic calculators
  - long FAQ

Reason:

- users must first understand the gold market state
- only then should they compare an alternative action

## 3. Widget Name

Preferred titles:

- `Nếu chưa mua vàng hôm nay`
- `So nhanh với gửi tiết kiệm`

Preferred subtitle:

- `Ước tính nhanh nếu tạm giữ tiền ở ngân hàng thay vì mua Nhẫn trơn 9999 ngay bây giờ.`

## 4. Scope

This widget should answer only one question:

- `Nếu chưa mua ngay, gửi tiết kiệm ngắn hạn có thay đổi quyết định của mình không?`

This widget should not answer:

- full bank ranking
- complete term deposit research
- loan decisions
- long retirement planning

## 5. Inputs

Keep the input set minimal.

Required:

1. `Số tiền`
2. `Kỳ hạn`

Optional:

3. `Lãi suất tham chiếu`

Recommended default behaviors:

- prefill `Số tiền` from:
  - `1 chỉ`
  - `2 chỉ`
  - `5 chỉ`
  - `1 lượng`
- offer quick term chips:
  - `1 tháng`
  - `3 tháng`
  - `6 tháng`
- default interest source:
  - sitewide reference rate or current average deposit rate

## 6. Outputs

The widget should show:

1. `Tiền lãi ước tính`
2. `Tổng tiền nhận được cuối kỳ`
3. `Số chỉ vàng tương đương tại giá hiện tại`
4. `Biến động giá vàng gần đây để tham chiếu`

Recommended output labels:

- `Nếu gửi tiết kiệm`
- `Nếu mua Nhẫn 9999 ngay`
- `Chênh lệch cần lưu ý`

## 7. Suggested Comparison Logic

The output should compare:

- `current gold purchase cost`
- `deposit return over chosen term`
- `recent gold movement context`

Important:

- do not pretend to predict future gold price
- compare only against:
  - current price
  - recent historical movement
  - known deposit return

Use wording like:

- `Nếu gửi 3 tháng ở mức lãi suất tham chiếu hiện tại, tiền lãi ước tính là ...`
- `Mức lãi này tương đương khoảng ... chỉ vàng tại giá hiện tại`
- `Trong 30 ngày gần nhất, giá đã biến động ...`

Avoid wording like:

- `Bạn sẽ lời hơn nếu...`
- `Nên mua` / `Nên gửi`

## 8. UX Constraints

The widget must stay small.

Do:

- use 2 inputs max in the default state
- include quick preset amounts
- output one compact summary block
- include a link to the full savings-rate page

Do not:

- render a full bank table inside the gold page
- add more than one accordion layer
- require login
- push users into a complex calculator before they see the summary

## 9. Data Dependencies

Needed inputs from the system:

- current best sell price for `Nhẫn trơn 9999`
- standard unit conversions:
  - `1 chỉ`
  - `2 chỉ`
  - `5 chỉ`
  - `1 lượng`
- current deposit reference rate
- optional recent historical delta:
  - `7 ngày`
  - `30 ngày`

## 10. Trust And Copy Rules

This widget sits on a money-adjacent page.

Therefore:

- keep tone neutral
- label as estimate
- do not frame as financial advice
- show the savings rate source or reference note

Recommended disclaimer:

- `Ước tính để tham khảo, không phải tư vấn đầu tư hay tư vấn tài chính.`

## 11. Best Minimal Version

If engineering time is limited, ship this version first:

Inputs:

- `Mốc số tiền`:
  - `1 chỉ`
  - `5 chỉ`
  - `1 lượng`
- `Kỳ hạn`:
  - `1 tháng`
  - `3 tháng`

Outputs:

- estimated deposit interest
- total cash after term
- equivalent gold fraction at current price
- 30-day gold change summary

## 12. Example Copy

Title:

- `Nếu chưa mua vàng hôm nay`

Subtitle:

- `So nhanh giữa việc mua Nhẫn trơn 9999 ngay bây giờ và tạm gửi tiết kiệm ngắn hạn.`

Output example:

- `Nếu giữ số tiền tương đương 1 lượng vàng và gửi 3 tháng theo lãi suất tham chiếu hiện tại, tiền lãi ước tính là ...`
- `Mức này tương đương khoảng ... chỉ vàng tại giá hiện tại.`
- `Trong 30 ngày gần nhất, giá Nhẫn trơn 9999 đã ...`

## 13. Link-Out Behavior

Include one supporting link:

- `Xem lãi suất tiết kiệm đầy đủ →`

Destination:

- the dedicated savings-rate page

This keeps:

- the gold page focused
- the finance vertical separate

## 14. Success Criteria

The widget is successful if:

1. it helps users compare `buy now` vs `wait briefly`
2. it does not dominate the gold-page layout
3. it drives qualified clicks to the full savings page
4. it increases usefulness without weakening the page's gold intent

## 15. Anti-Patterns

Do not do these:

- embed full multi-bank rate tables in the gold page
- compare too many products at once
- imply future gold prediction
- make savings the new primary topic of the page

## 16. Final Product Direction

This should be treated as:

- a `decision widget`

not as:

- a `banking widget pasted into a gold page`
