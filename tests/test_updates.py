import subprocess
import unittest

from test_contributors import DOMParser, ROOT, descendants, find_one


EXPECTED_NEWEST_UPDATES = [
    {
        "date": "2026.09",
        "kicker": "EMNLP 2026 Findings · OptSkills × VeryMath",
        "category_en": "Skill Integration",
        "category_zh": "Skill 接入",
        "links": {
            "https://github.com/VeryMath/AI4Math-Optimization/tree/main/skills/optskills",
            "https://arxiv.org/pdf/2605.29829",
        },
    },
    {
        "date": "2026.08",
        "kicker": "DeepSeek Harness × VeryMath",
        "category_en": "Skill Support",
        "category_zh": "技能支持",
        "links": {
            "https://github.com/VeryMath",
            "https://github.com/deepseek-ai/deepseek-harness",
        },
    },
    {
        "date": "2026.08",
        "kicker": "Danus × OpenCode × DeepSeek Harness",
        "category_en": "Runtime Support",
        "category_zh": "运行支持",
        "links": {
            "https://github.com/VeryMath/AI4Math-Auto-Research/tree/main/skills/danus-helper",
            "https://github.com/VeryMath/AI4Math-Auto-Research/tree/main/skills/danus-helper-dsh",
        },
    },
    {
        "date": "2026.08",
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

    def test_updates_are_separate_and_newest_first(self):
        self.assertEqual(self.render_result.returncode, 0, self.render_result.stderr)
        self.assertGreaterEqual(len(self.announcements), 6)

        for announcement, expected in zip(
            self.announcements[:4], EXPECTED_NEWEST_UPDATES
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

                self.assertIn(expected["date"], date.text())
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

    def test_optskills_copy_names_the_paper_source_without_validation_claims(self):
        optskills = self.announcements[0]
        text = optskills.text()
        kicker = find_one(
            optskills,
            lambda node: "vm-announcement-kicker" in node.classes,
        )

        self.assertTrue(kicker.text().startswith("EMNLP 2026 Findings"))
        self.assertNotIn("arXiv", kicker.text())
        self.assertIn("EMNLP 2026 Findings", text)
        self.assertIn(
            "OptSkills 现已加入 AI4Math-Optimization，内含 103 个优化问题原型。",
            text,
        )
        self.assertNotIn("Representative checks", text)
        self.assertNotIn("代表性验证", text)

    def test_optskills_footer_has_only_skill_and_paper_links(self):
        optskills = self.announcements[0]
        skill_link = find_one(
            optskills,
            lambda node: node.tag == "a"
            and node.attrs.get("href")
            == "https://github.com/VeryMath/AI4Math-Optimization/tree/main/skills/optskills",
        )
        links = {
            node.attrs["href"]
            for node in descendants(optskills)
            if node.tag == "a" and "href" in node.attrs
        }

        self.assertEqual(links, EXPECTED_NEWEST_UPDATES[0]["links"])
        self.assertEqual(
            find_one(skill_link, lambda node: "lang-en" in node.classes).text(),
            "OptSkills",
        )
        self.assertEqual(
            find_one(skill_link, lambda node: "lang-zh" in node.classes).text(),
            "OptSkills",
        )

    def test_optimization_repository_count_includes_optskills(self):
        optimization_card = find_one(
            self.document,
            lambda node: "vm-project" in node.classes
            and any(
                child.tag == "h3" and child.text() == "AI4Math-Optimization"
                for child in descendants(node)
            ),
        )

        self.assertIn("8 skills", optimization_card.text())
        self.assertIn("8 个技能", optimization_card.text())


if __name__ == "__main__":
    unittest.main()
