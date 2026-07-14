# VeryMath Compact Repository Star Counts — Design QA

- Base visual truth: selected repository-card mockup from the design task.
- Refinement truth: user feedback in the current task — show repository Star counts and make the controls smaller.
- Desktop, mobile, full-view, and focused comparison captures were reviewed locally during implementation.
- Desktop viewport override: `1487 × 1058` (`1472 × 1058` rendered client area)
- Mobile viewport override: `390 × 844` (`375px` rendered client width)
- State: Chinese selected; repository directory; GitHub counts loaded.

## Findings

- No actionable P0, P1, or P2 differences remain.
- Intentional refinement: the original selected design used a visible `Star` label. The implementation now uses only the outlined star icon plus the current count, directly following the user's request for a smaller control with quantity.
- Accepted variance: the generated design uses wider cards and larger type than the production site. The implementation retains the existing `1160px` content width, card density, and typography because the requested change is limited to the repository Star controls.

## Full-view comparison evidence

The comparison confirms that the refined controls remain attached to repository names throughout the directory while preserving the two-column grid, gold card accent, metadata pills, bilingual copy, and separate `打开仓库` action. The compact icon-and-count treatment reduces visual competition with the repository names and keeps the grid easier to scan.

## Focused region comparison evidence

The focused `AI4Math-Evolving` and `AI4Math-Auto-Research` comparison shows the intentional transition from labeled Star buttons to 26px-high icon-and-count controls. The controls remain on the same baseline as each repository name, retain the selected outline treatment, and now display the live fallback values `0` and `2`.

No additional focused crop is needed because all nine controls share the same markup, class, dimensions, icon, count updater, hover state, and focus state.

## Required fidelity surfaces

- Fonts and typography: existing repository headings and card copy remain unchanged. Count numerals use 12px/700 text with tabular numerals, and long repository names continue to wrap without clipping.
- Spacing and layout rhythm: each control is 26px high, 44px wide for a single-digit count, uses a 4px internal gap, 8px horizontal padding, and a 6px radius. The existing 10px title-group gap is preserved.
- Colors and visual tokens: the controls retain the VeryMath blue-gray secondary treatment (`#42526b`, `#d7e0ec`, white, and `--vm-bg`) with visible hover and focus affordances.
- Image quality and asset fidelity: all existing institutional and VeryMath assets are unchanged. Primer Octicons supplies the star icon; all nine icons loaded at their native `16 × 16` source size and render at `14 × 14`.
- Copy and content: the visible `Star` word is intentionally removed to save space. Repository-specific bilingual accessible labels retain the action meaning and announce the current count.

## Interaction and runtime checks

- Nine compact controls render for nine unique repository names and destinations.
- Static fallback counts match the GitHub organization response captured on 2026-07-14: Paper Reading `1`, Optimization `0`, Computational Mathematics `0`, Lean Agents `2`, Evolving `0`, Auto Research `2`, Paper Writing `1`, SageMath `6`, and co-mathematician `2`.
- One request to `https://api.github.com/orgs/VeryMath/repos?per_page=100&type=public` refreshes all repository counts and the title-level `verymath.github.io` count; no per-card requests are made.
- If the API is unavailable, the static counts and all GitHub links remain usable.
- Repository-specific accessible labels update in English and Chinese after counts load.
- Desktop controls measured `26 × 44px` for single-digit counts.
- Mobile controls remain `26 × 44px`; the page client width and scroll width both measured `375px`, so there is no horizontal overflow.
- Browser console check returned no warnings or errors.

## Comparison history

1. The selected design introduced labeled Star actions after repository names.
2. The first implementation reproduced those actions at 30px high and passed desktop/mobile QA.
3. User feedback requested visible quantities and a smaller footprint.
4. The controls were reduced to 26px, the visible label was replaced by the count, static fallbacks were added, and one organization-level API request was used for live updates. Desktop and mobile post-change captures showed no P0/P1/P2 regressions.

## Implementation checklist

- [x] Show a count beside every repository star icon.
- [x] Reduce control height, type, padding, radius, and icon size.
- [x] Refresh all counts with one GitHub organization request.
- [x] Retain static fallbacks when the API fails.
- [x] Preserve repository-specific links, secure new-tab behavior, and bilingual accessible labels.
- [x] Verify desktop, mobile, count values, icon loading, overflow, and console state.

## Follow-up polish

- P3: vendor the Primer Octicon files locally if the site later adopts a strict content-security policy or removes CDN dependencies.

final result: passed
