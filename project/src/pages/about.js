import { renderHero } from '../components/Hero.js';

export function renderAbout() {
  return `
    ${renderHero({
      title: 'About Us',
      subtitle: 'Learn more about our journey'
    })}
    <div class="container my-5">
      <div class="row">
        <div class="col-lg-8 mx-auto">
          <h2 class="mb-4">Our Story</h2>
          <p class="lead">We are passionate about creating innovative solutions that help businesses grow and succeed in the digital age.</p>
          <p>With years of experience in software development, we've helped numerous clients achieve their goals through custom solutions.</p>
        </div>
      </div>
    </div>
  `;
}