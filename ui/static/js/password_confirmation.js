var password = document.getElementById("id_password1")
  , confirm_password = document.getElementById("id_password2");

function validatePassword(){
  if(password.value != confirm_password.value) {

    // if there is some text in element.setCustomValidity, then an error message is raised
    // if empty string is provided, then it means there are no errors

    confirm_password.setCustomValidity("Passwords Don't Match");
  } else {
    confirm_password.setCustomValidity('');
  }
}

confirm_password.onkeyup = validatePassword;
