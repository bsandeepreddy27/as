import { renderCard } from '../components/Card.js';
import { hydroProjects, thermalProjects } from '../data/projects.js';

export function renderProjects() {
  const renderProjectList = (projects) => {
    return `
      <ul class="list-group list-group-flush">
        ${projects.map(project => `
          <li class="list-group-item">
            ${project.name}
            <small class="text-muted d-block">Location: ${project.location}</small>
          </li>
        `).join('')}
      </ul>
    `;
  };

  return `
    <div class="container my-5">
      <h2 class="mb-4">Our Projects</h2>
      <div class="row g-4">
        <div class="col-md-6">
          ${renderCard({
            title: 'Hydro Projects',
            content: renderProjectList(hydroProjects)
          })}
        </div>
        <div class="col-md-6">
          ${renderCard({
            title: 'Thermal Projects',
            content: renderProjectList(thermalProjects)
          })}
        </div>
      </div>
    </div>
  `;
}