jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 575) {
      $('#list').addClass('dropdown-menu');
      $('#list').removeClass('nav');
    } else if (ww >= 575) {
      $('#list').removeClass('dropdown-menu');
      $('#list').addClass('nav');
    };
  };
  $(window).resize(function(){
    alterClass();
  });
  alterClass();
});