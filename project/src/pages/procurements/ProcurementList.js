import { procurements } from '../../data/procurements.js';

export function renderProcurementList() {
  const getStatusBadgeClass = (status) => {
    const classes = {
      open: 'success',
      under_review: 'warning',
      closed: 'secondary'
    };
    return classes[status] || 'primary';
  };

  return `
    <div class="card">
      <div class="card-body">
        <h3 class="card-title mb-4">Active Procurements</h3>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th>Title</th>
                <th>Category</th>
                <th>Deadline</th>
                <th>Est. Value</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              ${procurements.map(proc => `
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <i class="bi bi-file-text me-2"></i>
                      ${proc.title}
                    </div>
                  </td>
                  <td>${proc.category}</td>
                  <td>${new Date(proc.deadline).toLocaleDateString()}</td>
                  <td>₹${proc.estimatedValue.toLocaleString()}</td>
                  <td>
                    <span class="badge bg-${getStatusBadgeClass(proc.status)}">
                      ${proc.status.replace('_', ' ')}
                    </span>
                  </td>
                </tr>
              `).join('')}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  `;
}