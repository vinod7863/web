function validateRegistration(){
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;
    let confirmPassword = document.getElementById("confirmPassword").value;
    
    let emailError = document.getElementById("emailError");
    let passwordError = document.getElementById("passwordError");
    let confirmPasswordError = document.getElementById("confirmPasswordError");

    let isValid = true;

    emailError.textContent= "";
    passwordError.textContent= "";
    confirmPasswordError.textContent= "";

    const emailRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
    if(!emailRegex.test(email)){
        emailError.innerText = "Invalid email";
        isValid = false;
    }

    if(password.length < 8){
        passwordError.textContent = "Password must be at least 8 characters long";
        isValid = false;
    } else if(!/[0-9]/.test(password)){
        passwordError.textContent = "Password must contain at least one number";
        isValid = false;
    } else if(!/[A-Z]/.test(password)){
        passwordError.textContent = "Password must contain at least one uppercase letter";
        isValid = false;
    } else if(!/[!@#$%^&*]/.test(password)){
        passwordError.textContent = "Password must contain at least one special character";
        isValid = false;
    }

    if(password !== confirmPassword){
        confirmPasswordError.textContent = "Passwords do not match";
        isValid = false;
    }

    return isValid;
}