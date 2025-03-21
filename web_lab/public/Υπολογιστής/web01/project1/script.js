const form = document.getElementById('form');
const usernameInput = document.getElementById('username');
const emailInput = document.getElementById('email');
const passwordInput = document.getElementById('password');
const validatePasswordInput = document.getElementById('validate-password');
const birthdayInput = document.getElementById('birthday');
const bioInput = document.getElementById('short-bio');
const progressBar = document.getElementById('progress-bar');
const submitButton = document.getElementById('submit-button');

submitButton.disabled = true;

let validations = {
    username: false,
    email: false,
    password: false,
    validatePassword: false,
    birthday: false,
    bio: false
};


usernameInput.addEventListener('input', () => {
    const usernameError = document.getElementById('username-validation-message');
    const value = usernameInput.value;
    const usernamePattern = /^[a-zA-Z][a-zA-Z0-9_]*$/;
    
    if (value.length < 3) {
        usernameError.textContent = "Τουλάχιστον 3 χαρακτήρες απαιτούνται";
        usernameError.style.color = "red";
        validations.username = false;
    } else if (!usernamePattern.test(value) || /[$%^&()\[\]]/.test(value)) {
        usernameError.textContent = "Μη επιτρεπτοί χαρακτήρες";
        usernameError.style.color = "red";
        validations.username = false;
    } else {
        usernameError.textContent = "Έγκυρο!";
        usernameError.style.color = "green";
        validations.username = true;
    }

    checkSubmitButton()
    updateProgressBar();

});


emailInput.addEventListener('input', () => {
    const emailError = document.getElementById('email-validation-message');
    const value = emailInput.value;
    const emailPattern = /^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z0-9._-]+\.[a-zA-Z]{2,4}$/;

    if (!emailPattern.test(value)) {
        emailError.textContent = "Μη έγκυρη διεύθυνση email";
        emailError.style.color = "red";
        validations.email = false;
    } else {
        emailError.textContent = "Έγκυρο!";
        emailError.style.color = "green";
        validations.email = true;
    }
    checkSubmitButton();
    updateProgressBar();
});


passwordInput.addEventListener('input', () => {
    const passwordError = document.getElementById('password-validation-message');
    const value = passwordInput.value;
    const hasLetter = /[a-zA-Z]/.test(value);
    const hasNumber = /[0-9]/.test(value);
    const hasSpecial = /[^a-zA-Z0-9]/.test(value);

    if (value.length < 6 || !hasLetter || !hasNumber || !hasSpecial) {
        passwordError.textContent = "Ο κωδικός πρέπει να έχει τουλάχιστον 6 χαρακτήρες, ένα γράμμα, έναν αριθμό και ένα ειδικό χαρακτήρα";
        passwordError.style.color = "red";
        validations.password = false;
    } else {
        passwordError.textContent = "Έγκυρο!";
        passwordError.style.color = "green";
        validations.password = true;
    }
    checkSubmitButton();
    updateProgressBar();
});


validatePasswordInput.addEventListener('input', () => {
    const validatePasswordError = document.getElementById('matching-password-validation-message');
    const isMatch = validatePasswordInput.value === passwordInput.value;

    if (!isMatch) {
        validatePasswordError.textContent = "Οι κωδικοί δεν ταιριάζουν";
        validatePasswordError.style.color = "red";
        validations.validatePassword = false;
    } else {
        validatePasswordError.textContent = "Έγκυρο!";
        validatePasswordError.style.color = "green";
        validations.validatePassword = true;
    }
    checkSubmitButton();
    updateProgressBar();
});


birthdayInput.addEventListener('change', () => {
    const birthdayError = document.getElementById('birthday-validation-message');
    const birthDate = new Date(birthdayInput.value);
    const today = new Date();
    const age = today.getFullYear() - birthDate.getFullYear();

    if (age < 18) {
        birthdayError.textContent = "Πρέπει να είστε τουλάχιστον 18 ετών";
        birthdayError.style.color = "red";
        validations.birthday = false;
    } else {
        birthdayError.textContent = "Έγκυρο!";
        birthdayError.style.color = "green";
        validations.birthday = true;
    }
    checkSubmitButton();
    updateProgressBar();
});


bioInput.addEventListener('input', () => {
    const charCount = document.getElementById('char-count');
    const currentLength = bioInput.value.length;
    const maxLength = 140;
    const bioErrorMassage = document.getElementById('bio-validation-message');
    
    charCount.textContent = `${currentLength}/${maxLength}`;
    if (currentLength > maxLength) {
        charCount.style.color = "red";
        validations.bio = false;
        bioErrorMassage.textContent = "Έχετε ξεπεράσει το όριο των λέξεων!";
        bioErrorMassage.style.color = "red";
        bioErrorMassage.style.display = "block";
    } else if(currentLength === 0){
        validations.bio = false;
        bioErrorMassage.textContent = "Πρέπει να προσθέσετε κάτι σε αυτό το πεδίο!";
        bioErrorMassage.style.color = "red";
        bioErrorMassage.style.display = "block";
    }
    else {
        charCount.style.color = "black";
        validations.bio = true;
        bioErrorMassage.textContent = "Έγκυρο!";
        bioErrorMassage.style.color = "green";
        bioErrorMassage.style.display = "block";
    }
    checkSubmitButton()
    updateProgressBar();
});

function updateProgressBar() {
    const totalToBeValid = Object.keys(validations).length;
    const totalValid = Object.values(validations).filter(Boolean).length;

    const progressPercentage = ((totalValid / totalToBeValid) * 100).toFixed(2);
    progressBar.style.width = progressPercentage + "%";
}

function checkSubmitButton(){
    submitButton.disabled = !(validations.birthday && validations.username && validations.validatePassword && validations.password
    &&validations.email && validations.bio)
}