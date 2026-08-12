# VeryMath Contributor Roster and Bilingual Names Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build one 21-person VeryMath contributor wall with the advisor first, every other member surname-sorted, language-specific names, and GitHub links only for confirmed accounts.

**Architecture:** `_data/contributors.json` remains the single identity and display-order source. Jekyll/Liquid emits both language variants into each card and relies on the existing global language switch for visibility; Python unit tests lock the schema, roster, order, and link behavior, while Playwright validates runtime language switching, avatar fallbacks, responsive layout, and four visual snapshots.

**Tech Stack:** Jekyll/Liquid, JSON, Ruby with Liquid 4.0.4, Python 3 `unittest`, Node.js, Playwright 1.62.1, local Chrome.

## Global Constraints

- Render exactly 21 unique people in one `Contributors / 贡献者` section.
- Keep Xiangfeng Wang / 王祥丰 as the only `advisor` and the first record.
- Keep the other 20 records in the approved Chinese-surname-pinyin order; use given-name pinyin for equal surnames.
- English names use given-name-first order; Chinese names use the approved Chinese spelling.
- Preserve exactly 11 confirmed GitHub mappings; never infer a GitHub account from email, avatar similarity, or a similar username.
- Records without confirmed GitHub accounts use language-specific fallback initials, have no image, show no handle, and are not links.
- Do not publish presentation photos, email addresses, grades, majors, rankings, or contribution counts.
- Do not add GitHub API requests; avatar URLs remain `https://github.com/<login>.png?size=160`.
- Do not modify unrelated homepage sections, merge the branch, push it, or publish the website.

## File Map

- `_data/contributors.json`: authoritative bilingual roster, role, order, confirmed GitHub mapping, and provenance.
- `index.md`: contributor copy and Liquid card rendering only; no duplicate roster or JavaScript translation dictionary.
- `tests/test_contributors.py`: deterministic schema, identity, ordering, bilingual DOM, and link-contract tests.
- `tests/verify_contributors_browser.cjs`: runtime language, avatar-failure, responsive-layout, and screenshot checks.
- `tests/README.md`: exact local validation and screenshot behavior.
- `docs/superpowers/specs/2026-08-12-contributor-bilingual-names-design.md`: implementation status after all gates pass.

---

### Task 1: Migrate the roster and render bilingual cards

**Files:**
- Modify: `tests/test_contributors.py:11-275`
- Modify: `_data/contributors.json:1-113`
- Modify: `index.md:1265-1292`

**Interfaces:**
- Consumes: `site.data.contributors`, an ordered JSON array.
- Produces: records with exact keys `name_en`, `name_zh`, `github`, `initial_en`, `initial_zh`, `role`, and `evidence`; HTML cards containing `.vm-contributor-name > .lang-en/.lang-zh` and `.vm-contributor-initial > .lang-en/.lang-zh`.

- [ ] **Step 1: Write failing registry and DOM tests**

Replace the old single-language constants with the approved ordered data:

```python
EXPECTED_CONTRIBUTORS = [
    ("Xiangfeng Wang", "王祥丰", "advisor", "xfwang87"),
    ("Yaling Chen", "陈亚玲", "member", None),
    ("Miao Dong", "董淼", "member", None),
    ("Yun Hua", "华贇", "member", "hyyh28"),
    ("Boxian Jiang", "蒋博先", "member", "Joseph20060208"),
    ("Rujing Li", "黎汝婧", "member", None),
    ("Shuangxi Li", "李爽夕", "member", "ricercar77"),
    ("Yipeng Lin", "林依鹏", "member", None),
    ("Chen Ling", "凌晨", "member", None),
    ("Yunfeng Lu", "陆云峰", "member", None),
    ("Quan Sun", "孙权", "member", None),
    ("Haoru Tang", "汤皓如", "member", "tang0805-em"),
    ("Zhuojie Tu", "涂卓杰", "member", "Tu-ZJ"),
    ("Nuoqian Wang", "王诺千", "member", None),
    ("Yihong Wei", "尉毅宏", "member", "Imccark"),
    ("Mengyuan Xing", "邢梦圆", "member", "IsRivulet"),
    ("Conan Xu", "徐柯楠", "member", "ConanXu-math"),
    ("Dong Yuan", "袁东", "member", "dyuan311"),
    ("Siyu Zhang", "张司雨", "member", "rain37233-del"),
    ("Xiaowen Zhang", "张笑玟", "member", None),
    ("Zhixin Zheng", "郑智心", "member", None),
]
EXPECTED_NAMES_EN = [item[0] for item in EXPECTED_CONTRIBUTORS]
EXPECTED_NAMES_ZH = [item[1] for item in EXPECTED_CONTRIBUTORS]
EXPECTED_GITHUB = {item[0]: item[3] for item in EXPECTED_CONTRIBUTORS if item[3]}
TEAM_NAMES_ZH = {
    "李爽夕", "林依鹏", "凌晨", "汤皓如", "涂卓杰", "王诺千", "邢梦圆",
    "陈亚玲", "蒋博先", "黎汝婧", "尉毅宏", "徐柯楠", "袁东", "张司雨",
}
TEAM_SOURCE = "team-introduction-2026-06-30"
```

