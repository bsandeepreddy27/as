import { renderHero } from '../../components/Hero.js';
import { renderProcurementList } from './ProcurementList.js';

export function renderProcurements() {
  return `
    ${renderHero({
      title: 'Procurement Portal',
      subtitle: 'View active tenders and procurement opportunities'
    })}
    <div class="container my-5">
      <div class="row">
        <div class="col-12">
          ${renderProcurementList()}
        </div>
      </div>
    </div>
  `;
}