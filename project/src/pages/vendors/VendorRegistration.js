export function renderVendorRegistration() {
  return `
    <div class="card">
      <div class="card-body">
        <h3 class="card-title mb-4">Vendor Registration</h3>
        <form id="vendorForm">
          <div class="mb-3">
            <label for="companyName" class="form-label">Company Name</label>
            <input type="text" class="form-control" id="companyName" required>
          </div>
          <div class="mb-3">
            <label for="businessType" class="form-label">Business Type</label>
            <select class="form-select" id="businessType" required>
              <option value="">Select business type</option>
              <option value="manufacturer">Manufacturer</option>
              <option value="supplier">Supplier</option>
              <option value="service">Service Provider</option>
            </select>
          </div>
          <div class="mb-3">
            <label for="gstNumber" class="form-label">GST Number</label>
            <input type="text" class="form-control" id="gstNumber" required>
          </div>
          <div class="mb-3">
            <label for="contactPerson" class="form-label">Contact Person</label>
            <input type="text" class="form-control" id="contactPerson" required>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label">Email</label>
            <input type="email" class="form-control" id="email" required>
          </div>
          <div class="mb-3">
            <label for="phone" class="form-label">Phone</label>
            <input type="tel" class="form-control" id="phone" required>
          </div>
          <button type="submit" class="btn btn-primary">Submit Registration</button>
        </form>
      </div>
    </div>
  `;
}