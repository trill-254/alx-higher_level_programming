// Ensure the code runs once the document is fully loaded
$(document).ready(function() {
  // Define a click event handler for the div with id 'red_header'
  $("#red_header").click(function() {
    // Update the text color of the <header> element to red (#FF0000)
    $("header").css("color", "#FF0000");
  });
});
