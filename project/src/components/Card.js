export function renderCard({ title, content, className = '' }) {
  return `
    <div class="card h-100 ${className}">
      <div class="card-body">
        <h5 class="card-title">${title}</h5>
        <div class="card-text">${content}</div>
      </div>
    </div>
  `;
}