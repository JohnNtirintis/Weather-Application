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
