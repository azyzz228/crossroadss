const usernameInput = document.getElementById("username--input");
const usernameCount = document.getElementById("username-count");
let usernameLimit = 15;
usernameCount.textContent = 0 + "/" + usernameLimit;

usernameInput.addEventListener("input", (e) => {
    let textLength = usernameInput.value.length;
    usernameCount.textContent = textLength + "/" + usernameLimit;
    console.log(textLength);
    // usernameCount.textContent = textLength + "/" + usernameLimit;
});


const titleInput = document.getElementById("title--input");
const titleCount = document.getElementById("title--count");
let titleLimit = 25;
titleCount.textContent = 0 + "/" + titleLimit;
titleInput.addEventListener("input", () => {
    let textLength = titleInput.value.length;
    titleCount.textContent = textLength + "/" + titleLimit;
});


const descriptionInput = document.getElementById("description--input");
const descriptionCount = document.getElementById("description--count");
let descriptionLimit = 250;
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
        emailWrapper.style.borderColor = "red";
    } else if (emailInput.value != "" && emailValidationRegex.test(emailInput.value)) {
        emailWrapper.style.borderColor = "green";
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



/**
 * Copy a string to clipboard
 * @param  {String} string         The string to be copied to clipboard
 * @return {Boolean}               returns a boolean correspondent to the success of the copy operation.
 * @see https://stackoverflow.com/a/53951634/938822
 */
function copyToClipboard(string) {
    let textarea;
    let result;

    try {
        textarea = document.createElement('textarea');
        //console.log("clipboard");
        textarea.setAttribute('readonly', true);
        textarea.setAttribute('contenteditable', true);
        textarea.style.position = 'fixed'; // prevent scroll from jumping to the bottom when focus is set.
        textarea.value = string;

        document.body.appendChild(textarea);

        textarea.focus();
        textarea.select();

        const range = document.createRange();
        range.selectNodeContents(textarea);

        const sel = window.getSelection();
        sel.removeAllRanges();
        sel.addRange(range);

        textarea.setSelectionRange(0, textarea.value.length);
        result = document.execCommand('copy');
    } catch (err) {
        console.error(err);
        result = null;
    } finally {
        document.body.removeChild(textarea);
    }

    // manual copy fallback using prompt
    // if (!result) {
    //   const isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    //   const copyHotkey = isMac ? '⌘C' : 'CTRL+C';
    //   result = prompt(`Press ${copyHotkey}`, string); // eslint-disable-line no-alert
    //   if (!result) {
    //     return false;
    //   }
    // }
    // return true;
}



function showNotification() {
    document.getElementById("notification").classList.replace("opacity-0", "opacity-100");

    setTimeout(() => {
        document.getElementById("notification").classList.replace("opacity-100", "opacity-0")
    }, 2000);
}

// CHANGE FIRST OPTION OF CATEGORY IS ALL



function copyContent(e) {
    let element = e.target
    showNotification();
    // console.log(element.previousElementSibling.textContent);
    copyToClipboard(element.previousElementSibling.textContent);
}



