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
