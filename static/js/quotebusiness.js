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

  if (isNot30DaysAhead(selectedDate)) {
    alert("Date is not 30 days or more into the future");
    return false;
  } else {
    return true;
  }
}

function isNot30DaysAhead(selectedDate) {
  var today = new Date();
  var newSelectedDate = new Date(selectedDate);

  daysDifference =
    (newSelectedDate.getTime() - today.getTime()) / (1000 * 3600 * 24);
  return daysDifference < 30;
}
