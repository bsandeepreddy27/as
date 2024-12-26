import { renderHero } from '../components/Hero.js';

export function renderHome() {
  return `
    ${renderHero({
      title: 'Welcome to AS',
      subtitle: 'Your Partner in Innovation'
    })}
    <div class="container my-5">
      <div class="row">
        <div class="col-md-4 mb-4">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">Web Development</h5>
              <p class="card-text">Custom web solutions tailored to your needs.</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">Mobile Apps</h5>
              <p class="card-text">Native and cross-platform mobile applications.</p>
            </div>
          </div>
        </div>
        <div class="col-md-4 mb-4">
          <div class="card h-100">
            <div class="card-body">
              <h5 class="card-title">Cloud Solutions</h5>
              <p class="card-text">Scalable and reliable cloud infrastructure.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
}