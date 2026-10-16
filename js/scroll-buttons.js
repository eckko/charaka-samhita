// Floating "go to top" / "go to bottom" buttons, shown on every screen.
(function () {
  function arrow(down) {
    return '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.6" ' +
      'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">' +
      (down ? '<path d="M12 4v13M6 12l6 6 6-6"/><path d="M5 21h14"/>'
            : '<path d="M5 3h14"/><path d="M12 20V7M6 12l6-6 6 6"/>') + '</svg>';
  }
  function make(label, down) {
    var b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', label);
    b.title = label;
    b.innerHTML = arrow(down);
    b.addEventListener('click', function () {
      var h = Math.max(document.documentElement.scrollHeight, document.body.scrollHeight);
      window.scrollTo({ top: down ? h : 0, behavior: 'smooth' });
    });
    return b;
  }
  function init() {
    var box = document.createElement('div');
    box.className = 'scroll-jump';
    box.appendChild(make('Go to top of page', false));
    box.appendChild(make('Go to bottom of page', true));
    document.body.appendChild(box);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
