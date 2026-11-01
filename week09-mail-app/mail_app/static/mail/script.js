// Wait until the DOM is fully loaded
document.addEventListener("DOMContentLoaded", function() {

  // Confirmation before sending mail
  const composeForm = document.querySelector("form");

  if (composeForm && window.location.pathname.includes("compose")) {
    composeForm.addEventListener("submit", function(event) {
      const confirmSend = confirm("Are you sure you want to send this mail?");
      if (!confirmSend) {
        event.preventDefault(); // cancel submission
      } else {
        // Show toast notification after sending
        showToast("✅ Mail sent successfully!");
      }
    });
  }

  // Highlight inbox items on hover
  const inboxItems = document.querySelectorAll("ul li");

  inboxItems.forEach(item => {
    item.addEventListener("mouseover", () => {
      item.style.backgroundColor = "#e9f5ff"; // light blue highlight
    });
    item.addEventListener("mouseout", () => {
      item.style.backgroundColor = "#fff"; // reset
    });
  });

  // Auto-focus first input field (login/register/compose)
  const firstInput = document.querySelector("form input");
  if (firstInput) {
    firstInput.focus();
  }

  // Password visibility toggle (login/register forms)
  const passwordFields = document.querySelectorAll("input[type='password']");

  passwordFields.forEach(field => {
    const toggle = document.createElement("span");
    toggle.textContent = "👁";
    toggle.style.cursor = "pointer";
    toggle.style.marginLeft = "10px";
    field.parentNode.appendChild(toggle);

    toggle.addEventListener("click", () => {
      field.type = field.type === "password" ? "text" : "password";
    });
  });

  // Toast notification function
  function showToast(message) {
    const toast = document.createElement("div");
    toast.textContent = message;
    toast.style.position = "fixed";
    toast.style.bottom = "20px";
    toast.style.right = "20px";
    toast.style.background = "#28a745";
    toast.style.color = "#fff";
    toast.style.padding = "10px 20px";
    toast.style.borderRadius = "5px";
    toast.style.boxShadow = "0px 2px 6px rgba(0,0,0,0.2)";
    document.body.appendChild(toast);

    setTimeout(() => toast.remove(), 3000); // disappear after 3s
  }
});
