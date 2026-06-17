# Checkgia Vs. Cuthongthai Framework Mapping

Date: 2026-06-17

Target page:

- `https://checkgia.com/vang/nhan-9999`

Reference docs:

- `cuthongthai_google_subdomain_logic_2026-06-11.vi.md`
- `cuthongthai_integrated_research_2026-06-10.vi.md`
- `cuthongthai_swot_analysis_2026-06-10.vi.md`

Related local docs:

- `docs/nhan-9999-seo-fixes.md`
- `docs/nhan-9999-content-spec.md`

## 1. Why This Mapping Exists

The `Cuthongthai` docs do not argue that `subdomain` is the winning trick.

They argue that the real advantage comes from combining:

- semantic clarity
- product surface
- intent purity
- answer-shaped content
- tool funnel
- measurement surfaces
- trust architecture

For `checkgia`, the correct move is not `copy subdomain`.

The correct move is:

- keep the current domain strategy
- copy the logic of `mini-product surfaces`
- sharpen the page until it behaves like a decision product, not a generic SEO page

## 2. One-To-One Mapping

### Principle 1: `Site Boundary / Source Identity`

Cuthongthai logic:

- each host behaves like a mini-site with its own proposition
- the boundary helps Google and users understand what the surface is for

Checkgia equivalent:

- `checkgia.com` = umbrella brand
- `/vang` = gold vertical
- `/vang/nhan-9999` = one transaction-specific mini-product page

Current state on `/vang/nhan-9999`:

- partially present
- page identity exists, but proposition is still soft

Problem:

- the page currently reads as `price page + widgets`
- it does not yet read strongly as `decision surface for ring gold buyers`

Implementation backlog:

1. Add a short proposition line under H1:
   - example: `Trang so sánh giá mua bán Nhẫn trơn 9999 theo từng thương hiệu, ưu tiên quyết định giao dịch trong ngày.`
2. Reframe hero labels around decision use:
   - `Giá bán thấp nhất hiện tại`
   - `Nguồn có spread thấp hơn`
   - `Nguồn cần thận trọng vì dữ liệu cũ`
3. Add one section that explicitly states what this page is for:
   - `Dành cho người cần so sánh giá mua hôm nay, spread và độ tươi dữ liệu trước khi ra tiệm.`

Priority:

- high

## Principle 2: `Intent Purity`

Cuthongthai logic:

- each surface stays close to one intent cluster
- cleaner intent means clearer matching and clearer expectations

Checkgia equivalent:

- the page should stay tightly focused on `nhẫn 9999 price comparison and transaction interpretation`

Current state:

- strong at the query level
- weaker at the block level

Problem:

- some blocks are still generic site furniture
- the page answers the query, but not yet the full decision intent

Implementation backlog:

1. Keep the first screen centered on:
   - current price
   - freshness
   - source comparison
   - spread
2. Push lower-priority blocks down:
   - generic calculators
   - long FAQ
3. Add a page-specific interpretation block:
   - why sellers differ
   - when spread matters more than lowest sell price

Priority:

- high

## Principle 3: `Answer-Shaped Packaging`

Cuthongthai logic:

- winning pages often package information in answer-ready chunks
- the page can be scanned and understood before deep interaction

Checkgia equivalent:

- a gold price page should answer the main transactional questions in under 10 seconds

Current state:

- weak to medium

Problem:

- users still need to read table rows and infer conclusions themselves
- hero currently under-delivers on direct answers

Implementation backlog:

1. Add a KPI row directly below hero:
   - `So với hôm qua`
   - `So với 7 ngày`
   - `So với 30 ngày`
   - `So với 1 năm`
2. Add one summary sentence above the source table:
   - `Hôm nay Mi Hồng đang có giá bán thấp nhất, nhưng DOJI đang cũ dữ liệu hơn và spread giữa các nguồn vẫn cần được cân nhắc.`
3. Add a spread summary block:
   - `Nếu mua rồi bán lại ngay`
   - show likely spread loss by seller

Priority:

- very high

## Principle 4: `Content -> Tool -> Ecosystem`

Cuthongthai logic:

- content does not end in content
- the user is pushed into a more useful tool or product action

Checkgia equivalent:

- page should move users from `reading a price` to `making a decision`

Current state:

- medium

Strength:

- history pages, charts, and calculators already exist

Problem:

- the flow is still loose
- tools are present, but not sequenced from strongest decision need to secondary exploration

Implementation backlog:

1. Add inline transaction-size conversion before external calculators:
   - `1 chỉ`
   - `2 chỉ`
   - `5 chỉ`
   - `1 lượng`
2. Keep generic calculators after spread and history context
3. Add clearer next steps:
   - `Xem giá hôm qua`
   - `Xem biểu đồ 7 ngày`
   - `Tính tổng tiền mua 5 chỉ`

Priority:

- high

