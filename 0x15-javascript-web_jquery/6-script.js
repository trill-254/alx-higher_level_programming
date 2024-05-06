// Ensure the code runs once the document is fully loaded
$(document).ready(function() {
  // Add a click event handler to the div with id 'update_header'
  $("#update_header").click(function() {
    // Change the text of the <header> element to 'New Header!!!'
    $("header").text("New Header!!!");
  });
});
