document.getElementById("contactForm").addEventListener("submit", function (e) {
  e.preventDefault();

  let isValid = true;

  const name = document.getElementById("name");
  const email = document.getElementById("email");
  const message = document.getElementById("message");

  const nameError = document.getElementById("name-error");
  const emailError = document.getElementById("email-error");
  const messageError = document.getElementById("message-error");

  nameError.textContent = "";
  emailError.textContent = "";
  messageError.textContent = "";

  if (name.value.trim() === "") {
    nameError.textContent = "Моля, въведете име.";
    isValid = false;
  }

  if (email.value.trim() === "") {
    emailError.textContent = "Моля, въведете имейл.";
    isValid = false;
  } else if (!email.value.includes("@")) {
    emailError.textContent = "Моля, въведете валиден имейл адрес.";
    isValid = false;
  }

  if (message.value.trim() === "") {
    messageError.textContent = "Моля, въведете съобщение.";
    isValid = false;
  }

  if (isValid) {
    alert("Формата е изпратена успешно.");
    this.reset();
  }
});