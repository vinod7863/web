function validateLogin() {
    // Sample credentials (In real applications, credentials should be checked on the server)
    const validUsername = "student123";
    const validPassword = "password123";
    
    // Get input values
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();
    const errorMessage = document.getElementById("error-message");
    
    // Validate credentials
    if (username === validUsername && password === validPassword) {
        window.location.href = "test.html"; // Redirect to the test page
    } else {
        errorMessage.textContent = "Invalid username or password.";
        errorMessage.style.color = "red";
    }
}

// Ensure the DOM is loaded before adding event listener
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("login-button").addEventListener("click", validateLogin);
});