Update `ContributorRegistryTests` with concrete schema and ordering assertions:

```python
def test_registry_matches_the_approved_order(self):
    actual = [
        (record["name_en"], record["name_zh"], record["role"], record["github"])
        for record in self.records
    ]
    self.assertEqual(actual, EXPECTED_CONTRIBUTORS)

def test_records_have_complete_bilingual_schema_and_sources(self):
    self.assertEqual(len(self.records), 21)
    self.assertEqual(len({record["name_en"] for record in self.records}), 21)
    self.assertEqual(len({record["name_zh"] for record in self.records}), 21)
    for record in self.records:
        self.assertEqual(
            set(record),
            {"name_en", "name_zh", "github", "initial_en", "initial_zh", "role", "evidence"},
        )
        self.assertRegex(record["initial_en"], r"^[A-Z]{1,3}$")
        self.assertRegex(record["initial_zh"], r"^.$")
        self.assertTrue(record["evidence"])
        self.assertTrue(
            all(source == TEAM_SOURCE or source.startswith("https://github.com/") for source in record["evidence"])
        )

def test_advisor_is_unique_and_first(self):
    advisors = [record for record in self.records if record["role"] == "advisor"]
    self.assertEqual([record["name_zh"] for record in advisors], ["王祥丰"])
    self.assertEqual(self.records[0]["name_zh"], "王祥丰")
    self.assertTrue(all(record["role"] == "member" for record in self.records[1:]))

def test_team_introduction_members_are_all_present(self):
    self.assertTrue(TEAM_NAMES_ZH.issubset({record["name_zh"] for record in self.records}))
    team_sourced = {record["name_zh"] for record in self.records if TEAM_SOURCE in record["evidence"]}
    self.assertEqual(team_sourced, TEAM_NAMES_ZH)

def test_only_confirmed_github_accounts_are_linked(self):
    linked = {record["name_en"]: record["github"] for record in self.records if record["github"]}
    self.assertEqual(linked, EXPECTED_GITHUB)
    self.assertEqual(len(linked), 11)
    self.assertEqual(len(linked.values()), len({value.lower() for value in linked.values()}))
    for github in linked.values():
        self.assertRegex(github, re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$"))
```

Change homepage assertions to locate the nested language nodes and verify both ordered name lists. Delete the old identity-specific tests that depended on a single `.vm-contributor-name` string; the ordered bilingual list and generic mapping test below cover those identities without duplicating implementation details:

