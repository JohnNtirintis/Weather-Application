$("form[name=signup_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/signup",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});

$("form[name=login_form").submit(function(e) {

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/user/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function(resp) {
      window.location.href = "/dashboard/";
    },
    error: function(resp) {
      $error.text(resp.responseJSON.error).removeClass("error--hidden");
    }
  });

  e.preventDefault();
});


// // Favorite City
// document.querySelectorAll('.star-btn').forEach(btn => {
//   btn.addEventListener('click', function() {
//     let cityName = this.getAttribute('data-city');

//     // Send POST request to server
//     fetch('/add_city_to_favorites', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ city: cityName }),
//     })
//     .then(response => response.json())
//     .then(data => {
//       // You can handle the server's response here
//       // For example, change the color of the star button to indicate the city has been added to favorites
//       if (data.success) {
//         this.classList.add('favorited');
//         alert("favorited")
//         console.log("HELLOOOO")
//       }
//     })
//     .catch((error) => {
//       console.error('Error:', error);
//     });
//   });
// });
