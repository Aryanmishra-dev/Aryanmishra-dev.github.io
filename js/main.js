import { fetchGitHubStats } from './stats.js';
import { fetchHashnodePosts } from './hashnode-feed.js';
import { initScrollReveal } from './animations.js';
import { initNav } from './nav.js';
import { initProjectFilters } from './projects.js';

document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initScrollReveal();
  initProjectFilters();
  fetchGitHubStats();
  fetchHashnodePosts();
});