```python
def language_text(card, language):
    name = find_one(card, lambda node: "vm-contributor-name" in node.classes)
    return find_one(name, lambda node: f"lang-{language}" in node.classes).text()

def test_every_registry_entry_renders_once_without_ranking(self):
    self.assertEqual(len(self.cards), 21)
    self.assertEqual([language_text(card, "en") for card in self.cards], EXPECTED_NAMES_EN)
    self.assertEqual([language_text(card, "zh") for card in self.cards], EXPECTED_NAMES_ZH)
    self.assertEqual(language_text(self.cards[0], "zh"), "王祥丰")
    self.assertNotIn("contributions", self.section.text().lower())
    self.assertNotIn("ranking", self.section.text().lower())

def test_contributor_copy_includes_teamwork_and_guidance(self):
    lead = find_one(self.section, lambda node: "vm-lead" in node.classes)
    english = find_one(lead, lambda node: "lang-en" in node.classes)
    chinese = find_one(lead, lambda node: "lang-zh" in node.classes)
    self.assertEqual(
        english.text(),
        "We thank everyone who contributes tools, workflows, research infrastructure, teamwork, and guidance to VeryMath.",
    )
    self.assertEqual(
        chinese.text(),
        "感谢所有为 VeryMath 的工具、工作流、科研基础设施、团队协作与指导支持作出贡献的参与者。",
    )

def test_only_confirmed_accounts_render_links_and_lazy_avatars(self):
    records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))
    cards_by_name = {language_text(card, "en"): card for card in self.cards}
    for record in records:
        with self.subTest(name=record["name_en"]):
            card = cards_by_name[record["name_en"]]
            images = [node for node in descendants(card) if node.tag == "img"]
            handles = [node for node in descendants(card) if "vm-contributor-handle" in node.classes]
            if record["github"]:
                self.assertEqual(card.tag, "a")
                self.assertEqual(card.attrs.get("href"), f"https://github.com/{record['github']}")
                self.assertEqual(len(images), 1)
                self.assertEqual(images[0].attrs.get("src"), f"https://github.com/{record['github']}.png?size=160")
                self.assertEqual(images[0].attrs.get("loading"), "lazy")
                self.assertEqual([handle.text() for handle in handles], [f"@{record['github']}"])
            else:
                self.assertEqual(card.tag, "div")
                self.assertNotIn("href", card.attrs)
                self.assertEqual(images, [])
                self.assertEqual(handles, [])
```

- [ ] **Step 2: Run the unit suite and verify the new tests fail**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: FAIL because current records do not have `name_en`, `name_zh`, `initial_en`, `initial_zh`, or `role`, and only 16 cards render.

- [ ] **Step 3: Replace the contributor registry with the approved schema and order**

Write the 21 records in the exact `EXPECTED_CONTRIBUTORS` order. Use these initials and sources:

```text
Xiangfeng Wang | 王祥丰 | XW | 王 | https://github.com/xfwang87
Yaling Chen | 陈亚玲 | YC | 陈 | team-introduction-2026-06-30
Miao Dong | 董淼 | MD | 董 | https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md
Yun Hua | 华贇 | YH | 华 | https://github.com/VeryMath/verymath.github.io/commits/main/?author=hyyh28
Boxian Jiang | 蒋博先 | BJ | 蒋 | https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md ; https://github.com/VeryMath/skill-Finite-Element-Analysis/commit/94c1545b7efa262efe0dd4db09e4f0e43c0cd16d ; team-introduction-2026-06-30
Rujing Li | 黎汝婧 | RL | 黎 | team-introduction-2026-06-30
Shuangxi Li | 李爽夕 | SL | 李 | https://github.com/VeryMath/AI4Math-Optimization/blob/main/CONTRIBUTORS.md ; https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md ; team-introduction-2026-06-30
Yipeng Lin | 林依鹏 | YL | 林 | team-introduction-2026-06-30
Chen Ling | 凌晨 | CL | 凌 | team-introduction-2026-06-30
Yunfeng Lu | 陆云峰 | YL | 陆 | https://github.com/VeryMath/AI4Math-MathTool/blob/main/CONTRIBUTORS.md
Quan Sun | 孙权 | QS | 孙 | https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md
Haoru Tang | 汤皓如 | HT | 汤 | https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md ; https://github.com/VeryMath/AI4Math-Computational-Mathematics/commit/8978f0204fae7cfa1c865fd3382776ef7bbaf7ec ; team-introduction-2026-06-30
Zhuojie Tu | 涂卓杰 | ZT | 涂 | https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md ; team-introduction-2026-06-30
Nuoqian Wang | 王诺千 | NW | 王 | team-introduction-2026-06-30
Yihong Wei | 尉毅宏 | YW | 尉 | https://github.com/VeryMath/AI4Math-Sagemath-skill/commits/main/?author=Imccark ; team-introduction-2026-06-30
Mengyuan Xing | 邢梦圆 | MX | 邢 | https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md ; team-introduction-2026-06-30
Conan Xu | 徐柯楠 | CX | 徐 | https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md ; team-introduction-2026-06-30
Dong Yuan | 袁东 | DY | 袁 | https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md ; https://github.com/VeryMath/AI4Math-Auto-Research/pull/7 ; team-introduction-2026-06-30
Siyu Zhang | 张司雨 | SZ | 张 | https://github.com/VeryMath/AI4Math-Lean-Agents/blob/main/CONTRIBUTORS.md ; https://github.com/VeryMath/AI4Math-Lean-Agents/commit/709869640f9f65403f646edc64433f5c0c9a99b7 ; team-introduction-2026-06-30
Xiaowen Zhang | 张笑玟 | XZ | 张 | https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md
Zhixin Zheng | 郑智心 | ZZ | 郑 | https://github.com/VeryMath/AI4Math-MathTool/blob/main/CONTRIBUTORS.md
```

