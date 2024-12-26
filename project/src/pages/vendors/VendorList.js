export function renderVendorList(vendors) {
  return `
    <div class="card">
      <div class="card-body">
        <h3 class="card-title mb-4">Registered Vendors</h3>
        <div class="table-responsive">
          <table class="table table-hover">
            <thead>
              <tr>
                <th>Company Name</th>
                <th>Type</th>
                <th>Location</th>
                <th>Category</th>
                <th>Rating</th>
              </tr>
            </thead>
            <tbody>
              ${vendors.map(vendor => `
                <tr>
                  <td>
                    <div class="d-flex align-items-center">
                      <i class="bi bi-building me-2"></i>
                      ${vendor.companyName}
                    </div>
                  </td>
                  <td><span class="badge bg-secondary">${vendor.businessType}</span></td>
                  <td>${vendor.location}</td>
                  <td>${vendor.category}</td>
                  <td>
                    <div class="text-warning">
                      ${renderStars(vendor.rating)}
                    </div>
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

function renderStars(rating) {
  const fullStars = Math.floor(rating);
  const hasHalfStar = rating % 1 >= 0.5;
  let stars = '';
  
  for (let i = 0; i < fullStars; i++) {
    stars += '<i class="bi bi-star-fill"></i>';
  }
  
  if (hasHalfStar) {
    stars += '<i class="bi bi-star-half"></i>';
  }
  
  const emptyStars = 5 - Math.ceil(rating);
  for (let i = 0; i < emptyStars; i++) {
    stars += '<i class="bi bi-star"></i>';
  }
  
  return stars;
}