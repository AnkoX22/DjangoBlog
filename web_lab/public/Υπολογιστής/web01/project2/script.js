const dishChoice = document.getElementById('choose-dish');
const ingredient1 = document.getElementById('ingredient1');
const ingredient2 = document.getElementById('ingredient2');
const ingredient3 = document.getElementById('ingredient3');
const ingredient4 = document.getElementById('ingredient4');
const username = document.getElementById('username');
const usernameError = document.getElementById('username-error');
const phoneNumberInput = document.getElementById('phone-number');
const phoneNumberError = document.getElementById('phone-number-error');
const totalPrice = document.getElementById('total-price');
const deliverySelect = document.getElementById("delivery-options");
const tipInput = document.getElementById('tip');
const paymentMethods = document.getElementById('payment-methods');
const ingredientCheckboxes = document.querySelectorAll('input[name="ingredients[]"]');
const submitButton = document.getElementById('submit-button');

let foodCost = 0;
let totalCost = 0;
let tipCost = 0;
let paymentCost = 0;
let deliveryCost = 0;

let isUsernameValid = false;
let isNumberValid = false;
submitButton.disabled = true;

const dish_prices = [
    {
        "dish": 8.00,
        "ingredient1": 1.00,
        "ingredient2": 0.50,
        "ingredient3": 0.70,
        "ingredient4": 1.00
    },
    {
        "dish": 7.00,
        "ingredient1": 1.50,
        "ingredient2": 0.80,
        "ingredient3": 1.00,
        "ingredient4": 0.50
    },
    {
        "dish": 6.00,
        "ingredient1": 1.00,
        "ingredient2": 1.20,
        "ingredient3": 0.50,
        "ingredient4": 2.00
    },
]

window.addEventListener('DOMContentLoaded', () => {
    // Set initial food cost based on default selected dish
    foodCost = dish_prices[dishChoice.value - 1]["dish"];

    // Reset all ingredient checkboxes
    ingredientCheckboxes.forEach(checkbox => {
        checkbox.checked = false;
    });

    const dish = dishChoice.value;
    if (dish === '1') {
        ingredient1.innerHTML = `<b>Τυρί<br>(€1.00)</b>`;
        ingredient2.innerHTML = `<b>Ντομάτες<br>(€0.50)</b>`;
        ingredient3.innerHTML = `<b>Ελιές<br>(€0.70)</b>`;
        ingredient4.innerHTML = `<b>Μανιτάρια<br>(€1.00)</b>`;
    }

    updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
    ingredientCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            foodCost = dish_prices[dishChoice.value - 1]["dish"]; // Reset to base price
            ingredientCheckboxes.forEach(cb => {
                if(cb.checked) {
                    foodCost += dish_prices[dishChoice.value - 1][cb.value] || 0;
                }
            });
            updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
        });
    });


});

dishChoice.addEventListener('change', () => {
  const dish = dishChoice.value;
  if (dish === '1') {
    ingredient1.innerHTML = `<b>Τυρί<br>(€1.00)</b>`;
    ingredient2.innerHTML = `<b>Ντομάτες<br>(€0.50)</b>`;
    ingredient3.innerHTML = `<b>Ελιές<br>(€0.70)</b>`;
    ingredient4.innerHTML = `<b>Μανιτάρια<br>(€1.00)</b>`;
  } else if (dish === '2') {
    ingredient1.innerHTML = `<b>Μπέικον<br>(€1.50)</b>`;
    ingredient2.innerHTML = `<b>Πιπεριές<br>(€0.80)</b>`;
    ingredient3.innerHTML = `<b>Τυρί Τσένταρ<br>(€1.00)<b>`;
    ingredient4.innerHTML = `<b>Μαρούλι<br>(€0.50)<b>`;
  } else if (dish === '3') {
    ingredient1.innerHTML = `<b>Σάλτσα Ντομάτας<br>(€1.00)</b>`;
    ingredient2.innerHTML = `<b>Παραδοσιακό Τυρί<br>(€1.20)</b>`;
    ingredient3.innerHTML = `<b>Βασιλικός<br>(€0.50)</b>`;
    ingredient4.innerHTML = `<b>Κιμάς<br>(€2.00)</b>`;
  }

    foodCost = dish_prices[dish - 1]["dish"];
    updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
    ingredientCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', () => {
            foodCost = dish_prices[dishChoice.value - 1]["dish"]; // Reset to base price
            ingredientCheckboxes.forEach(cb => {
                if(cb.checked) {
                    foodCost += dish_prices[dishChoice.value - 1][cb.value] || 0;
                }
            });
            updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
        });
    });
});


