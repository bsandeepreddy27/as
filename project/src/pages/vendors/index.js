import { renderHero } from '../../components/Hero.js';
import { renderVendorRegistration } from './VendorRegistration.js';
import { renderVendorGuidelines } from './VendorGuidelines.js';
import { renderVendorList } from './VendorList.js';
import { vendors } from '../../data/vendors.js';

export function renderVendors() {
  return `
    ${renderHero({
      title: 'Vendor Portal',
      subtitle: 'Partner with us for business growth'
    })}
    <div class="container my-5">
      <div class="row mb-5">
        <div class="col-12">
          ${renderVendorList(vendors)}
        </div>
      </div>
      <div class="row">
        <div class="col-md-6 mb-4">
          ${renderVendorGuidelines()}
        </div>
        <div class="col-md-6">
          ${renderVendorRegistration()}
        </div>
      </div>
    </div>
  `;
}