export function initFormHandlers() {
  document.addEventListener('submit', (e) => {
    if (e.target.id === 'contactForm') {
      e.preventDefault();
      handleContactFormSubmit(e.target);
    } else if (e.target.id === 'vendorForm') {
      e.preventDefault();
      handleVendorFormSubmit(e.target);
    }
  });
}

function handleContactFormSubmit(form) {
  alert('Message sent! (This is a demo)');
  form.reset();
}

function handleVendorFormSubmit(form) {
  alert('Vendor registration submitted! (This is a demo)');
  form.reset();
}