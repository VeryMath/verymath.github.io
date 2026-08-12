import json
import re
import subprocess
import unittest
from html.parser import HTMLParser
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
    "rain37233": "rain37233-del",
    "tanghaoru": "tang0805-em",
    "Yihong Wei": "Imccark",
    "李爽夕": "ricercar77",
    "蒋博先": "Joseph20060208",
}
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


class ContributorRegistryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.records = json.loads(CONTRIBUTORS_PATH.read_text(encoding="utf-8"))

    def test_registry_contains_each_verified_public_identity_once(self):
        names = [record["name"] for record in self.records]
        self.assertEqual(names, EXPECTED_NAMES)
        self.assertEqual(len(names), len(set(names)))

    def test_records_are_renderable_and_have_public_evidence(self):
        self.assertEqual(len(self.records), 15)
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
        self.assertEqual(len(self.cards), 15)
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
                    self.assertEqual(
                        images[0].attrs.get("src"),
                        f"https://github.com/{record['github']}.png?size=160",
                    )
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


if __name__ == "__main__":
    unittest.main()
