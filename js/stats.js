import { animateCount } from "./utils.js";
const GITHUB_USER = 'Aryanmishra-dev';
const CACHE_KEY   = 'gh_stats_cache';
const CACHE_TTL   = 3600 * 1000; // 1 hour

export async function fetchGitHubStats() {
  const cached = JSON.parse(localStorage.getItem(CACHE_KEY) || 'null');
  if (cached && Date.now() - cached.timestamp < CACHE_TTL) {
    renderStats(cached.data);
    return;
  }

  try {
    const [userRes, reposRes, eventsRes] = await Promise.all([
      fetch(`https://api.github.com/users/${GITHUB_USER}`),
      fetch(`https://api.github.com/users/${GITHUB_USER}/repos?per_page=100`),
      fetch(`https://api.github.com/users/${GITHUB_USER}/events/public?per_page=100`)
    ]);

    const user   = await userRes.json();
    const repos  = await reposRes.json();
    const events = await eventsRes.json();

    const totalCommits = events
      .filter(e => e.type === 'PushEvent')
      .reduce((sum, e) => sum + (e.payload.commits?.length || 0), 0);

    const totalStars = repos.reduce((sum, r) => sum + r.stargazers_count, 0);

    const data = {
      repos:   user.public_repos,
      commits: totalCommits,
      stars:   totalStars,
      followers: user.followers,
    };

    localStorage.setItem(CACHE_KEY, JSON.stringify({ timestamp: Date.now(), data }));
    renderStats(data);

  } catch (err) {
    console.warn('GitHub API failed, using cached fallback');
    renderStats({ repos: 32, commits: 502, stars: 0, followers: 0 });
  }
}

function renderStats(data) {
  Object.entries(data).forEach(([key, value]) => {
    document.querySelectorAll(`[data-stat="${key}"]`).forEach(el => {
      animateCount(el, value);
    });
  });
}

function animateCount(el, target) {
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


