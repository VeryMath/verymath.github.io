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

The browser command verifies the 21-card bilingual order, confirmed/static card counts, language-specific fallback initials, avatar loading and fault handling, and responsive overflow. When `VERYMATH_SCREENSHOT_DIR` is set, it writes English and Chinese contributor-section screenshots for desktop and mobile viewports.
