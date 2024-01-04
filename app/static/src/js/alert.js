// Remove Alert on Close
let alertButton = document.querySelector('.alert button');

if (alertButton){
  alertButton.addEventListener('click', function (event) {

  	// If the clicked element doesn't have the right selector, bail
    alertButton.parentNode.style.display = 'none';

  	// Don't follow the link
  	event.preventDefault();

  }, false);
}

function toggleButtons(button1, button2) {
  var userMenu = document.getElementById(button1);
  var closeUserMenu = document.getElementById(button2);

  // Toggle visibility of the buttons
  if (userMenu.style.display === 'none') {
      userMenu.style.display = 'block';
      closeUserMenu.style.display = 'none';
  } else {
      userMenu.style.display = 'none';
      closeUserMenu.style.display = 'block';
  }
}
