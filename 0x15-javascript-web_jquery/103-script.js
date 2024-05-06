$(document).ready(function() {
  function translateHello() {
    // Get the language code from the input field
    var langCode = $("#language_code").val();
    
    // Fetch the translation of "Hello" for the specified language code
    $.get(`https://www.fourtonfish.com/hellosalut/hello/?lang=${langCode}`, function(data) {
      // Set the translation in the DIV#hello
      $("#hello").text(data.hello);
    });
  }

  // Trigger translation when the button is clicked
  $("#btn_translate").click(translateHello);

  // Trigger translation when "Enter" is pressed while focused on the input field
  $("#language_code").keypress(function(event) {
    if (event.which === 13) { // Check if the key pressed is "Enter"
      translateHello(); // Call the translation function
    }
  });
});
