document.getElementById("newsletter").addEventListener("submit", function (event) {
  event.preventDefault();
  var email = this.querySelector('input[type="email"]').value;
  alert("Thank you for subscribing, " + email);
  // Add more functionality as needed
});
