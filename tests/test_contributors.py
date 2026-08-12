import json
import re
import subprocess
import unittest
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRIBUTORS_PATH = ROOT / "_data" / "contributors.json"
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
EXPECTED_NAMES = [item[0] for item in EXPECTED_CONTRIBUTORS]
EXPECTED_NAMES_ZH = [item[1] for item in EXPECTED_CONTRIBUTORS]
EXPECTED_GITHUB = {item[0]: item[3] for item in EXPECTED_CONTRIBUTORS if item[3]}
TEAM_NAMES_ZH = {
    "李爽夕",
    "林依鹏",
    "凌晨",
    "汤皓如",
    "涂卓杰",
    "王诺千",
    "邢梦圆",
    "陈亚玲",
    "蒋博先",
    "黎汝婧",
    "尉毅宏",
    "徐柯楠",
    "袁东",
    "张司雨",
}
TEAM_SOURCE = "team-introduction-2026-06-30"
VOID_ELEMENTS = {
    "area",
    "base",
    "br",
    "col",
    "embed",
    "hr",
    "img",
    "input",
    "link",
    "meta",
    "param",
    "source",
    "track",
    "wbr",
}


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


def localized_text(node, field_class, language):
    field = find_one(node, lambda candidate: field_class in candidate.classes)
    localized = find_one(field, lambda candidate: f"lang-{language}" in candidate.classes)
    return localized.text()


class ContributorRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))

    def test_registry_matches_the_approved_order(self):
        actual = [
            (
                record.get("name_en"),
                record.get("name_zh"),
                record.get("role"),
                record.get("github"),
            )
            for record in self.records
        ]
        self.assertEqual(actual, EXPECTED_CONTRIBUTORS)

    def test_records_have_complete_bilingual_schema_and_sources(self):
        self.assertEqual(len(self.records), 21)
        self.assertEqual(len({record.get("name_en") for record in self.records}), 21)
        self.assertEqual(len({record.get("name_zh") for record in self.records}), 21)
        for record in self.records:
            with self.subTest(name=record.get("name_en") or record.get("name")):
                self.assertEqual(
                    set(record),
                    {
                        "name_en",
                        "name_zh",
                        "github",
                        "initial_en",
                        "initial_zh",
                        "role",
                        "evidence",
                    },
                )
                self.assertIsInstance(record["name_en"], str)
                self.assertTrue(record["name_en"].strip())
                self.assertIsInstance(record["name_zh"], str)
                self.assertTrue(record["name_zh"].strip())
                self.assertRegex(record["initial_en"], r"^[A-Z]{1,3}$")
                self.assertRegex(record["initial_zh"], r"^.$")
                self.assertIn(record["role"], {"advisor", "member"})
                self.assertIsInstance(record["evidence"], list)
                self.assertTrue(record["evidence"])
                self.assertTrue(
                    all(
                        source == TEAM_SOURCE or source.startswith("https://github.com/")
                        for source in record["evidence"]
                    )
                )

    def test_advisor_is_unique_and_first(self):
        advisors = [record for record in self.records if record.get("role") == "advisor"]
        self.assertEqual([record.get("name_zh") for record in advisors], ["王祥丰"])
        self.assertEqual(self.records[0].get("name_zh"), "王祥丰")
        self.assertTrue(all(record.get("role") == "member" for record in self.records[1:]))

    def test_team_introduction_members_are_all_present(self):
        self.assertTrue(TEAM_NAMES_ZH.issubset({record.get("name_zh") for record in self.records}))
        team_sourced = {
            record.get("name_zh") for record in self.records if TEAM_SOURCE in record["evidence"]
        }
        self.assertEqual(team_sourced, TEAM_NAMES_ZH)

    def test_only_confirmed_github_accounts_are_linked(self):
        linked = {
            record.get("name_en"): record["github"]
            for record in self.records
            if record["github"]
        }
        self.assertEqual(linked, EXPECTED_GITHUB)
        self.assertEqual(len(linked), 11)
        self.assertEqual(len(linked.values()), len({value.lower() for value in linked.values()}))
        for github in linked.values():
            self.assertRegex(github, re.compile(r"^[A-Za-z0-9](?:[A-Za-z0-9-]{0,37}[A-Za-z0-9])?$"))


class ContributorHomepageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.render_result = subprocess.run(
            ["ruby", str(ROOT / "tests" / "render_homepage.rb")],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        if cls.render_result.returncode != 0:
            return
        cls.html = cls.render_result.stdout
        parser = DOMParser()
        parser.feed(cls.html)
        cls.document = parser.root
        cls.section = find_one(
            cls.document,
            lambda node: node.tag == "section" and node.attrs.get("aria-labelledby") == "vm-contributors-title",
        )
        cls.cards = [node for node in descendants(cls.section) if "vm-contributor-card" in node.classes]

    def test_homepage_renders_with_strict_liquid(self):
        self.assertEqual(self.render_result.returncode, 0, self.render_result.stderr)

    def test_contributors_are_the_final_homepage_section(self):
        homepage_sections = [
            node
            for node in self.section.parent.children
            if isinstance(node, Node) and node.tag == "section"
        ]
        self.assertIs(homepage_sections[-1], self.section)
        title = find_one(self.section, lambda node: node.attrs.get("id") == "vm-contributors-title")
        english = find_one(title, lambda node: "lang-en" in node.classes)
        chinese = find_one(title, lambda node: "lang-zh" in node.classes)
        self.assertEqual(english.text(), "Contributors")
        self.assertEqual(chinese.text(), "贡献者")

    def test_every_registry_entry_renders_once_without_ranking(self):
        self.assertEqual(len(self.cards), 21)
        self.assertEqual(
            [localized_text(card, "vm-contributor-name", "en") for card in self.cards],
            EXPECTED_NAMES,
        )
        self.assertEqual(
            [localized_text(card, "vm-contributor-name", "zh") for card in self.cards],
            EXPECTED_NAMES_ZH,
        )
        self.assertEqual(localized_text(self.cards[0], "vm-contributor-name", "zh"), "王祥丰")
        self.assertNotIn("contributions", self.section.text().lower())
        self.assertNotIn("ranking", self.section.text().lower())

    def test_contributor_copy_includes_teamwork_and_guidance(self):
        lead = find_one(self.section, lambda node: "vm-lead" in node.classes)
        english = find_one(lead, lambda node: "lang-en" in node.classes)
        chinese = find_one(lead, lambda node: "lang-zh" in node.classes)
        self.assertEqual(
            english.text(),
            "We thank everyone who contributes tools, workflows, research infrastructure, "
            "teamwork, and guidance to VeryMath.",
        )
        self.assertEqual(
            chinese.text(),
            "感谢所有为 VeryMath 的工具、工作流、科研基础设施、团队协作与指导支持作出贡献的参与者。",
        )

    def test_fallback_initials_follow_the_active_language(self):
        records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))
        for card, record in zip(self.cards, records):
            with self.subTest(name=record["name_en"]):
                self.assertEqual(
                    localized_text(card, "vm-contributor-initial", "en"), record["initial_en"]
                )
                self.assertEqual(
                    localized_text(card, "vm-contributor-initial", "zh"), record["initial_zh"]
                )

    def test_only_confirmed_accounts_render_links_and_lazy_avatars(self):
        records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))
        cards_by_name = {
            localized_text(card, "vm-contributor-name", "en"): card
            for card in self.cards
        }
        for record in records:
            with self.subTest(name=record["name_en"]):
                card = cards_by_name[record["name_en"]]
                images = [node for node in descendants(card) if node.tag == "img"]
                handles = [
                    node for node in descendants(card) if "vm-contributor-handle" in node.classes
                ]
                if record["github"]:
                    self.assertEqual(card.tag, "a")
                    self.assertEqual(card.attrs.get("href"), f"https://github.com/{record['github']}")
                    self.assertEqual(len(images), 1)
                    self.assertEqual(
                        images[0].attrs.get("src"),
                        f"https://github.com/{record['github']}.png?size=160",
                    )
                    self.assertEqual(images[0].attrs.get("loading"), "lazy")
                    self.assertEqual([handle.text() for handle in handles], [f"@{record['github']}"])
                else:
                    self.assertEqual(card.tag, "div")
                    self.assertNotIn("href", card.attrs)
                    self.assertEqual(images, [])
                    self.assertEqual(handles, [])

    def test_page_adds_no_contributor_api_dependency(self):
        self.assertNotIn("api.github.com/orgs/VeryMath", self.html)
        self.assertNotRegex(self.html, r"api\.github\.com/repos/VeryMath/[^\"']+/contributors")


if __name__ == "__main__":
    unittest.main()
