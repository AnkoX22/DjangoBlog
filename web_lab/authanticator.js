
let users = [
    {username: "user1", password: "user1password"},
    {username: "user2", password: "user2password"}
];

let newUsers = [];

function authanticatePassword(username, password) {

    username = String(username).trim();
    password = String(password).trim();

    if(!username || !password){
        return false;
    }

    const user = users.find(user => user.username === username);
    if( user && user.password === password){
        return true;
    }

    return false;
}

function handleSubmit(event) {

    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if(authanticatePassword(username, password)){
        window.location.href = "main.html";
    }
    else {
        const error = document.getElementById("error-message");

        error.textContent = "Invalid username or password!"
        error.style.color = "red";
        error.style.display = "block";
    }
}

function handleSignUp(event){

    event.preventDefault();

    const new_username = document.getElementById("username").value;
    const new_password = document.getElementById("password").value;
    const first_name = document.getElementById("firstname").value;
    const last_name = document.getElementById("lastname").value;
    const  email = document.getElementById("email").value;
    const favourite_books = document.getElementById("favouritebooks").value;

    new_user = {
        username: String(new_username).trim(),
        password: String(new_password).trim(),
        first_name: String(first_name).trim(),
        last_name: String(last_name).trim(),
        email: String(email).trim(),
        favourite_books: String(favourite_books),
    }

    if(new_username && new_password && first_name && last_name && email && favourite_books){
        window.location.href = "main.html";
    } else {
        const error_message = document.getElementById("error-message");

        error_message.textContent = "Yu haven't filled all the input values"
        error_message.style.display = "block";
        error_message.color = "red";
    }

    newUsers.push(new_user);
    users.push({username: new_username, password: new_password})

    console.log(newUsers);
    console.log(users);
}

document.addEventListener("DOMContentLoaded", function(){

    const form = document.getElementById("login-form");
    const sign_up_form = document.getElementById("signup-form")

    if(form){
        form.addEventListener("submit",handleSubmit);
    }

    if(sign_up_form){
        sign_up_form.addEventListener("submit", handleSignUp);
    }
});

