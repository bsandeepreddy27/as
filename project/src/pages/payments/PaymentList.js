import { payments } from '../../data/payments.js';
import { vendors } from '../../data/vendors.js';

export function renderPaymentList() {
  return `
    <div class="card">
      <div class="card-body">
        <h3 class="card-title mb-4">Payment History</h3>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th>Invoice No.</th>
                <th>Vendor</th>
                <th>Amount</th>
                <th>Date</th>
                <th>Status</th>
                <th>Method</th>
              </tr>
            </thead>
            <tbody>
              ${payments.map(payment => {
                const vendor = vendors.find(v => v.id === payment.vendorId);
                return `
                  <tr>
                    <td>${payment.invoiceNumber}</td>
                    <td>${vendor ? vendor.companyName : 'N/A'}</td>
                    <td>₹${payment.amount.toLocaleString()}</td>
                    <td>${new Date(payment.date).toLocaleDateString()}</td>
                    <td>
                      <span class="badge bg-${payment.status === 'completed' ? 'success' : 'warning'}">
                        ${payment.status}
                      </span>
                    </td>
                    <td>${payment.paymentMethod}</td>
                  </tr>
                `;
              }).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  `;
}