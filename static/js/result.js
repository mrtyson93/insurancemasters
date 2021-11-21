function changeOptions(){
    var quote = $('input[name="quote_value"]').val();
    var sel_deductible_option = $('select[name="deductible_options"] option').filter(":selected").val();
    var sel_coverage_option = $('select[name="coverage_per_incident_options"] option').filter(":selected").val();
    var final_quote = quote;
    switch (sel_deductible_option){
         case "1":
            //alert("option 2 selected");
             final_quote *= 1;
            break;
        case "2":
            //alert("option 2 selected");
            final_quote *= 0.9;
            break;
        case "3":
            final_quote *= 0.8;
            //alert("option 3 selected");
            break;
        case "4":
            //alert("option 4 selected");
            final_quote *= 0.75;
            break;
    }
    switch (sel_coverage_option){
         case "1":
             final_quote *= 1;
            break;
        case "2":
            final_quote *= 0.9;
            break;
        case "3":
            final_quote *= 0.75;
            break;
    }

    $("#final_quote").html(formatToCurrency(final_quote));
}

const formatToCurrency = amount => {
  return "$" + amount.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, "$&,");
};