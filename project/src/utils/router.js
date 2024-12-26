export function initRouter(routes) {
  function handleRoute() {
    const path = window.location.pathname;
    const route = routes[path] || routes['/'];
    document.getElementById('app').innerHTML = route();
  }

  // Handle initial route
  handleRoute();

  // Handle navigation
  document.addEventListener('click', (e) => {
    if (e.target.matches('a') && e.target.href.startsWith(window.location.origin)) {
      e.preventDefault();
      window.history.pushState({}, '', e.target.href);
      handleRoute();
    }
  });

  // Handle browser back/forward
  window.addEventListener('popstate', handleRoute);
}