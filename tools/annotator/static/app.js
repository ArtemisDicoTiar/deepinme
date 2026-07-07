"use strict";

const state = {
  files: [],
  currentId: null,
  items: [],
  filterUnreviewed: true,
};

const $fileList = document.getElementById("file-list");
const $overallProgress = document.getElementById("overall-progress");
const $items = document.getElementById("items");
const $fileTitle = document.getElementById("file-title");
const $filterUnreviewed = document.getElementById("filter-unreviewed");

function escapeHtml(s) {
  return (s ?? "").replace(/[&<>"']/g, (c) => ({
    "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
  }[c]));
}

function progressBar(reviewed, count) {
  const pct = count ? Math.round((reviewed / count) * 100) : 0;
  return `
    <div class="progress-bar"><div style="width:${pct}%"></div></div>
    <div class="progress-label"><span>${reviewed}/${count}</span><span>${pct}%</span></div>
  `;
}

async function loadFiles() {
  const res = await fetch("/api/files");
  const data = await res.json();
  state.files = data.files;
  renderSidebar();
}

function renderSidebar() {
  const totalReviewed = state.files.reduce((a, f) => a + f.reviewed, 0);
  const totalCount = state.files.reduce((a, f) => a + f.count, 0);
  $overallProgress.innerHTML = `
    <div class="progress-label"><span>전체 진행</span></div>
    ${progressBar(totalReviewed, totalCount)}
  `;

  $fileList.innerHTML = state.files.map((f) => `
    <li data-id="${escapeHtml(f.id)}" class="${f.id === state.currentId ? "active" : ""}">
      <span class="instrument">${escapeHtml(f.instrument)}</span>
      ${progressBar(f.reviewed, f.count)}
    </li>
  `).join("");

  $fileList.querySelectorAll("li").forEach((li) => {
    li.addEventListener("click", () => loadFile(li.dataset.id));
  });
}

async function loadFile(id) {
  state.currentId = id;
  renderSidebar();
  $fileTitle.textContent = "불러오는 중…";
  const res = await fetch(`/api/file?id=${encodeURIComponent(id)}`);
  if (!res.ok) {
    $fileTitle.textContent = "불러오기 실패";
    return;
  }
  const data = await res.json();
  state.items = data.items;
  $fileTitle.textContent = `${data.meta.instrument || id} · ${state.items.length}문항`;
  renderItems();
}

function isBipolar(text) {
  return typeof text === "string" && text.includes(" ↔ ");
}

function defaultSourceFor(item) {
  if (item.text_ko_friendly && item.text_ko_friendly !== item.text) return "friendly";
  if (item.text_ko_friendly === item.text) return "friendly";
  return "translation";
}

function defaultTextFor(item, source) {
  if (source === "friendly") return item.text_ko_friendly || item.text || "";
  if (source === "translation") return item.text || "";
  return item.text_ko_friendly || item.text || "";
}

function renderItems() {
  const visible = state.filterUnreviewed
    ? state.items.filter((it) => !it.text_ko_friendly_reviewed)
    : state.items;

  if (!state.currentId) {
    $items.innerHTML = `<div class="empty-state">왼쪽에서 데이터셋을 선택하세요.</div>`;
    return;
  }
  if (!visible.length) {
    $items.innerHTML = `<div class="empty-state">🎉 이 데이터셋은 모두 검토되었습니다 (필터: ${state.filterUnreviewed ? "미검토만" : "전체"}).</div>`;
    return;
  }

  $items.innerHTML = visible.map((it, i) => itemCardHtml(it, i)).join("");

  visible.forEach((it, i) => wireCard(it, i));
}

