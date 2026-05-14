---
layout: default
title: Search
---

# Search

공부한 내용에서 원하는 키워드를 검색할 수 있습니다.

<div class="search-box" style="margin: 20px 0;">
  <label for="search-input" style="display:block; font-weight:700; margin-bottom:8px;">검색어</label>
  <input
    id="search-input"
    type="search"
    placeholder="예: 리스트, for, 포인터, readline"
    autocomplete="off"
    style="width:100%; max-width:680px; padding:12px 14px; border:1px solid #d0d7de; border-radius:8px; font-size:16px;"
  >
</div>

<p id="search-count" style="color:#57606a;"></p>
<div id="search-results"></div>

<script>
  window.SEARCH_INDEX_URL = "{{ '/search.json' | relative_url }}";
</script>
<script src="{{ '/assets/js/search.js' | relative_url }}"></script>
