function displayOptionTextField() {
  var businessNature = document.getElementById("business_natures").value;
  if (businessNature == "other") {
    textField = document.getElementById("optionalBusinessNatureRow");
    textField.style.display = "block";
    textField.style.visibility = "visible";
  } else {
    document.getElementById("optionalBusinessNatureRow").style.display = "none";
  }
}

