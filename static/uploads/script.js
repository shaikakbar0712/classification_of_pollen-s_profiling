// Show the requested slide
function showSlide(id) {
  document.querySelectorAll(".slide").forEach(slide => {
    slide.classList.remove("active");
  });
  document.getElementById(id).classList.add("active");
}

// Default slide on first load
document.addEventListener("DOMContentLoaded", () => {
  showSlide("predict"); // You can change this to "about" or "contact" if needed

  // Update button while submitting
  const form = document.querySelector("form");
  if (form) {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button");
      if (button) {
        button.innerText = "Classifying...";
        button.disabled = true;
      }
    });
  }
});
