import json
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "_config.yml"


class GitHubPagesConfigurationTests(unittest.TestCase):
    def test_internal_project_docs_are_excluded_from_the_published_site(self):
        script = (
            'require "json"; require "yaml"; '
            'puts JSON.generate(YAML.load_file(ARGV.fetch(0)) || {})'
        )
        config = json.loads(
            subprocess.check_output(
                ["ruby", "-e", script, str(CONFIG_PATH)],
                cwd=ROOT,
                text=True,
            )
        )
        excluded_paths = {
            str(path).strip("/") for path in config.get("exclude", [])
        }

        self.assertIn(
            "docs",
            excluded_paths,
            "Jekyll must not parse internal plans containing Liquid examples",
        )


if __name__ == "__main__":
    unittest.main()
