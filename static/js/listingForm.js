const titleInput = document.getElementById("title--input");
const titleCount = document.getElementById("title--count");
let titleLimit = 25;
titleCount.textContent = 0 + "/" + titleLimit;
titleInput.addEventListener("input", () => {
    let textLength = titleInput.value.length;
    titleCount.textContent = textLength + "/" + titleLimit;
});

const emailAAA = document.getElementById("email--input")
console.log(emailAAA);

const descriptionInput = document.getElementById("description--input");
const descriptionCount = document.getElementById("description--count");
let descriptionLimit = 450;
descriptionCount.textContent = 0 + "/" + descriptionLimit;
descriptionInput.addEventListener("input", () => {
    let textLength = descriptionInput.value.length;
    descriptionCount.textContent = textLength + "/" + descriptionLimit;
});


const regexV1 = /^[A-Za-z0-9]+(@duke.edu)$/;
const emailValidationRegex = /^[A-Za-z]+\S\d+(@duke.edu)$/;

const emailInput = document.getElementById("email--input");
const emailWrapper = document.getElementById("email--wrapper");
emailInput.addEventListener("input", () => {
    if (emailInput.value != "" && !emailValidationRegex.test(emailInput.value)) {
        emailWrapper.style.border = "1px solid red"

    } else if (emailInput.value != "" && emailValidationRegex.test(emailInput.value)) {
        emailWrapper.style.borderColor = "green";
    } else {
        emailWrapper.style.border = ""
    }
})

function validate() {
    if (emailInput.value != "" && emailValidationRegex.test(emailInput.value)) {
        return true;
    } else {
        document.getElementById("error").style.display = "block";
        return false;
    }
}