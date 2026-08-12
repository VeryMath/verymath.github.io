# VeryMath Homepage Contributors Section Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

> **Post-implementation identity audit (2026-08-12):** Preserved branch/source history confirmed `rain37233 → rain37233-del`, `tanghaoru → tang0805-em`, and `蒋博先 → Joseph20060208`; the user subsequently confirmed that `hyyh28` is 华贇, `IsRivulet` is 邢梦圆, `rain37233` is 张司雨, `ricercar77` is 李爽夕, and the `njustar2002` attribution belongs to 郑智心. The current registry therefore renders 15 people as nine linked and six static cards; 郑智心 remains static because `njustar2002` is not a usable GitHub profile. Fault-injection avatar checks and clean visual screenshots are now separate; the step-by-step snippets below retain the original pre-audit plan values.

**Goal:** Add a bilingual, responsive homepage section that credits all 15 verified, deduplicated actual VeryMath contributors, including people whom GitHub's contributor API misses.

**Architecture:** Store reviewed public attribution in `_data/contributors.json` and render it at Jekyll build time with a Liquid loop in `index.md`. Keep the browser independent of contributor APIs; GitHub-linked people receive public profile avatars, while everyone retains a text-initial fallback. Validate the registry with Python, render the real Liquid template with Liquid 4.0.4, and exercise the rendered page in Chrome at desktop and mobile widths.

**Tech Stack:** Jekyll data files, Liquid 4.0.4, HTML/CSS, Python 3.9 `unittest`, Ruby 2.6, Playwright 1.62.1 with installed Chrome.

## Global Constraints

- The scope is actual contributors across all public repositories in the `VeryMath` GitHub organization, not only `verymath.github.io` contributors or organization members.
- The current registry contains exactly the 15 deduplicated public identities approved in `docs/superpowers/specs/2026-08-12-contributors-section-design.md`.
- Never infer a GitHub account from a similar name, organization membership, or private email.
- Do not publish private roster fields, grades, majors, email addresses, contribution counts, or rankings.
- Do not add a contributor API request; the existing site-repository Star API request remains unchanged.
- Keep English and Chinese content compatible with the existing `.lang-en` and `.lang-zh` switch.
- Preserve the existing course-release work on `codex/publish-course-tools` and do not touch `.DS_Store` or `assets/.DS_Store`.
- Do not push or publish the website as part of this implementation.

## File Structure

- Create `_data/contributors.json`: reviewed, stable source of public contributor identity and evidence.
- Modify `index.md`: contributor card styles and Liquid-rendered homepage section only.
- Create `tests/test_contributors.py`: registry and rendered-page contract tests using only the Python standard library.
- Create `tests/render_homepage.rb`: strict Liquid renderer for the real `index.md` and `_layouts/default.html` templates.
- Create `tests/verify_contributors_browser.cjs`: Chrome checks for layout, language switching, card counts, and avatar failure fallback.
- Create `tests/README.md`: exact local dependency and validation commands.

---

### Task 1: Establish the Reviewed Contributor Registry

**Files:**
- Create: `_data/contributors.json`
- Create: `tests/test_contributors.py`

**Interfaces:**
- Consumes: The 16-person attribution decision in `docs/superpowers/specs/2026-08-12-contributors-section-design.md`.
- Produces: `site.data.contributors`, an ordered array of records with `name: string`, `github: string | null`, `initial: string`, and `evidence: string[]`.

- [ ] **Step 1: Write the failing registry tests**

Create `tests/test_contributors.py` with this content:

