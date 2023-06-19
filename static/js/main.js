const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
       console.log(entry)
       if(entry.isIntersecting){
        entry.target.classList.add('show');
        entry.target.classList.add('show-menu');
       }
    //    } else {
    //     // If we want to show the animation more than once
    //     // If we delete/comment the else statement
    //     // The animation will only be played once 
    //     entry.target.classList.remove('show');
    //    }
    });
});

document.getElementById("showFormButton").addEventListener('click', function() {
  var formContainer = document.getElementById("formContainer");
  var signup = document.getElementById("signup-link")
  if(!formContainer.classList.contains('visible') && (!signup.classList.contains('visible'))){
      formContainer.classList.add("visible");
      signup.classList.add('visible');
  } else {
      formContainer.classList.remove("visible");
      signup.classList.remove('visible')
  }
});

window.onload = function() {
    var letters = document.querySelectorAll('.letter');
    var delay = 200; // delay in milliseconds
    for(var i = 0; i < letters.length; i++) {
        (function(index) {
            setTimeout(function() { 
                letters[index].style.opacity = 1; 
            }, delay * index);
        })(i);
    }
};

const hiddenElements = document.querySelectorAll('.hidden');
const menuHiddenElements = document.querySelectorAll('.menu-hidden');
hiddenElements.forEach((el) => observer.observe(el))
menuHiddenElements.forEach((el) => observer.observe(el))

const nav = document.querySelector('.topnav');
const observerOptions = {
  root: null,
  rootMargin: '0px',
  threshold: 0.35 // Adjust the threshold as needed
};

const observer2 = new IntersectionObserver(entries => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      nav.classList.remove('blue');
    } else {
      nav.classList.add('blue');
    }
  });
}, observerOptions);

observer2.observe(document.querySelector('.content-section'));