For every row, set `role` to `member` except Xiangfeng Wang, whose role is `advisor`. Preserve the 11 GitHub values in `EXPECTED_GITHUB`; use JSON `null` for all other GitHub fields. Treat each semicolon-separated source above as a separate string in the record's `evidence` array.

- [ ] **Step 4: Render both language variants in the existing card template**

Update the section copy and replace each single-language initial/name expression with nested language spans:

```liquid
<span class="lang-en">We thank everyone who contributes tools, workflows, research infrastructure, teamwork, and guidance to VeryMath.</span>
<span class="lang-zh">感谢所有为 VeryMath 的工具、工作流、科研基础设施、团队协作与指导支持作出贡献的参与者。</span>
```

Use this structure in both linked and static cards:

```liquid
<span class="vm-contributor-avatar" aria-hidden="true">
  <span class="vm-contributor-initial">
    <span class="lang-en">{{ contributor.initial_en | escape }}</span>
    <span class="lang-zh">{{ contributor.initial_zh | escape }}</span>
  </span>
  {% if contributor.github %}
    <img class="vm-contributor-image" src="https://github.com/{{ contributor.github | escape }}.png?size=160" alt="" width="64" height="64" loading="lazy" decoding="async" onload="this.classList.add('vm-contributor-image-loaded')" onerror="this.hidden = true">
  {% endif %}
</span>
<span class="vm-contributor-name">
  <span class="lang-en">{{ contributor.name_en | escape }}</span>
  <span class="lang-zh">{{ contributor.name_zh | escape }}</span>
</span>
```

Keep the existing outer `{% if contributor.github %}` branch so linked records remain `<a>` cards with one handle and static records remain `<div>` cards with no `href`, image, or handle. Do not render `role` or `evidence`.

- [ ] **Step 5: Run the complete unit suite and verify it passes**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all tests PASS with 21 cards, 11 linked cards, 10 static cards, and the advisor first in both languages.

- [ ] **Step 6: Commit the roster and template change**

```bash
git add _data/contributors.json index.md tests/test_contributors.py
git commit -m "feat: add complete bilingual contributor roster"
```

---

### Task 2: Strengthen runtime and visual verification

**Files:**
- Modify: `tests/verify_contributors_browser.cjs:8-256`
- Modify: `tests/README.md:1-19`

**Interfaces:**
- Consumes: the 21-record registry and rendered `.vm-contributor-card`, `.lang-en`, `.lang-zh`, `.vm-contributor-initial`, and `.vm-contributor-image` nodes from Task 1.
- Produces: one JSON QA report plus `contributors-desktop-en.png`, `contributors-desktop-zh.png`, `contributors-mobile-en.png`, and `contributors-mobile-zh.png` when `VERYMATH_SCREENSHOT_DIR` is set.

- [ ] **Step 1: Run the existing browser test as a baseline**

Run with the already installed Playwright location if available; otherwise use the documented temporary install:

```bash
VM_PLAYWRIGHT_DIR="$(mktemp -d)"
npm install --prefix "$VM_PLAYWRIGHT_DIR" playwright@1.62.1
NODE_PATH="$VM_PLAYWRIGHT_DIR/node_modules" node tests/verify_contributors_browser.cjs
```

Expected: PASS for the existing avatar and responsive checks.

- [ ] **Step 2: Add exact bilingual sequence and fallback assertions**

Derive expected sequences directly from the registry:

