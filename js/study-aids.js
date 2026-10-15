/*
 * study-aids.js
 * The memory aids on a verse card (a block with "aids": mnemonics, a
 * chain diagram, the metre, and so on) and the Sanskrit section of the
 * Settings screen, where each KIND of aid can be switched on or off.
 *
 * Every kind is on by default. The choice is saved in this browser only,
 * per book, under its own key "recall-quiz-aids:<bookId>". It is NOT
 * part of the book settings, so cloud sync never sends it to the account.
 *
 * How hiding works: the <html> element carries data-hide-aids="chain
 * pegs" (the kinds that are off) and css/rich-content.css hides the
 * matching .aid-item elements, so a card that is already open changes at
 * once. A block whose items are all hidden is hidden too (applyToBlock).
 */
(function setUpStudyAids(quiz) {
  "use strict";

  const STORAGE_KEY_PREFIX = "recall-quiz-aids:";
  const STORED_VERSION = 1;
  /**
   * Every kind of aid, in the order shown on the Settings screen:
   * [id, name, what it is]. A card may carry only the kinds that really
   * help for its verse; a kind switched on that no card has shows nothing.
   */
  const KINDS = [
    ["chain", "Chain and order", "Who passed it to whom, as a short chain or initials"],
    ["letters", "First letters", "A list of names held together by their first letters"],
    ["seesaw", "Pairs that answer each other", "यदा–तदा and other matching words"],
    ["sandhi", "Sandhi rule", "The join in the verse as a rule, and where it comes again"],
    ["frame", "Who, to whom, why", "A fixed frame to ask of every verse"],
    ["anchors", "Word families", "Link a new word to a word you already know"],
    ["diagram", "Diagram", "A chain or a ledge picture drawn from words"],
    ["metre", "Metre", "The verse cut into its quarter lines (pāda)"],
    ["chunks", "Rhythm chunks", "The verse said in short beats"],
    ["pegs", "Picture words", "A vivid picture for each key word"],
    ["puns", "Sound-alikes", "A familiar sound that carries the word"],
    ["contrast", "Look-alike pairs", "Two things that are easy to mix up, side by side"],
    ["story", "Story", "The verses as a small story with a cause at each step"],
  ];
  const state = { bookId: "", off: new Set(), isReady: false };
  const root = document.documentElement;
  let listElement = null;

  /** @returns {string[]} the ids of every kind */
  function kindIds() {
    return KINDS.map(function id(kind) { return kind[0]; });
  }

  /** @returns {string} the saved key for this book, or "" if not known */
  function storageKey() {
    return state.bookId ? STORAGE_KEY_PREFIX + state.bookId : "";
  }

  /** Read the saved choice for the open book (nothing saved: all on). */
  function load() {
    state.off = new Set();
    try {
      const raw = JSON.parse(window.localStorage.getItem(storageKey()));
      if (raw && raw.v === STORED_VERSION && Array.isArray(raw.off)) {
        raw.off.filter(function known(id) {
          return kindIds().indexOf(id) !== -1;
        }).forEach(function add(id) { state.off.add(id); });
      }
    } catch (error) {
      state.off = new Set();
    }
  }

  /** Save the choice, on this device only. */
  function save() {
    try {
      window.localStorage.setItem(storageKey(), JSON.stringify(
        { v: STORED_VERSION, off: Array.from(state.off) }));
    } catch (error) {
      // Private window or blocked storage: the choice lasts until reload.
    }
  }

  /** @param {string} id @returns {boolean} true if this kind is shown */
  function isOn(id) {
    return !state.off.has(id);
  }

  /**
   * Hide a block when every one of its items is off.
   * @param {HTMLElement} block a .aid-block
   */
  function applyToBlock(block) {
    const items = Array.from(block.querySelectorAll(".aid-item"));
    block.hidden = items.length > 0 && items.every(function off(item) {
      return !isOn(item.dataset.aid);
    });
  }

  /** Put the choice on the page: the html attribute and every block. */
  function applyAll() {
    root.setAttribute("data-hide-aids", Array.from(state.off).join(" "));
    document.querySelectorAll(".aid-block").forEach(applyToBlock);
    refreshSettings();
  }

  /**
   * Switch one kind on or off.
   * @param {string} id
   * @param {boolean} on
   */
  function setKind(id, on) {
    if (on) {
      state.off.delete(id);
    } else {
      state.off.add(id);
    }
    save();
    applyAll();
  }

  /** Switch every kind on or off at once. @param {boolean} on */
  function setAll(on) {
    state.off = on ? new Set() : new Set(kindIds());
    save();
    applyAll();
  }

  // ------------------------------------------------------------- settings

  /** Draw the rows of the Sanskrit section (once). */
  function buildSettings() {
    listElement = document.getElementById("sanskrit-aids-list");
    if (!listElement || listElement.children.length) {
      return;
    }
    KINDS.forEach(function addRow(kind) {
      const row = document.createElement("div");
      row.className = "setting-row";
      const label = document.createElement("div");
      label.className = "setting-label";
      label.appendChild(Object.assign(document.createElement("b"),
        { textContent: kind[1] }));
      label.appendChild(Object.assign(document.createElement("small"),
        { textContent: kind[2] }));
      const group = document.createElement("div");
      group.className = "choice-group";
      group.dataset.aid = kind[0];
      [["show", "Show"], ["hide", "Hide"]].forEach(function addButton(pair) {
        const button = document.createElement("button");
        button.type = "button";
        button.dataset.value = pair[0];
        button.textContent = pair[1];
        button.addEventListener("click", function choose() {
          setKind(kind[0], pair[0] === "show");
        });
        group.appendChild(button);
      });
      row.appendChild(label);
      row.appendChild(group);
      listElement.appendChild(row);
    });
    const all = document.getElementById("sanskrit-aids-all");
    const none = document.getElementById("sanskrit-aids-none");
    if (all) {
      all.addEventListener("click", function showAll() { setAll(true); });
    }
    if (none) {
      none.addEventListener("click", function hideAll() { setAll(false); });
    }
  }

  /** Show the chosen buttons and the "n of 13 on" summary. */
  function refreshSettings() {
    if (!listElement) {
      return;
    }
    listElement.querySelectorAll(".choice-group").forEach(function mark(g) {
      const on = isOn(g.dataset.aid);
      g.querySelectorAll("button").forEach(function press(button) {
        button.setAttribute("aria-pressed",
          String((button.dataset.value === "show") === on));
      });
    });
    const current = document.getElementById("sanskrit-section-current");
    if (current) {
      const count = KINDS.length - state.off.size;
      current.textContent = count === KINDS.length ? "All on" :
        count + " of " + KINDS.length + " on";
    }
  }

  document.addEventListener("recallquiz:book-opened", function opened(event) {
    state.bookId = (event.detail && event.detail.bookId) || "";
    load();
    state.isReady = true;
    buildSettings();
    applyAll();
  });

  quiz.studyAids = { kinds: KINDS, isOn, setKind, setAll, applyToBlock,
                     applyAll };
})(window.RecallQuiz = window.RecallQuiz || {});
