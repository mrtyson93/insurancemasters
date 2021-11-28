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

function checkValidDate() {
  var selectedDate = document.getElementById("startpicker").value;

  if (isMoreThan90DaysAhead(selectedDate)) {
    alert("Date is 90 days or more into the future");
    return false;
  } else {
    return true;
  }
}

function isMoreThan90DaysAhead(selectedDate) {
  var today = new Date();
  var newSelectedDate = new Date(selectedDate);

  daysDifference =
    (newSelectedDate.getTime() - today.getTime()) / (1000 * 3600 * 24);
  return daysDifference > 90;
}