```python
import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRIBUTORS_PATH = ROOT / "_data" / "contributors.json"
EXPECTED_NAMES = [
    "Conan Xu",
    "Dong Yuan",
    "hyyh28",
    "IsRivulet",
    "Miao Dong",
    "njustar2002",
    "Quan Sun",
    "rain37233",
    "ricercar77",
    "tanghaoru",
    "Xiaowen Zhang",
    "Yihong Wei",
    "Yunfeng Lu",
    "Zhuojie Tu",
    "李爽夕",
    "蒋博先",
]
EXPECTED_GITHUB = {
    "Conan Xu": "ConanXu-math",
    "Dong Yuan": "dyuan311",
    "hyyh28": "hyyh28",
    "IsRivulet": "IsRivulet",
    "ricercar77": "ricercar77",
    "tanghaoru": "tanghaoru",
    "Yihong Wei": "Imccark",
}


class ContributorRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))

    def test_registry_contains_each_verified_public_identity_once(self):
        names = [record["name"] for record in self.records]
        self.assertEqual(names, EXPECTED_NAMES)
        self.assertEqual(len(names), len(set(names)))

    def test_records_are_renderable_and_have_public_evidence(self):
        self.assertEqual(len(self.records), 16)
        for record in self.records:
            with self.subTest(name=record.get("name")):
                self.assertEqual(set(record), {"name", "github", "initial", "evidence"})
                self.assertIsInstance(record["name"], str)
                self.assertTrue(record["name"].strip())
                self.assertIsInstance(record["initial"], str)
                self.assertRegex(record["initial"], r"^.{1,3}$")
                self.assertIsInstance(record["evidence"], list)
                self.assertTrue(record["evidence"])
                self.assertTrue(all(item.startswith("https://github.com/VeryMath/") for item in record["evidence"]))

    def test_only_confirmed_github_accounts_are_linked(self):
        linked = {record["name"]: record["github"] for record in self.records if record["github"]}
        self.assertEqual(linked, EXPECTED_GITHUB)
        self.assertEqual(len(linked.values()), len(set(value.lower() for value in linked.values())))
        for github in linked.values():
            self.assertRegex(github, re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run the registry test and verify the expected failure**

Run:

```bash
python3 -m unittest tests.test_contributors.ContributorRegistryTests -v
```

Expected: `ERROR` with `FileNotFoundError` for `_data/contributors.json`. The failure proves that the test is exercising the missing production registry.

- [ ] **Step 3: Create the minimal reviewed registry**

Create `_data/contributors.json` with exactly this content:

```json
[
  {
    "name": "Conan Xu",
    "github": "ConanXu-math",
    "initial": "CX",
    "evidence": ["https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "Dong Yuan",
    "github": "dyuan311",
    "initial": "DY",
    "evidence": ["https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "hyyh28",
    "github": "hyyh28",
    "initial": "H",
    "evidence": ["https://github.com/VeryMath/verymath.github.io/commits/main/?author=hyyh28"]
  },
  {
    "name": "IsRivulet",
    "github": "IsRivulet",
    "initial": "I",
    "evidence": ["https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "Miao Dong",
    "github": null,
    "initial": "MD",
    "evidence": ["https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "njustar2002",
    "github": null,
    "initial": "N",
    "evidence": ["https://github.com/VeryMath/AI4Math-MathTool/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "Quan Sun",
    "github": null,
    "initial": "QS",
    "evidence": ["https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "rain37233",
    "github": null,
    "initial": "R",
    "evidence": ["https://github.com/VeryMath/AI4Math-Lean-Agents/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "ricercar77",
    "github": "ricercar77",
    "initial": "R",
    "evidence": [
      "https://github.com/VeryMath/AI4Math-Optimization/blob/main/CONTRIBUTORS.md",
      "https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md"
    ]
  },
  {
    "name": "tanghaoru",
    "github": "tanghaoru",
    "initial": "T",
    "evidence": ["https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "Xiaowen Zhang",
    "github": null,
    "initial": "XZ",
    "evidence": ["https://github.com/VeryMath/AI4Math-Auto-Research/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "Yihong Wei",
    "github": "Imccark",
    "initial": "YW",
    "evidence": ["https://github.com/VeryMath/AI4Math-Sagemath-skill/commits/main/?author=Imccark"]
  },
  {
    "name": "Yunfeng Lu",
    "github": null,
    "initial": "YL",
    "evidence": ["https://github.com/VeryMath/AI4Math-MathTool/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "Zhuojie Tu",
    "github": null,
    "initial": "ZT",
    "evidence": ["https://github.com/VeryMath/AI4Math-Paper-Reading/blob/main/CONTRIBUTORS.md"]
  },
  {
    "name": "李爽夕",
    "github": null,
    "initial": "李",
    "evidence": [
      "https://github.com/VeryMath/AI4Math-Optimization/blob/main/CONTRIBUTORS.md",
      "https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md"
    ]
  },
  {
    "name": "蒋博先",
    "github": null,
    "initial": "蒋",
    "evidence": ["https://github.com/VeryMath/AI4Math-Computational-Mathematics/blob/main/CONTRIBUTORS.md"]
  }
]
```

- [ ] **Step 4: Run the registry tests and verify green**

Run:

```bash
python3 -m unittest tests.test_contributors.ContributorRegistryTests -v
```

Expected: three tests pass, with no warnings or errors.

- [ ] **Step 5: Commit the registry and its contract**

```bash
git add _data/contributors.json tests/test_contributors.py
git commit -m "data: register VeryMath contributors"
```

---

### Task 2: Render and Style the Homepage Contributor Grid

**Files:**
- Modify: `index.md:296-306`
- Modify: `index.md:583-715`
- Modify: `index.md:1151-1162`
- Modify: `tests/test_contributors.py`
- Create: `tests/render_homepage.rb`
- Create: `tests/verify_contributors_browser.cjs`
- Create: `tests/README.md`

**Interfaces:**
- Consumes: `site.data.contributors`, preserving the record order and treating a non-null `github` as the only permission to create a profile link and avatar request.
- Produces: `section[aria-labelledby="vm-contributors-title"]` containing 16 `.vm-contributor-card` elements, seven linked cards and nine static cards.

- [ ] **Step 1: Add the strict real-Liquid preview renderer**

Create `tests/render_homepage.rb`:

```ruby
# frozen_string_literal: true

require "json"
require "liquid"

root = File.expand_path("..", __dir__)
contributors = JSON.parse(File.read(File.join(root, "_data", "contributors.json")))
index_source = File.read(File.join(root, "index.md"), encoding: "UTF-8")
index_body = index_source.sub(/\A---\s*\n.*?\n---\s*\n/m, "")
layout_source = File.read(File.join(root, "_layouts", "default.html"), encoding: "UTF-8")

site = {
  "title" => "VeryMath",
  "description" => "AI for mathematical research. Reusable, verifiable, and collaborative workflows for open mathematics.",
  "data" => { "contributors" => contributors }
}
page = { "title" => "VeryMath" }
assigns = { "site" => site, "page" => page }

content = Liquid::Template.parse(index_body, error_mode: :strict).render!(
  assigns,
  strict_variables: true,
  strict_filters: true
)
html = Liquid::Template.parse(layout_source, error_mode: :strict).render!(
  assigns.merge("content" => content),
  strict_variables: true,
  strict_filters: true
)

$stdout.write(html)
```

- [ ] **Step 2: Add rendered-page behavior tests**

Add these imports to `tests/test_contributors.py`:

```python
import subprocess
from html.parser import HTMLParser
```

Add these helpers after `EXPECTED_GITHUB`:

```python
VOID_ELEMENTS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class Node:
    def __init__(self, tag="document", attrs=None, parent=None):
        self.tag = tag
        self.attrs = dict(attrs or [])
        self.parent = parent
        self.children = []

    @property
    def classes(self):
        return set(self.attrs.get("class", "").split())

    def text(self):
        return " ".join(
            part.strip()
            for child in self.children
            for part in ([child] if isinstance(child, str) else [child.text()])
            if part.strip()
        )


class DOMParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.root = Node()
        self.stack = [self.root]

    def handle_starttag(self, tag, attrs):
        node = Node(tag, attrs, self.stack[-1])
        self.stack[-1].children.append(node)
        if tag not in VOID_ELEMENTS:
            self.stack.append(node)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID_ELEMENTS:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        for index in range(len(self.stack) - 1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]
                return

    def handle_data(self, data):
        self.stack[-1].children.append(data)


def descendants(node):
    for child in node.children:
        if isinstance(child, Node):
            yield child
            yield from descendants(child)


def find_one(node, predicate):
    matches = [candidate for candidate in descendants(node) if predicate(candidate)]
    if len(matches) != 1:
        raise AssertionError(f"expected one matching node, found {len(matches)}")
    return matches[0]
```

Add this test class before the `if __name__ == "__main__"` block:

```python
class ContributorHomepageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        result = subprocess.run(
            ["ruby", str(ROOT / "tests" / "render_homepage.rb")],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        cls.html = result.stdout
        parser = DOMParser()
        parser.feed(cls.html)
        cls.document = parser.root
        cls.section = find_one(
            cls.document,
            lambda node: node.tag == "section" and node.attrs.get("aria-labelledby") == "vm-contributors-title",
        )
        cls.cards = [node for node in descendants(cls.section) if "vm-contributor-card" in node.classes]

    def test_contributors_are_the_final_homepage_section(self):
        homepage_sections = [
            node for node in self.section.parent.children
            if isinstance(node, Node) and node.tag == "section"
        ]
        self.assertIs(homepage_sections[-1], self.section)
        title = find_one(self.section, lambda node: node.attrs.get("id") == "vm-contributors-title")
        english = find_one(title, lambda node: "lang-en" in node.classes)
        chinese = find_one(title, lambda node: "lang-zh" in node.classes)
        self.assertEqual(english.text(), "Contributors")
        self.assertEqual(chinese.text(), "贡献者")

    def test_every_registry_entry_renders_once_without_ranking(self):
        self.assertEqual(len(self.cards), 16)
        rendered_names = [
            find_one(card, lambda node: "vm-contributor-name" in node.classes).text()
            for card in self.cards
        ]
        self.assertEqual(rendered_names, EXPECTED_NAMES)
        self.assertNotIn("contributions", self.section.text().lower())
        self.assertNotIn("ranking", self.section.text().lower())

    def test_only_confirmed_accounts_render_links_and_lazy_avatars(self):
        records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))
        cards_by_name = {
            find_one(card, lambda node: "vm-contributor-name" in node.classes).text(): card
            for card in self.cards
        }
        for record in records:
            with self.subTest(name=record["name"]):
                card = cards_by_name[record["name"]]
                images = [node for node in descendants(card) if node.tag == "img"]
                if record["github"]:
                    self.assertEqual(card.tag, "a")
                    self.assertEqual(card.attrs.get("href"), f"https://github.com/{record['github']}")
                    self.assertEqual(len(images), 1)
                    self.assertEqual(images[0].attrs.get("src"), f"https://github.com/{record['github']}.png?size=160")
                    self.assertEqual(images[0].attrs.get("loading"), "lazy")
                    handle = find_one(card, lambda node: "vm-contributor-handle" in node.classes)
                    self.assertEqual(handle.text(), f"@{record['github']}")
                else:
                    self.assertEqual(card.tag, "div")
                    self.assertNotIn("href", card.attrs)
                    self.assertEqual(images, [])

    def test_page_adds_no_contributor_api_dependency(self):
        self.assertNotIn("api.github.com/orgs/VeryMath", self.html)
        self.assertNotRegex(self.html, r"api\.github\.com/repos/VeryMath/[^\"']+/contributors")
```

- [ ] **Step 3: Add the browser behavior harness before the component**

Create `tests/verify_contributors_browser.cjs` with a Node HTTP server that serves the rendered page and repository assets, launches Chrome with `chromium.launch({ channel: "chrome", headless: true })`, and checks both `{ width: 1366, height: 900 }` and `{ width: 390, height: 844 }`.

The script must perform these literal assertions and exit nonzero on failure:

```javascript
const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
const os = require("node:os");
const path = require("node:path");
const { execFileSync } = require("node:child_process");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const html = execFileSync("ruby", [path.join(root, "tests", "render_homepage.rb")], {
  cwd: root,
  encoding: "utf8",
});

function contentType(filePath) {
  if (filePath.endsWith(".png")) return "image/png";
  if (filePath.endsWith(".gif")) return "image/gif";
  if (filePath.endsWith(".jpeg") || filePath.endsWith(".jpg")) return "image/jpeg";
  return "application/octet-stream";
}

const server = http.createServer((request, response) => {
  if (request.url === "/" || request.url === "/index.html") {
    response.writeHead(200, { "Content-Type": "text/html; charset=utf-8" });
    response.end(html);
    return;
  }
  if (request.url.startsWith("/assets/")) {
    const assetPath = path.resolve(root, `.${request.url}`);
    const assetRoot = path.resolve(root, "assets") + path.sep;
    if (assetPath.startsWith(assetRoot) && fs.existsSync(assetPath)) {
      response.writeHead(200, { "Content-Type": contentType(assetPath) });
      fs.createReadStream(assetPath).pipe(response);
      return;
    }
  }
  response.writeHead(404);
  response.end("Not found");
});

async function listen() {
  await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
  return `http://127.0.0.1:${server.address().port}/`;
}

async function inspect(browser, url, viewport, screenshotName) {
  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  await page.route("https://github.com/ConanXu-math.png?size=160", (route) => route.abort());
  await page.goto(url, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".vm-contributor-card");
  await page.waitForTimeout(300);

  const report = await page.evaluate(() => {
    const section = document.querySelector('[aria-labelledby="vm-contributors-title"]');
    const join = [...document.querySelectorAll("section")].find((item) => item.textContent.includes("Join the Ecosystem"));
    const cards = [...section.querySelectorAll(".vm-contributor-card")];
    const linked = cards.filter((card) => card.matches("a[href]"));
    const staticCards = cards.filter((card) => card.matches("div.vm-contributor-card"));
    const lefts = [...new Set(cards.map((card) => Math.round(card.getBoundingClientRect().left)))];
    const failedImage = section.querySelector('img[src*="ConanXu-math.png"]');
    const failedInitial = failedImage.parentElement.querySelector(".vm-contributor-initial");
    return {
      cardCount: cards.length,
      linkedCount: linked.length,
      staticCount: staticCards.length,
      columns: lefts.length,
      followsJoin: section.getBoundingClientRect().top > join.getBoundingClientRect().top,
      overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
      englishVisible: getComputedStyle(section.querySelector(".lang-en")).display !== "none",
      chineseVisible: getComputedStyle(section.querySelector(".lang-zh")).display !== "none",
      failedImageHidden: failedImage.hidden,
      failedInitialVisible: getComputedStyle(failedInitial).display !== "none",
      cardsHaveSize: cards.every((card) => {
        const rect = card.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
      }),
    };
  });

  assert.equal(report.cardCount, 16);
  assert.equal(report.linkedCount, 7);
  assert.equal(report.staticCount, 9);
  assert.equal(report.followsJoin, true);
  assert.equal(report.overflowX, false);
  assert.equal(report.englishVisible, true);
  assert.equal(report.chineseVisible, false);
  assert.equal(report.failedImageHidden, true);
  assert.equal(report.failedInitialVisible, true);
  assert.equal(report.cardsHaveSize, true);
  assert.ok(report.columns >= (viewport.width >= 760 ? 4 : 2));

  await page.click('[data-set-lang="zh"]');
  const chinese = await page.evaluate(() => ({
    title: document.querySelector("#vm-contributors-title").innerText.trim(),
    lang: document.documentElement.lang,
    overflowX: document.documentElement.scrollWidth > document.documentElement.clientWidth + 1,
  }));
  assert.equal(chinese.title, "贡献者");
  assert.equal(chinese.lang, "zh-CN");
  assert.equal(chinese.overflowX, false);

  const screenshotDir = process.env.VERYMATH_SCREENSHOT_DIR;
  if (screenshotDir) {
    fs.mkdirSync(screenshotDir, { recursive: true });
    await page.locator('[aria-labelledby="vm-contributors-title"]').screenshot({
      path: path.join(screenshotDir, screenshotName),
    });
  }
  await page.close();
  return { viewport, ...report, chinese };
}

(async () => {
  const url = await listen();
  const browser = await chromium.launch({ channel: "chrome", headless: true });
  try {
    const desktop = await inspect(browser, url, { width: 1366, height: 900 }, "contributors-desktop.png");
    const mobile = await inspect(browser, url, { width: 390, height: 844 }, "contributors-mobile.png");
    process.stdout.write(`${JSON.stringify({ desktop, mobile }, null, 2)}\n`);
  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
})().catch((error) => {
  console.error(error);
  server.close(() => process.exit(1));
});
```

- [ ] **Step 4: Run the new tests and verify the component is missing**

Install the renderer dependency once if `ruby -rliquid -e 'puts Liquid::VERSION'` fails:

```bash
gem install liquid -v 4.0.4 --user-install --no-document
```

Run:

```bash
python3 -m unittest tests.test_contributors.ContributorHomepageTests -v
```

Expected: `ERROR` stating that no `section[aria-labelledby="vm-contributors-title"]` exists. This is the RED state for the homepage behavior.

- [ ] **Step 5: Add the minimal contributor component to `index.md`**

Add a `.vm-contributor-grid` using `repeat(auto-fill, minmax(150px, 1fr))`. Add `.vm-contributor-card`, `.vm-contributor-avatar`, `.vm-contributor-initial`, `.vm-contributor-avatar img`, `.vm-contributor-name`, and `.vm-contributor-handle` styles that reuse `--vm-line`, `--vm-ink`, `--vm-muted`, `--vm-bg`, and `--vm-blue`. Linked cards receive hover and `:focus-visible` states; static cards do not animate.

Add a separate `@media (max-width: 480px)` block that sets the grid to two equal columns and reduces card padding. Add `@media (max-width: 340px)` with one column.

Immediately after the closing tag for `Join the Ecosystem`, add this Liquid-backed section:

```html
  <section class="vm-section" aria-labelledby="vm-contributors-title">
    <h2 id="vm-contributors-title"><span class="lang-en">Contributors</span><span class="lang-zh">贡献者</span></h2>
    <p class="vm-lead">
      <span class="lang-en">We thank everyone who has contributed tools, workflows, and research infrastructure to VeryMath.</span>
      <span class="lang-zh">感谢所有为 VeryMath 的工具、工作流与科研基础设施作出贡献的参与者。</span>
    </p>
    <div class="vm-contributor-grid">
      {% for contributor in site.data.contributors %}
        {% if contributor.github %}
          <a class="vm-contributor-card" href="https://github.com/{{ contributor.github | escape }}">
            <span class="vm-contributor-avatar" aria-hidden="true">
              <span class="vm-contributor-initial">{{ contributor.initial | escape }}</span>
              <img src="https://github.com/{{ contributor.github | escape }}.png?size=160" alt="" width="64" height="64" loading="lazy" decoding="async" onerror="this.hidden = true">
            </span>
            <span class="vm-contributor-name">{{ contributor.name | escape }}</span>
            <span class="vm-contributor-handle">@{{ contributor.github | escape }}</span>
          </a>
        {% else %}
          <div class="vm-contributor-card vm-contributor-card-static">
            <span class="vm-contributor-avatar" aria-hidden="true">
              <span class="vm-contributor-initial">{{ contributor.initial | escape }}</span>
            </span>
            <span class="vm-contributor-name">{{ contributor.name | escape }}</span>
          </div>
        {% endif %}
      {% endfor %}
    </div>
  </section>
```

Use these exact behavioral CSS properties while matching the existing card appearance:

```css
  .vm-contributor-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
    gap: 12px;
  }

  .vm-contributor-card {
    min-width: 0;
    min-height: 154px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 18px 12px 16px;
    border: 1px solid var(--vm-line);
    border-radius: 8px;
    color: var(--vm-ink);
    text-align: center;
    text-decoration: none;
    background: #fff;
  }

  a.vm-contributor-card {
    transition: border-color 120ms ease, box-shadow 120ms ease, transform 120ms ease;
  }

  a.vm-contributor-card:hover {
    border-color: rgba(11, 79, 156, 0.4);
    color: var(--vm-ink);
    box-shadow: 0 10px 24px rgba(22, 33, 61, 0.1);
    transform: translateY(-2px);
  }

  a.vm-contributor-card:focus-visible {
    outline: 3px solid rgba(9, 105, 218, 0.28);
    outline-offset: 2px;
  }

  .vm-contributor-avatar {
    position: relative;
    width: 64px;
    height: 64px;
    display: grid;
    flex: 0 0 64px;
    place-items: center;
    overflow: hidden;
    border: 1px solid rgba(11, 79, 156, 0.16);
    border-radius: 50%;
    color: var(--vm-blue);
    font-size: 17px;
    font-weight: 800;
    background: var(--vm-bg);
  }

  .vm-contributor-avatar img {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    background: #fff;
  }

  .vm-contributor-name {
    max-width: 100%;
    font-weight: 800;
    line-height: 1.35;
    overflow-wrap: anywhere;
  }

  .vm-contributor-handle {
    max-width: 100%;
    color: var(--vm-muted);
    font-size: 13px;
    line-height: 1.3;
    overflow-wrap: anywhere;
  }

  @media (max-width: 480px) {
    .vm-contributor-grid {
      grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .vm-contributor-card {
      min-height: 144px;
      padding: 16px 10px 14px;
    }
  }

  @media (max-width: 340px) {
    .vm-contributor-grid {
      grid-template-columns: 1fr;
    }
  }
```

- [ ] **Step 6: Run the rendered-page tests and verify green**

Run:

```bash
python3 -m unittest discover -s tests -v
```

Expected: all registry and rendered-page tests pass. The rendered page contains 16 ordered cards, seven GitHub links, nine static credits, no contributor API call, and both language labels.

- [ ] **Step 7: Document and execute browser verification**

Create `tests/README.md`:

````markdown
# Local validation

Install the pinned Liquid renderer and run the deterministic tests:

```bash
gem install liquid -v 4.0.4 --user-install --no-document
python3 -m unittest discover -s tests -v
```

Run the browser checks with a temporary Playwright install and the local Chrome channel:

```bash
VM_PLAYWRIGHT_DIR="$(mktemp -d)"
npm install --prefix "$VM_PLAYWRIGHT_DIR" playwright@1.62.1
VM_SCREENSHOT_DIR="$(mktemp -d)"
NODE_PATH="$VM_PLAYWRIGHT_DIR/node_modules" VERYMATH_SCREENSHOT_DIR="$VM_SCREENSHOT_DIR" node tests/verify_contributors_browser.cjs
```

The browser command prints the desktop/mobile assertion report and writes two section screenshots to the temporary screenshot directory.
````

Run the documented command. Expected JSON facts at both widths: `cardCount: 16`, `linkedCount: 7`, `staticCount: 9`, `overflowX: false`, `failedImageHidden: true`, and Chinese title `贡献者`. Desktop must report at least four columns and the 390px viewport at least two.

Open both generated PNG files and inspect that names are not clipped, linked and static cards align, initials remain legible, spacing matches the surrounding homepage, and the mobile grid does not crowd the viewport.

- [ ] **Step 8: Re-run the full repository checks**

Run:

```bash
python3 -m unittest discover -s tests -v
git diff --check
git status --short
```

Expected: every test passes; `git diff --check` produces no output; status lists only the intended contributor files plus the two pre-existing unstaged `.DS_Store` modifications.

- [ ] **Step 9: Commit the rendered component and verification harness**

```bash
git add index.md tests/test_contributors.py tests/render_homepage.rb tests/verify_contributors_browser.cjs tests/README.md
git commit -m "feat: credit contributors on homepage"
```

---

### Task 3: Final Requirement and Regression Audit

**Files:**
- Verify only; no production file is expected to change.

**Interfaces:**
- Consumes: The two implementation commits and the approved design specification.
- Produces: Fresh evidence that the implementation satisfies attribution, static rendering, responsive layout, language, and workspace-preservation requirements.

- [ ] **Step 1: Compare the final diff against the approved scope**

Run:

```bash
git diff 5123369..HEAD -- _data/contributors.json index.md tests
git diff 5123369..HEAD --stat
```

Confirm that no repository cards, course-release content, Star control behavior, layout file, or existing assets changed.

- [ ] **Step 2: Run fresh deterministic and browser verification**

Run the complete commands from `tests/README.md` again. Read every test result and the full browser JSON; do not rely on an earlier run.

- [ ] **Step 3: Verify unrelated workspace changes remain untouched**

Run:

```bash
git status --short --branch
git diff -- .DS_Store assets/.DS_Store
```

Confirm `.DS_Store` and `assets/.DS_Store` remain unstaged user-owned modifications and are absent from both feature commits.

- [ ] **Step 4: Report the exact delivery boundary**

Report the created data registry, homepage component, automated checks, browser widths, and commit hashes. State explicitly that the branch has not been pushed and the live website has not been published.
