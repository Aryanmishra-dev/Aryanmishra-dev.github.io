export function initNav() {
  const sections  = document.querySelectorAll('section[id]');
  const navLinks  = document.querySelectorAll('.nav-item');
  
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        navLinks.forEach(link => link.classList.remove('active'));
        const active = document.querySelector(`.nav-item[href="#${entry.target.id}"]`);
        if (active) active.classList.add('active');
      }
    });
  }, { rootMargin: '-40% 0px -55% 0px' });
  
  sections.forEach(s => observer.observe(s));
  
  // Mobile drawer
  const ham = document.getElementById('ham');
  const sidebar = document.getElementById('sidebar');
  const ov = document.getElementById('ov');
  
  if (ham && sidebar && ov) {
    ham.addEventListener('click', () => {
      sidebar.classList.toggle('open');
      ov.classList.toggle('open');
      document.body.classList.toggle('menu-open');
      const isExpanded = ham.getAttribute('aria-expanded') === 'true';
      ham.setAttribute('aria-expanded', !isExpanded);
    });
  
    ov.addEventListener('click', () => {
      sidebar.classList.remove('open');
      ov.classList.remove('open');
      document.body.classList.remove('menu-open');
      ham.setAttribute('aria-expanded', 'false');
    });
  }
  
}
