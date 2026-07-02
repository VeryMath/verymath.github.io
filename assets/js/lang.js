(function () {
  var root = document.documentElement;
  var buttons = document.querySelectorAll("[data-set-lang]");
  var saved = localStorage.getItem("vm-lang");
  var initial = saved || ((navigator.language || "").toLowerCase().indexOf("zh") === 0 ? "zh" : "en");

  function setLanguage(lang) {
    var normalized = lang === "zh" ? "zh" : "en";
    var isZh = normalized === "zh";

    root.setAttribute("data-vm-lang", normalized);
    root.setAttribute("lang", isZh ? "zh-CN" : "en");
    localStorage.setItem("vm-lang", normalized);

    buttons.forEach(function (button) {
      var active = button.getAttribute("data-set-lang") === normalized;
      button.setAttribute("aria-pressed", active ? "true" : "false");
    });
  }

  buttons.forEach(function (button) {
    button.addEventListener("click", function () {
      setLanguage(button.getAttribute("data-set-lang"));
    });
  });

  setLanguage(initial);
})();
