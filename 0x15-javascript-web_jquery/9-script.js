// Ensure the code runs once the document is fully loaded
$(document).ready(function() {
  // Perform a GET request to the given URL
  $.get("https://hellosalut.stefanbohacek.dev/?lang=fr", function(data) {
    // Extract the "hello" value from the fetched data and set it as the text of the DIV#hello
    $("#hello").text(data.hello);
  });
});