## Principle 5: `Measurement Surface`

Cuthongthai logic:

- strong systems expose clean surfaces for measurement
- inventory is meaningful only when pages and clusters can be evaluated clearly

Checkgia equivalent:

- `/vang/nhan-9999`
- `/vang/nhan-9999/gia/YYYY-MM-DD`
- `/vang/nhan-9999/gia/thang/YYYY-MM`
- `/vang/nhan-9999/gia/nam/YYYY`
- `/vang/nhan-9999/bieu-do-*`

Current state:

- structurally strong

Strength:

- inventory around the entity already exists

Problem:

- the main page does not yet summarize the deeper measurement surfaces well enough

Implementation backlog:

1. Connect main page to measurement pages with explicit semantics:
   - `Giá đóng cửa hôm qua`
   - `Biên độ 30 ngày`
   - `Diễn biến 1 năm`
2. Show deltas on the historical links, not only dates
3. Distinguish current snapshot from close-price history clearly

Priority:

- medium to high

## Principle 6: `Trust Architecture`

Cuthongthai logic:

- scaling architecture is not enough
- each vertical needs a trust layer that matches user expectations

Checkgia equivalent:

- money-adjacent pages need stronger trust than generic comparison content

Current state:

- medium at site level
- weak on this specific page

Problems:

- freshness messaging is broader than the actual source-level data
- FAQ tone is too casual for the page type
- `FAQPage` and `Dataset` schema add clutter without improving trust
- seller entity naming is inconsistent in schema

Implementation backlog:

1. Rewrite freshness copy:
   - page-level summary must not overstate freshness
   - source-level timestamps must lead trust interpretation
2. Remove `FAQPage` JSON-LD
3. Remove `Dataset` JSON-LD
4. Normalize seller names in schema:
   - `Mi Hồng`
   - `PNJ`
   - `DOJI`
5. Rewrite FAQ in neutral Vietnamese
6. Add source links or source labels near each seller row

Priority:

- very high

## Principle 7: `Inventory + Distinct Value`

Cuthongthai logic:

- large inventory only works if pages have a reason to exist beyond template expansion

Checkgia equivalent:

- history pages and chart pages can scale
- but the pillar page must carry distinct explanatory value

Current state:

- medium risk

Problem:

- if many gold pages reuse the same block pattern without stronger interpretation, the system may scale breadth faster than value

Implementation backlog:

1. Add one page-specific section:
   - `Cách đọc chênh lệch giá Nhẫn trơn 9999`
2. Explain:
   - why sellers differ
   - why spread matters
   - when stale data should be discounted
3. Use the same framework for other gold entity pages, but with entity-specific explanations

Priority:

- high

## 3. Strategic Scorecard

Scoring:

- `strong`
- `medium`
- `weak`

| Layer | Cuthongthai Logic | `/vang/nhan-9999` Today | Verdict |
| --- | --- | --- | --- |
| Source identity | mini-site / mini-product clarity | page identity exists but proposition soft | `medium` |
| Intent purity | one host or surface for one cluster | query fit is tight | `strong` |
| Answer packaging | direct answer chunks | still too much user inference | `weak` |
| Tool funnel | content leads to useful action | tools exist but flow is loose | `medium` |
| Measurement surface | clear inventory and surfaces | structurally good | `strong` |
| Trust architecture | vertical-specific trust layer | inconsistent at page level | `weak` |
| Distinct value under scale | templates plus page-specific value | template leaning too hard | `medium` |

## 4. Core Strategic Interpretation

The most important lesson from the `Cuthongthai` framework is this:

- winning does not come from `more pages`
- winning does not come from `more schema`
- winning does not come from `host structure alone`

Winning comes from:

- clear surface identity
- clean intent
- fast answer delivery
- useful next-step actions
- measurement-friendly architecture
- trust signals that match the topic

For `checkgia`, this means:

- do not spend energy imitating the `subdomain` part
- spend energy turning `/vang/nhan-9999` into a sharper `mini-product surface`

## 5. Execution Backlog By Wave

### Wave 1: Fix What Breaks The Model

1. SSR real hero values
2. correct freshness messaging
3. remove `FAQPage` and `Dataset` schema
4. neutralize FAQ tone

Reason:

- these are the parts currently making the page less trustworthy and less clear

### Wave 2: Add Answer Layer

1. KPI row
2. spread summary block
3. historical delta labels
4. inline unit conversion

Reason:

- this is the layer that turns the page from `data display` into `decision support`

### Wave 3: Add Distinct Value

1. page-specific explanation block
2. source-link enrichment
3. seller-region detail if available

Reason:

- this is what protects the page from becoming only a template variant

## 6. One-Sentence Direction

`/vang/nhan-9999` should be rebuilt mentally as a mini-product page for same-day ring-gold buying decisions, not as a generic SEO page with a price table.`
