export function renderHero({ title, subtitle }) {
  return `
    <div class="hero-section text-center py-5 bg-dark text-white">
      <div class="container">
        <h1 class="display-4">${title}</h1>
        <p class="lead">${subtitle}</p>
      </div>
    </div>
  `;
}