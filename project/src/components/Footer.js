export function renderFooter() {
  return `
    <footer class="footer mt-auto py-3 bg-light">
      <div class="container text-center">
        <span class="text-muted">© ${new Date().getFullYear()} NEEPCO. All rights reserved.</span>
      </div>
    </footer>
  `;
}