const assert = require("node:assert/strict");
const fs = require("node:fs");
const http = require("node:http");
const path = require("node:path");
const { execFileSync } = require("node:child_process");
const { chromium } = require("playwright");

const root = path.resolve(__dirname, "..");
const contributors = JSON.parse(
  fs.readFileSync(path.join(root, "_data", "contributors.json"), "utf8"),
);
const expectedCardCount = contributors.length;
const expectedLinkedCount = contributors.filter((contributor) => contributor.github).length;
const expectedStaticCount = expectedCardCount - expectedLinkedCount;
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

async function inspect(browser, url, viewport) {
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
  await page.waitForFunction(
    (expected) => {
      const images = [...document.querySelectorAll(".vm-contributor-avatar img")];
      return (
        images.length === expected &&
        images.every(
          (image) =>
            image.hidden ||
            (image.complete && image.naturalWidth > 0 && getComputedStyle(image).opacity === "1"),
        )
      );
    },
    expectedLinkedCount,
  );

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

  assert.equal(report.cardCount, expectedCardCount);
  assert.equal(report.linkedCount, expectedLinkedCount);
  assert.equal(report.staticCount, expectedStaticCount);
  assert.equal(report.followsJoin, true);
  assert.equal(report.overflowX, false);
  assert.equal(report.englishVisible, true);
  assert.equal(report.chineseVisible, false);
  assert.equal(report.failedImageHidden, true);
  assert.equal(report.blockedAvatarRequests, 1);
  assert.equal(report.delayedAvatarRequests, 1);
  assert.equal(report.failedInitialVisible, true);
  assert.equal(report.loadedAvatarCount, expectedLinkedCount - 1);
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

  await page.close();
  return { viewport, ...report, chinese };
}

async function captureCleanScreenshot(browser, url, viewport, screenshotName) {
  const screenshotDir = process.env.VERYMATH_SCREENSHOT_DIR;
  if (!screenshotDir) return null;

  const page = await browser.newPage({ viewport, deviceScaleFactor: 1 });
  await page.goto(url, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(".vm-contributor-card");
  const avatarImages = page.locator(".vm-contributor-avatar img");
  for (let index = 0; index < (await avatarImages.count()); index += 1) {
    await avatarImages.nth(index).scrollIntoViewIfNeeded();
  }
  await page.waitForFunction(
    (expected) => {
      const images = [...document.querySelectorAll(".vm-contributor-avatar img")];
      return (
        images.length === expected &&
        images.every(
          (image) =>
            image.hidden ||
            (image.complete && image.naturalWidth > 0 && getComputedStyle(image).opacity === "1"),
        )
      );
    },
    expectedLinkedCount,
  );
  await page.click('[data-set-lang="zh"]');

  const realDongYuanAvatarLoaded = await page.evaluate(() => {
    const image = document.querySelector('img[src*="dyuan311.png"]');
    return Boolean(
      image &&
        !image.hidden &&
        image.complete &&
        image.naturalWidth > 0 &&
        getComputedStyle(image).opacity === "1",
    );
  });
  assert.equal(realDongYuanAvatarLoaded, true);

  fs.mkdirSync(screenshotDir, { recursive: true });
  const screenshotPath = path.join(screenshotDir, screenshotName);
  await page.locator('[aria-labelledby="vm-contributors-title"]').screenshot({
    path: screenshotPath,
  });
  await page.close();
  return { screenshotPath, realDongYuanAvatarLoaded };
}

(async () => {
  const url = await listen();
  const browser = await chromium.launch({ channel: "chrome", headless: true });
  try {
    const desktopViewport = { width: 1366, height: 900 };
    const mobileViewport = { width: 390, height: 844 };
    const desktop = await inspect(browser, url, desktopViewport);
    const mobile = await inspect(browser, url, mobileViewport);
    const desktopScreenshot = await captureCleanScreenshot(
      browser,
      url,
      desktopViewport,
      "contributors-desktop.png",
    );
    const mobileScreenshot = await captureCleanScreenshot(
      browser,
      url,
      mobileViewport,
      "contributors-mobile.png",
    );
    process.stdout.write(
      `${JSON.stringify({ desktop, mobile, desktopScreenshot, mobileScreenshot }, null, 2)}\n`,
    );
  } finally {
    await browser.close();
    await new Promise((resolve) => server.close(resolve));
  }
})().catch((error) => {
  console.error(error);
  server.close(() => process.exit(1));
});
