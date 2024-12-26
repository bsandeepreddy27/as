import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';
import 'bootstrap-icons/font/bootstrap-icons.css';
import './styles/main.css';

import { renderNavbar } from './components/Navbar.js';
import { renderHome } from './pages/home.js';
import { renderAbout } from './pages/about.js';
import { renderContact } from './pages/contact.js';
import { renderVendors } from './pages/vendors/index.js';
import { renderPayments } from './pages/payments/index.js';
import { renderProcurements } from './pages/procurements/index.js';
import { renderProjects } from './pages/projects.js';
import { initRouter } from './utils/router.js';
import { initFormHandlers } from './utils/formHandler.js';

// Define routes
const routes = {
  '/': renderHome,
  '/about': renderAbout,
  '/contact': renderContact,
  '/vendors': renderVendors,
  '/payments': renderPayments,
  '/procurements': renderProcurements,
  '/projects': renderProjects
};

// Initialize app
document.addEventListener('DOMContentLoaded', () => {
  document.querySelector('header').innerHTML = renderNavbar();
  initRouter(routes);
  initFormHandlers();
});