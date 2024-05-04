setTimeout(function() {
  var cards = document.querySelectorAll('.card');
  cards.forEach(function(card) {
      var content = card.innerText;
      var replacedContent = content.replace(/./g, '*'); // Replace each character with *
      card.innerText = replacedContent;
  });
}, 700); // 700 milliseconds = 0.7 seconds

  // Call the function when the page is loaded
  window.onload = function() {
    blinkHeaders();
  };