export function updateGreeting(newText) {
  const greetingEl = document.getElementById('greeting');
  if (greetingEl) greetingEl.textContent = newText;
}

(() => {
  // Demo call (commented out) to illustrate usage
  // updateGreeting('Hello, Dynamic World!');
})();
