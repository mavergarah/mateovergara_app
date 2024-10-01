const images = document.querySelectorAll('.image');
const indicators = document.querySelectorAll('.indicator');
let currentImage = 0;

function showImage(n) {
  images.forEach((image, index) => {
    image.style.display = index === n ? 'block' : 'none';
  });
  indicators.forEach((indicator, index) => {
    indicator.classList.toggle('active', index === n);
  });
}

function toggleDropdown(event) {
  event.preventDefault(); // Prevent default link behavior
  const dropdownContent = event.target.nextElementSibling;
  dropdownContent.classList.toggle("show");
}

// Attach event listeners to all dropdown buttons
const dropdownButtons = document.querySelectorAll('.dropbtn');
dropdownButtons.forEach(button => {
  button.addEventListener('click', toggleDropdown);
});
