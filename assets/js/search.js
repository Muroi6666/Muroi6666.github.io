(function () {
  const input = document.getElementById("search-input");
  const results = document.getElementById("search-results");
  const count = document.getElementById("search-count");

  if (!input || !results || !count) {
    return;
  }

  const indexUrl = window.SEARCH_INDEX_URL || "/search.json";
  let pages = [];

  function normalize(value) {
    return (value || "").toString().toLowerCase();
  }

  function escapeHtml(value) {
    return value
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#039;");
  }

  function makeSnippet(content, query) {
    const clean = content.replace(/\s+/g, " ").trim();
    const lowerClean = normalize(clean);
    const lowerQuery = normalize(query);
    const index = lowerClean.indexOf(lowerQuery);

    if (index === -1) {
      return clean.slice(0, 140);
    }

    const start = Math.max(0, index - 45);
    const end = Math.min(clean.length, index + lowerQuery.length + 95);
    const prefix = start > 0 ? "... " : "";
    const suffix = end < clean.length ? " ..." : "";

    return prefix + clean.slice(start, end) + suffix;
  }

  function render(query) {
    const trimmed = query.trim();

    if (!trimmed) {
      count.textContent = "검색어를 입력하면 결과가 표시됩니다.";
      results.innerHTML = "";
      return;
    }

    const terms = normalize(trimmed).split(/\s+/).filter(Boolean);
    const matches = pages.filter((page) => {
      const haystack = normalize(page.title + " " + page.content);
      return terms.every((term) => haystack.includes(term));
    });

    count.textContent = matches.length + "개의 결과를 찾았습니다.";

    if (matches.length === 0) {
      results.innerHTML = "<p>검색 결과가 없습니다.</p>";
      return;
    }

    results.innerHTML = matches
      .map((page) => {
        const title = escapeHtml(page.title);
        const url = escapeHtml(page.url);
        const snippet = escapeHtml(makeSnippet(page.content, trimmed));

        return [
          '<article style="padding:16px 0; border-top:1px solid #d0d7de;">',
          '<h2 style="font-size:20px; margin:0 0 6px;"><a href="' + url + '">' + title + "</a></h2>",
          '<p style="margin:0; color:#57606a;">' + snippet + "</p>",
          "</article>"
        ].join("");
      })
      .join("");
  }

  fetch(indexUrl)
    .then((response) => response.json())
    .then((data) => {
      pages = data.filter((page) => page.url && page.content);
      render(input.value);
      input.addEventListener("input", function () {
        render(input.value);
      });
    })
    .catch(() => {
      count.textContent = "검색 인덱스를 불러오지 못했습니다. Jekyll 서버를 다시 실행해보세요.";
    });
})();
