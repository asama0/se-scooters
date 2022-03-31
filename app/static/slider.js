jQuery(document).ready(function($) {
  var alterClass = function() {
    var ww = document.body.clientWidth;
    if (ww < 575) {
      $('#list').addClass('collapse');
      $('#list').addClass('card card-body');
      $('#list').removeClass('nav');
    } else if (ww >= 575) {
      $('#list').removeClass('collapse');
      $('#list').removeClass('card card-body');
      $('#list').addClass('nav');
    };
  };
  $(window).resize(function(){
    alterClass();
  });
  alterClass();
});