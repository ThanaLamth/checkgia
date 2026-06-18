# Dev Prompt For Improving SEO And AISO On `checkgia.com/vang`

Date: 2026-06-18

Use this prompt as the primary handoff to engineering.

## Prompt

You are implementing SEO, AISO, and UX improvements for the gold section of `checkgia.com`, starting with:

- `https://checkgia.com/vang`
- `https://checkgia.com/vang/nhan-9999`

Your goal is to improve:

- classic SEO alignment
- Google AI features readiness
- decision-support usefulness for users

Do not treat this as a “schema-only” or “meta-tag-only” task.

The important principle is:

- make the pages more indexable
- make the important content more visible in rendered HTML
- make the page answers clearer and more trustworthy
- improve the `content -> tool` flow without weakening the page’s main intent

## What To Build

### 1. Fix Hero SSR On Entity Pages

Priority:

- critical

Pages:

- at minimum `https://checkgia.com/vang/nhan-9999`
- ideally the same fix should apply to other gold entity pages using the same template

Problem:

- the page still renders placeholder `—` values in the hero for key numbers even though the table below has real prices

Required implementation:

- server-render the hero with real values:
  - best source
  - best sell price
  - buy price
  - sell price
  - update time

Do not:

- rely on client hydration for these primary numbers

Acceptance:

- fetching the page HTML must show real hero values, not placeholders

### 2. Improve Freshness Messaging

Priority:

- critical

Pages:

- `/vang`
- `/vang/nhan-9999`

Problem:

- freshness wording is too broad or too casual
- source timestamps and copy are not aligned tightly enough

Required implementation:

- change copy to reflect source-level freshness
- make it clear that each source updates independently
- if data is older than expected, label that explicitly

Do not:

- claim freshness in a way that overstates confidence

### 3. Remove Low-Value Schema

Priority:

- critical

Pages:

- `/vang`
- gold entity pages, starting with `/vang/nhan-9999`

Required implementation:

- remove `FAQPage` JSON-LD
- remove `Dataset` JSON-LD where present

Keep:

- `Organization`
- `BreadcrumbList`
- `Product` / `AggregateOffer` where relevant

Reason:

- `FAQPage` is no longer a Google Search rich-result lever
- `Dataset` is not for normal Google Search on these pages

### 4. Rewrite FAQ Tone And Utility Copy

Priority:

- high

Pages:

- `/vang`
- `/vang/nhan-9999`

Problem:

- current copy includes:
  - `mày`
  - `Tao`
  - `magic link`
  - `cross threshold`
- that weakens trust for money-adjacent pages

Required implementation:

- rewrite in neutral Vietnamese
- shorten FAQs to practical questions only

### 5. Add Direct Answer Layer To `/vang/nhan-9999`

Priority:

- high

Required implementation:

- add a short answer block above the detailed comparison table
- include:
  - current lowest sell price
  - best source
  - spread summary
  - freshness summary

Example output style:

- `Giá bán thấp nhất hiện tại là ...`
- `Nguồn có spread hẹp hơn là ...`
- `Nguồn cũ hơn ngưỡng kỳ vọng sẽ được đánh dấu`

### 6. Add Decision KPI Row To `/vang/nhan-9999`

Priority:

- high

Required implementation:

- add SSR KPI cards:
  - `So với hôm qua`
  - `So với 7 ngày`
  - `So với 30 ngày`
  - `So với 1 năm`

Each KPI should show:

- absolute delta
- percentage delta where possible

### 7. Improve Source Table

Priority:

- high

Required implementation:

- add spread per source
- add freshness badge per source
- keep:
  - buy
  - sell
  - delta vs previous snapshot
  - timestamp

Badges should distinguish:

- cheapest
- low spread
- stale

### 8. Add A Small Savings Comparison Widget

Priority:

- medium

Page:

- `/vang/nhan-9999`

Required implementation:

- add a compact decision-support widget titled like:
  - `Nếu chưa mua vàng hôm nay`
- compare:
  - buying now
  - waiting briefly with a short deposit assumption

Do not:

- embed a full banking comparison table
- turn the gold page into a savings page

See:

- `docs/nhan-9999-savings-widget-spec.md`

### 9. Improve `/vang` As A Better Hub Page

Priority:

- high

Required implementation:

- make `/vang` read as a stronger category hub, not just a list page
- add a short intro that explains:
  - what the page covers
  - how to compare products
  - where to go for per-brand pages
- keep the entity grid
- keep links to brand pages
- keep links to historical date pages

Recommended additions:

- a short summary block:
  - what gold products are tracked
  - which ones update more frequently
  - what users should click depending on their intent
- cleaner, more neutral FAQ

### 10. Keep The `content -> tool` Flow, But Reorder It

Priority:

- medium

Required implementation:

- put the most decision-critical blocks before generic tools

Recommended order on `/vang/nhan-9999`:

1. hero
2. KPI row
3. source comparison
4. spread/freshness summary
5. transaction conversion
6. savings comparison widget
7. history context
8. calculators
9. FAQ

## Non-Negotiables

Do not:

- add more generic FAQ just to “improve SEO”
- add AI-only hacks or fake AIO technical features
- add more schema unless it clearly helps real Search eligibility
- hide important numbers behind client-only rendering
- make `/vang/nhan-9999` drift into a broad finance page

## Definition Of Done

The task is done when:

1. hero values on entity pages render as real numbers in HTML
2. `/vang` and `/vang/nhan-9999` no longer output `FAQPage`
3. entity pages no longer output `Dataset`
4. FAQ tone is neutral and product-helpful
5. `/vang/nhan-9999` has a direct answer block and KPI row
6. source comparison includes spread and freshness
7. `/vang` works as a clearer gold hub
8. the savings comparison widget is present but compact

## Validation

After implementation:

- run the QA checklist in `docs/vang-qa-checklist.md`
- run the script in `scripts/check-vang-page.py`
- if checks fail, iterate until clean