```javascript
const expectedEnglishNames = contributors.map((contributor) => contributor.name_en);
const expectedChineseNames = contributors.map((contributor) => contributor.name_zh);
assert.equal(expectedCardCount, 21);
assert.equal(expectedLinkedCount, 11);
assert.equal(expectedStaticCount, 10);
```

Inside the existing pre-switch `page.evaluate`, add these fields to the returned report:

```javascript
englishNames: [...section.querySelectorAll(".vm-contributor-name .lang-en")].map((node) =>
  node.textContent.trim(),
),
failedInitialText: failedInitial.innerText.trim(),
```

Replace the post-switch Chinese inspection with:

```javascript
const chinese = await page.evaluate(() => {
  const section = document.querySelector('[aria-labelledby="vm-contributors-title"]');
  const failedImage = section.querySelector('img[src*="ConanXu-math.png"]');
  const failedInitial = failedImage.parentElement.querySelector(".vm-contributor-initial");
  return {
    title: document.querySelector("#vm-contributors-title").innerText.trim(),
    lang: document.documentElement.lang,
    overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
    names: [...section.querySelectorAll(".vm-contributor-name .lang-zh")].map((node) =>
      node.textContent.trim(),
    ),
    failedInitialText: failedInitial.innerText.trim(),
  };
});
```

Then assert:

```javascript
assert.deepEqual(report.englishNames, expectedEnglishNames);
assert.deepEqual(chinese.names, expectedChineseNames);
assert.equal(report.englishNames[0], "Xiangfeng Wang");
assert.equal(chinese.names[0], "王祥丰");
assert.equal(report.failedInitialText, "CX");
assert.equal(chinese.failedInitialText, "徐");
```

Select visible names with `.vm-contributor-name .lang-en` before the switch and `.vm-contributor-name .lang-zh` after the switch. Select fallback text from the failed `ConanXu-math` image's closest `.vm-contributor-avatar`.

- [ ] **Step 3: Generate clean screenshots for both languages and viewports**

Replace the current clean-screenshot helper with:

```javascript
async function captureCleanScreenshot(browser, url, viewport, language, screenshotName) {
  const screenshotDir = process.env.VERYMATH_SCREENSHOT_DIR;
  if (!screenshotDir) return null;

  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".vm-contributor-card");
  const avatarImages = page.locator(".vm-contributor-avatar img");
  for (let index = 0; index < (await avatarImages.count()); index += 1) {
    await avatarImages.nth(index).scrollIntoViewIfNeeded();
  }
  await page.waitForFunction(
    (expected) => {
      const images = [...document.querySelectorAll(".vm-contributor-avatar img")];
      return (
        images.length === expected &&
        images.every(
          (image) =>
            image.hidden ||
            (image.complete && image.naturalWidth > 0 && getComputedStyle(image).opacity === "1"),
        )
      );
    },
    expectedLinkedCount,
  );

  await page.click(`[data-set-lang="${language}"]`);
  const expectedNames = language === "zh" ? expectedChineseNames : expectedEnglishNames;
  const visibleNames = (
    await page.locator(`.vm-contributor-name .lang-${language}`).allTextContents()
  ).map((name) => name.trim());
  assert.deepEqual(visibleNames, expectedNames);
  assert.equal(await page.locator("html").getAttribute("lang"), language === "zh" ? "zh-CN" : "en");

  const realDongYuanAvatarLoaded = await page.evaluate(() => {
    const image = document.querySelector('img[src*="dyuan311.png"]');
    return Boolean(
      image &&
        !image.hidden &&
        image.complete &&
        image.naturalWidth > 0 &&
        getComputedStyle(image).opacity === "1"
    );
  });
  assert.equal(realDongYuanAvatarLoaded, true);

  fs.mkdirSync(screenshotDir, { recursive: true });
  const screenshotPath = path.join(screenshotDir, screenshotName);
  await page.locator('[aria-labelledby="vm-contributors-title"]').screenshot({
    path: screenshotPath,
  });
  await page.close();
  return { screenshotPath, language, visibleNames, realDongYuanAvatarLoaded };
}
```

Call it four times with these exact filenames:

