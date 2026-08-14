import subprocess
import unittest

from test_contributors import DOMParser, ROOT, descendants, find_one


EXPECTED_AUGUST_UPDATES = [
    {
        "kicker": "DeepSeek Harness × VeryMath",
        "category_en": "Skill Support",
        "category_zh": "技能支持",
        "links": {
            "https://github.com/VeryMath",
            "https://github.com/deepseek-ai/deepseek-harness",
        },
    },
    {
        "kicker": "Danus × OpenCode × DeepSeek Harness",
        "category_en": "Runtime Support",
        "category_zh": "运行支持",
        "links": {
            "https://github.com/VeryMath/AI4Math-Auto-Research/tree/main/skills/danus-helper",
            "https://github.com/VeryMath/AI4Math-Auto-Research/tree/main/skills/danus-helper-dsh",
        },
    },
    {
        "kicker": "Rethlas & Archon × OpenCode",
        "category_en": "Platform Adaptation",
        "category_zh": "平台适配",
        "links": {
            "https://github.com/VeryMath/AI4Math-Auto-Research/tree/main/skills/rethlas-helper",
            "https://github.com/VeryMath/AI4Math-Auto-Research/tree/main/skills/archon-helper",
        },
    },
]


class HomepageUpdateTests(unittest.TestCase):
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

        parser = DOMParser()
        parser.feed(cls.render_result.stdout)
        cls.document = parser.root
        cls.section = find_one(
            cls.document,
            lambda node: node.tag == "section"
            and node.attrs.get("aria-labelledby") == "vm-news-title",
        )
        cls.announcements = [
            node
            for node in descendants(cls.section)
            if "vm-announcement" in node.classes
        ]

    def test_star_count_uses_a_non_stale_loading_fallback(self):
        star_count = find_one(
            self.document,
            lambda node: node.attrs.get("id") == "vm-star-count",
        )
        self.assertEqual(star_count.text(), "—")
        self.assertEqual(star_count.attrs.get("aria-label"), "Star count loading")

    def test_august_updates_are_separate_and_newest_first(self):
        self.assertEqual(self.render_result.returncode, 0, self.render_result.stderr)
        self.assertGreaterEqual(len(self.announcements), 5)

        for announcement, expected in zip(
            self.announcements[:3], EXPECTED_AUGUST_UPDATES
        ):
            with self.subTest(kicker=expected["kicker"]):
                date = find_one(
                    announcement,
                    lambda node: "vm-announcement-date" in node.classes,
                )
                category = find_one(date, lambda node: node.tag == "strong")
                category_en = find_one(
                    category, lambda node: "lang-en" in node.classes
                )
                category_zh = find_one(
                    category, lambda node: "lang-zh" in node.classes
                )
                kicker = find_one(
                    announcement,
                    lambda node: "vm-announcement-kicker" in node.classes,
                )
                title = find_one(
                    announcement,
                    lambda node: "vm-announcement-title" in node.classes,
                )
                links = {
                    node.attrs["href"]
                    for node in descendants(announcement)
                    if node.tag == "a" and "href" in node.attrs
                }

                self.assertIn("2026.08", date.text())
                self.assertEqual(category_en.text(), expected["category_en"])
                self.assertEqual(category_zh.text(), expected["category_zh"])
                self.assertEqual(kicker.text(), expected["kicker"])
                self.assertEqual(
                    len([node for node in descendants(title) if "lang-en" in node.classes]),
                    1,
                )
                self.assertEqual(
                    len([node for node in descendants(title) if "lang-zh" in node.classes]),
                    1,
                )
                self.assertTrue(expected["links"].issubset(links))


if __name__ == "__main__":
    unittest.main()
