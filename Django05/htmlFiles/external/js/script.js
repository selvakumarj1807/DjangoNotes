document.getElementById("registrationForm").addEventListener("submit", function (e) {
    e.preventDefault();

    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;
    const message = document.getElementById("message");

    if (password !== confirmPassword) {
        message.textContent = "Passwords do not match!";
    } else {
        message.style.color = "green";
        message.textContent = "Registration successful!";
        alert("Registration successful!");
    }
});
