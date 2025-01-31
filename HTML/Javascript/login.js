function validateLogin(event) {
    event.preventDefault();

    const validEmail = "vinod@gmail.com";
    const validPassword = "student123";

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const errorMessage = document.getElementById("error-message");

    if (email === validEmail && password === validPassword) {
        window.location.href = './Test.html';
    } else {
        errorMessage.textContent = "Invalid username or password. Please try again.";
        errorMessage.style.color = "red";
    }
}