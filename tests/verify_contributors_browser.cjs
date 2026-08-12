const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
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
  let blockedAvatarRequests = 0;
  let delayedAvatarRequests = 0;
  let releaseDelayedAvatar;
  let markDelayedAvatarRequested;
  const delayedAvatarGate = new Promise((resolve) => {
    releaseDelayedAvatar = resolve;
  });
  const delayedAvatarRequested = new Promise((resolve) => {
    markDelayedAvatarRequested = resolve;
  });
  page.on("request", (request) => {
    if (request.url().includes("ConanXu-math.png")) blockedAvatarRequests += 1;
  });
  await page.route("https://github.com/ConanXu-math.png?size=160", (route) => route.abort());
  await page.route("https://github.com/dyuan311.png?size=160", async (route) => {
    delayedAvatarRequests += 1;
    markDelayedAvatarRequested();
    await delayedAvatarGate;
    await route.fulfill({
      path: path.join(root, "assets", "img", "VeryMathlogo.jpeg"),
      contentType: "image/jpeg",
    });
  });
  await page.goto(url, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".vm-contributor-card");
  const avatarImages = page.locator(".vm-contributor-avatar img");
  for (let index = 0; index < (await avatarImages.count()); index += 1) {
    await avatarImages.nth(index).scrollIntoViewIfNeeded();
  }
  await delayedAvatarRequested;
  const pendingFallback = await page.evaluate(() => {
    const image = document.querySelector('img[src*="dyuan311.png"]');
    const initial = image.parentElement.querySelector(".vm-contributor-initial");
    return {
      imageOpacity: getComputedStyle(image).opacity,
      initialVisible: getComputedStyle(initial).display !== "none",
    };
  });
  releaseDelayedAvatar();
  assert.equal(pendingFallback.imageOpacity, "0");
  assert.equal(pendingFallback.initialVisible, true);
  await page.waitForFunction(() => {
    const images = [...document.querySelectorAll(".vm-contributor-avatar img")];
    return (
      images.length === 7 &&
      images.every(
        (image) =>
          image.hidden ||
          (image.complete && image.naturalWidth > 0 && getComputedStyle(image).opacity === "1"),
      )
    );
  });

  const report = await page.evaluate(() => {
    const section = document.querySelector('[aria-labelledby="vm-contributors-title"]');
    const join = [...document.querySelectorAll("section")].find((item) =>
      item.textContent.includes("Join the Ecosystem"),
    );
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
      loadedAvatarCount: [...section.querySelectorAll(".vm-contributor-avatar img")].filter(
        (image) => !image.hidden && image.complete && image.naturalWidth > 0,
      ).length,
      loadedAvatarsOpaque: [...section.querySelectorAll(".vm-contributor-avatar img")]
        .filter((image) => !image.hidden)
        .every((image) => getComputedStyle(image).opacity === "1"),
      cardsHaveSize: cards.every((card) => {
        const rect = card.getBoundingClientRect();
        return rect.width > 0 && rect.height > 0;
      }),
    };
  });
  report.blockedAvatarRequests = blockedAvatarRequests;
  report.delayedAvatarRequests = delayedAvatarRequests;
  report.pendingFallbackVisible = pendingFallback.initialVisible;

  assert.equal(report.cardCount, 16);
  assert.equal(report.linkedCount, 7);
  assert.equal(report.staticCount, 9);
  assert.equal(report.followsJoin, true);
  assert.equal(report.overflowX, false);
  assert.equal(report.englishVisible, true);
  assert.equal(report.chineseVisible, false);
  assert.equal(report.failedImageHidden, true);
  assert.equal(report.blockedAvatarRequests, 1);
  assert.equal(report.delayedAvatarRequests, 1);
  assert.equal(report.failedInitialVisible, true);
  assert.equal(report.loadedAvatarCount, 6);
  assert.equal(report.loadedAvatarsOpaque, true);
  assert.equal(report.pendingFallbackVisible, true);
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
    const desktop = await inspect(
      browser,
      url,
      { width: 1366, height: 900 },
      "contributors-desktop.png",
    );
    const mobile = await inspect(
      browser,
      url,
      { width: 390, height: 844 },
      "contributors-mobile.png",
    );
    process.stdout.write(`${JSON.stringify({ desktop, mobile }, null, 2)}\n`);
  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
})().catch((error) => {
  console.error(error);
  server.close(() => process.exit(1));
});
