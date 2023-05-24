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
