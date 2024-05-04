function blinkHeaders() {
    var headers = document.getElementsByTagName("h1");
    setInterval(function() {
      for (var i = 0; i < headers.length; i++) {
        var header = headers[i];
        if (header.style.visibility === "hidden") {
          header.style.visibility = "visible";
        } else {
          header.style.visibility = "hidden";
        }
      }
    }, 1000); // Change 500 to adjust blinking speed in milliseconds
  }
  
  // Call the function when the page is loaded
  window.onload = function() {
    blinkHeaders();
  };