function itemCardHtml(it, i) {
  const reviewed = !!it.text_ko_friendly_reviewed;
  const source = it.text_ko_friendly_source || defaultSourceFor(it);
  const initialText = reviewed ? (it.text_ko_friendly || "") : defaultTextFor(it, source);
  const dim = it.factor || it.facet || it.dimension || "";

  return `
    <div class="item-card ${reviewed ? "reviewed" : ""}" data-num="${escapeHtml(it.num)}" data-idx="${i}">
      <div class="item-head">
        <span>#${escapeHtml(it.num)} ${dim ? `<span class="badge">${escapeHtml(dim)}</span>` : ""}</span>
        <span class="${reviewed ? "reviewed-mark" : ""}">${reviewed ? "✓ 검토됨" : ""}</span>
      </div>
      <div class="cols">
        <div class="col en">
          <label>원문 (text_en)</label>
          <div class="val">${escapeHtml(it.text_en || "—")}</div>
        </div>
        <div class="col ko">
          <label>번역 (text)</label>
          <div class="val">${escapeHtml(it.text || "—")}</div>
        </div>
      </div>
      <div class="choices">
        <label><input type="radio" name="src-${i}" value="friendly" ${source === "friendly" ? "checked" : ""} ${!it.text_ko_friendly ? "disabled" : ""}/>
          친화(추천)${it.text_ko_friendly ? `<span class="friendly-text">— ${escapeHtml(it.text_ko_friendly)}</span>` : `<span class="friendly-text">(제안 없음)</span>`}
        </label>
        <label><input type="radio" name="src-${i}" value="translation" ${source === "translation" ? "checked" : ""}/>
          번역 사용<span class="translation-text">— ${escapeHtml(it.text || "")}</span>
        </label>
        <label><input type="radio" name="src-${i}" value="custom" ${source === "custom" ? "checked" : ""}/>
          직접 입력
        </label>
      </div>
      <textarea class="final-text" rows="2">${escapeHtml(initialText)}</textarea>
      <div class="item-foot">
        <span class="warn" style="display:none"></span>
        <button class="save">저장</button>
      </div>
    </div>
  `;
}

function wireCard(it, i) {
  const card = $items.querySelector(`.item-card[data-idx="${i}"]`);
  const textarea = card.querySelector("textarea.final-text");
  const radios = card.querySelectorAll(`input[name="src-${i}"]`);
  const saveBtn = card.querySelector("button.save");
  const warn = card.querySelector(".warn");

  radios.forEach((r) => {
    r.addEventListener("change", () => {
      textarea.value = defaultTextFor(it, r.value);
      saveBtn.classList.remove("saved");
      saveBtn.textContent = "저장";
    });
  });

  function checkWarn() {
    const sourceHasBipolar = isBipolar(it.text_en) || isBipolar(it.text);
    if (sourceHasBipolar && !isBipolar(textarea.value)) {
      warn.style.display = "inline";
      warn.textContent = "⚠ 원문은 양극형(A ↔ B)인데 ' ↔ ' 구분자가 없습니다.";
    } else {
      warn.style.display = "none";
    }
  }
  textarea.addEventListener("input", () => {
    saveBtn.classList.remove("saved");
    saveBtn.textContent = "저장";
    checkWarn();
  });
  checkWarn();

  saveBtn.addEventListener("click", async () => {
    const source = card.querySelector(`input[name="src-${i}"]:checked`)?.value || "custom";
    const text = textarea.value.trim();
    if (!text) return;
    saveBtn.disabled = true;
    saveBtn.textContent = "저장 중…";
    try {
      const res = await fetch("/api/item", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id: state.currentId, num: it.num, text, source }),
      });
      const data = await res.json();
      if (!res.ok) throw new Error(data.error || "save failed");

      Object.assign(it, data.item);
      const fileEntry = state.files.find((f) => f.id === state.currentId);
      if (fileEntry) Object.assign(fileEntry, data.summary);
      renderSidebar();

      saveBtn.disabled = false;
      saveBtn.textContent = "✓ 저장됨";
      saveBtn.classList.add("saved");
      card.classList.add("reviewed");
      card.querySelector(".item-head .reviewed-mark").textContent = "✓ 검토됨";

      if (state.filterUnreviewed) {
        setTimeout(() => renderItems(), 300);
      }
    } catch (err) {
      saveBtn.disabled = false;
      saveBtn.textContent = "저장 실패 — 재시도";
      console.error(err);
    }
  });
}

$filterUnreviewed.addEventListener("change", () => {
  state.filterUnreviewed = $filterUnreviewed.checked;
  renderItems();
});

loadFiles();