const usernamePattern = /^[a-zA-Z]/;
const usernamePattern2 = /[a-zA-Z]+\s+[a-zA-Z]+/;
username.addEventListener('change', () => {
  if(!usernamePattern.test(username.value) || !usernamePattern2.test(username.value)){
      if (!usernamePattern.test(username.value)) {
          usernameError.style.display = 'block';
          usernameError.innerHTML = 'Το όνομα πρέπει να περιέχει μόνο γράμματα';
          usernameError.style.color = 'red';
          username.style.backgroundColor = 'white';
          console.log('error pattern 1');
          isUsernameValid = false;
      }
      if(!usernamePattern2.test(username.value)){
          usernameError.style.display = 'block';
          usernameError.innerHTML = 'Το όνομα και το επίθετο θα πρέπει να περιέχουν κενό μεταξύ τους';
          usernameError.style.color = 'red';
          username.style.backgroundColor = 'white';
          console.log('error pattern 2');
          isUsernameValid = false;
      }

  }else {
      usernameError.style.display = 'none';
      usernameError.innerHTML = '';
      username.style.backgroundColor = 'lightgreen';
      console.log('no error');
      isUsernameValid = true;
      checkSubmitButton();
  }
  });

const phoneNumberPattern1 = /^(\+30)?69[0-9]{8}$/;
const phoneNumberPattern2 = /^(\+30)?2[0-9]{9}$/;

phoneNumberInput.addEventListener('change', () => {
    
    if(!(phoneNumberPattern2.test(phoneNumberInput.value) || phoneNumberPattern1.test(phoneNumberInput.value))){
        phoneNumberError.style.display = 'block';
        phoneNumberError.innerHTML = 'Το τηλέφωνο πρέπει να έχει την μορφή +302ΧΧΧΧΧΧΧΧΧ / +3069XXXXXXXX ή 2ΧΧΧΧΧΧΧΧΧ / 69XXXXXXXX';
        phoneNumberError.style.color = 'red';
        phoneNumberInput.style.backgroundColor = 'white';
        console.log('error pattern 2');
        isNumberValid = false
    } else {
        phoneNumberError.style.display = 'none';
        phoneNumberError.innerHTML = '';
        phoneNumberInput.style.backgroundColor = 'lightgreen';
        console.log('no error');
        isNumberValid = true;
    }
    checkSubmitButton();
});

deliverySelect.addEventListener('change', () => {
    if(deliverySelect.value === 'delivery'){
        deliveryCost = 1;
    } else {
        deliveryCost = 0;
    }
    updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
})
tipInput.addEventListener('change', () => {
    if(parseFloat(tipInput.value) < 0){
        tipInput.innerHTML = "0";
    }
    tipCost = parseFloat(tipInput.value);
    updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
})

paymentMethods.addEventListener('change', () => {
    if(paymentMethods.value === 'credit-card'){
        paymentCost = 0.50;
    }
    else {
        paymentCost = 0;
    }
    updateCosts(foodCost, deliveryCost, tipCost, paymentCost);
})

const updateCosts = (foodPrice, deliveryPrice, tipPrice, paymentPrice) => {
    totalCost = foodPrice + deliveryPrice + tipPrice + paymentPrice;
    totalPrice.textContent = totalCost;
}

function checkSubmitButton() {

    submitButton.disabled = !(isNumberValid && isUsernameValid);
}