document.addEventListener("DOMContentLoaded", () => {
    // Show spinner on generate
    const tagForm = document.getElementById("tagForm");
    const spinner = document.getElementById("spinner");
    if (tagForm) {
      tagForm.addEventListener("submit", () => {
        spinner.classList.remove("hidden");
      });
    }
  
    // (Optional) disable post button after click
    const postForm = document.getElementById("postForm");
    if (postForm) {
      postForm.addEventListener("submit", () => {
        postForm.querySelector("button").disabled = true;
      });
    }
  });
  