/**
 * Shared utility helpers
 */

/**
 * Animate a number counting up from 0 to target.
 * Uses IntersectionObserver so it only fires when visible.
 */
export function animateCount(el, target) {
  const duration = 1500;
  const start    = performance.now();
  const from     = 0;

  const observer = new IntersectionObserver(([entry]) => {
    if (!entry.isIntersecting) return;
    observer.disconnect();

    function tick(now) {
      const elapsed  = now - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased    = 1 - Math.pow(1 - progress, 3); // ease-out-cubic
      el.textContent = Math.round(from + eased * (target - from));
      if (progress < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  });

  observer.observe(el);
}

/**
 * Debounce a function call.
 */
export function debounce(fn, delay = 250) {
  let timer;
  return (...args) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn.apply(this, args), delay);
  };
}
