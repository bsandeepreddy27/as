import { renderHero } from '../components/Hero.js';
import { renderContactForm } from '../components/ContactForm.js';

export function renderContact() {
  return `
    ${renderHero({
      title: 'Contact Us',
      subtitle: 'Get in touch with our team'
    })}
    <div class="container my-5">
      <div class="row">
        <div class="col-md-6 mb-4">
          <h3>Our Office</h3>
          <p>
            123 Tech Street<br>
            Innovation City, IC 12345<br>
            United States
          </p>
          <p>
            <strong>Email:</strong> contact@as.com<br>
            <strong>Phone:</strong> (123) 456-7890
          </p>
        </div>
        <div class="col-md-6">
          ${renderContactForm()}
        </div>
      </div>
    </div>
  `;
}