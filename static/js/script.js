<script>
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
</script>