```javascript
const screenshots = {
  desktopEnglish: await captureCleanScreenshot(browser, url, desktopViewport, "en", "contributors-desktop-en.png"),
  desktopChinese: await captureCleanScreenshot(browser, url, desktopViewport, "zh", "contributors-desktop-zh.png"),
  mobileEnglish: await captureCleanScreenshot(browser, url, mobileViewport, "en", "contributors-mobile-en.png"),
  mobileChinese: await captureCleanScreenshot(browser, url, mobileViewport, "zh", "contributors-mobile-zh.png"),
};
```

Retain the real Dong Yuan avatar assertion on every clean screenshot page. Extend the JSON report with `screenshots`.

- [ ] **Step 4: Update the validation documentation**

Keep the pinned commands in `tests/README.md` and replace the final explanation with:

```markdown
The browser command verifies the 21-card bilingual order, confirmed/static card counts, language-specific fallback initials, avatar loading and fault handling, and responsive overflow. When `VERYMATH_SCREENSHOT_DIR` is set, it writes English and Chinese contributor-section screenshots for desktop and mobile viewports.
```

- [ ] **Step 5: Run the enhanced browser verification**

Run:

```bash
VM_PLAYWRIGHT_DIR="$(mktemp -d)"
npm install --prefix "$VM_PLAYWRIGHT_DIR" playwright@1.62.1
VM_SCREENSHOT_DIR="$(mktemp -d)"
NODE_PATH="$VM_PLAYWRIGHT_DIR/node_modules" VERYMATH_SCREENSHOT_DIR="$VM_SCREENSHOT_DIR" node tests/verify_contributors_browser.cjs
```

Expected: PASS; JSON reports 21 cards, 11 linked, 10 static, no horizontal overflow at 1366×900 or 390×844, correct name order in both languages, and four screenshot paths under `$VM_SCREENSHOT_DIR`.

- [ ] **Step 6: Commit the browser QA change**

```bash
git add tests/verify_contributors_browser.cjs tests/README.md
git commit -m "test: verify bilingual contributor wall"
```

---

### Task 3: Run release gates and mark the design implemented

**Files:**
- Modify: `docs/superpowers/specs/2026-08-12-contributor-bilingual-names-design.md:3`

**Interfaces:**
- Consumes: Task 1's unit-testable roster/template and Task 2's four screenshot outputs.
- Produces: a clean branch state whose design status accurately says `已实现` only after every automated and visual gate passes.

- [ ] **Step 1: Run deterministic tests and whitespace validation**

```bash
python3 -m unittest discover -s tests -v
git diff --check
```

Expected: all tests PASS and `git diff --check` prints nothing.

- [ ] **Step 2: Run the final browser gate with fresh screenshots**

```bash
VM_PLAYWRIGHT_DIR="$(mktemp -d)"
npm install --prefix "$VM_PLAYWRIGHT_DIR" playwright@1.62.1
VM_FINAL_SCREENSHOTS="$(mktemp -d)"
NODE_PATH="$VM_PLAYWRIGHT_DIR/node_modules" VERYMATH_SCREENSHOT_DIR="$VM_FINAL_SCREENSHOTS" node tests/verify_contributors_browser.cjs
```

Expected: PASS with four PNG files and no console assertion errors.

- [ ] **Step 3: Inspect all four screenshots at full size**

Open each generated PNG with the local image viewer and confirm:

- Xiangfeng Wang / 王祥丰 is the first card;
- every card has a visible, untruncated name;
- `Joseph20060208`, `Xiangfeng Wang`, and `Xiaowen Zhang` do not clip or collide;
- English screenshots contain no visible Chinese names, and Chinese screenshots contain no visible English names;
- the 21-card grid has no overlap or horizontal overflow at either viewport;
- unconfirmed accounts use clean initials and show no blank handle row.

If any criterion fails, fix the responsible source/test file, rerun Steps 1-3, and do not change the design status.

- [ ] **Step 4: Mark the approved design implemented and commit**

Change only:

```markdown
状态：已实现
```

Then run and commit:

```bash
git diff --check
git add docs/superpowers/specs/2026-08-12-contributor-bilingual-names-design.md
git commit -m "docs: mark contributor roster implemented"
```

- [ ] **Step 5: Verify the final branch state**

```bash
git status --short --branch
git log -6 --oneline --decorate
```

Expected: branch `codex/contributors-homepage`, no uncommitted files, and separate feature, browser-QA, and design-status commits. Do not merge, push, or publish.
