# VeryMath Star Entry — Design QA

## Design decision

- Keep one segmented GitHub / Star / count control beside the VeryMath name.
- Remove repository-level Star icons and counts from the website directory.
- Keep each repository name and its existing `Open Repo` action as the primary card navigation.
- Reserve repository-specific Star prompts for the corresponding repository README or documentation.

## Rationale

VeryMath is a multi-repository ecosystem. Showing a count for every repository added visual density and suggested a ranking between projects. One prominent Star control preserves a clear site-level invitation, while the repository directory stays focused on research areas and project descriptions.

## Verification checklist

- [x] The header control targets the `VeryMath/verymath.github.io` repository.
- [x] The header control has English and Chinese accessible labels.
- [x] The header count refreshes through one repository-level GitHub API request and retains a static fallback.
- [x] All nine repository Star controls and fallback counts are removed.
- [x] Repository names and `Open Repo` actions remain unchanged.
- [x] Responsive sizing and keyboard focus treatment remain available for the header control.

final result: passed
