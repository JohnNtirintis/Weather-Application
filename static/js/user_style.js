document.querySelectorAll('input').forEach((item) => {
    item.addEventListener("focus", function () {
        item.previousElementSibling.className = 'label-selected';
    })
    item.addEventListener("blur", function () {
        console.log(item.value);
        if (item.value === '') {
            item.previousElementSibling.className = '';
        }
    })
})

function resetAnimation(element) {
    element.style.animation = 'none';
    element.offsetHeight; // Trigger a reflow, flushing the CSS changes
    element.style.animation = null; 
}

document.getElementById("registerLink").addEventListener("click", function () {
    if (window.innerWidth < 600) {
        document.getElementById("signUp").style.display = 'block';
        document.getElementById("login").style.display = 'none';
    }
    else {
        document.getElementById("overlay").style.transform = 'translate(550px , -25px)';
        document.getElementById("overlay-text").innerHTML = "We will be very happy to have you over :)";
        resetAnimation(document.getElementById("overlay-text"));  // restart the animation
    }
});

document.getElementById("loginLink").addEventListener("click", function () {
    if (window.innerWidth < 600) {
        document.getElementById("login").style.display = 'block';
        document.getElementById("signUp").style.display = 'none';
    }
    else {
        document.getElementById("overlay").style.transform = 'translate(0px , -25px)';
        document.getElementById("overlay-text").innerHTML = "Welcome back friend. How you've been?";
        resetAnimation(document.getElementById("overlay-text"));  // restart the animation
    }
});