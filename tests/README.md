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
