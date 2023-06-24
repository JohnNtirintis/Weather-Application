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

if(document.getElementById('showFormButton')){
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
}

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

function rgbToHex(rgb) {
  let sep = rgb.indexOf(",") > -1 ? "," : " ";
  rgb = rgb.substr(4).split(")")[0].split(sep);

  let r = (+rgb[0]).toString(16),
      g = (+rgb[1]).toString(16),
      b = (+rgb[2]).toString(16);

  if (r.length == 1)
      r = "0" + r;
  if (g.length == 1)
      g = "0" + g;
  if (b.length == 1)
      b = "0" + b;

  return "#" + r + g + b;
}

let star_button = document.getElementById('favoriteCity');

star_button.addEventListener('click', function() {
  let cityName = this.getAttribute('data-city');
  let star = document.getElementById('star');
  let currentColor = window.getComputedStyle(star).getPropertyValue('color');
  let hexColor = rgbToHex(currentColor);

  if(hexColor == "#ffffff"){
    star.style.color = '#e8cc17';
    fetch('/add_city_to_favorites', {
      method: 'POST',
      dataType: 'json',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ city: cityName }),
    })
    .then(response => response.json())
    .then(data => {
      if (data.success) {
        this.classList.add('favorited');
        alert("favorited")
        console.log("HELLOOOO")
      }
    })
    .catch((error) => {
      console.error('Error:', error);
    });
  } else if(hexColor == '#e8cc17'){
    star.style.color = '#ffffff';
  }
});