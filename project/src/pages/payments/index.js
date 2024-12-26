import { renderHero } from '../../components/Hero.js';
import { renderPaymentList } from './PaymentList.js';

export function renderPayments() {
  return `
    ${renderHero({
      title: 'Payment Management',
      subtitle: 'Track and manage vendor payments'
    })}
    <div class="container my-5">
      <div class="row">
        <div class="col-12">
          ${renderPaymentList()}
        </div>
      </div>
    </div>
  `;
}