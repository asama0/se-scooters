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

  //change btn icon on click
  var clicked = false;
  var downArrow = `
  <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-chevron-down" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M1.646 4.646a.5.5 0 0 1 .708 0L8 10.293l5.646-5.647a.5.5 0 0 1 .708.708l-6 6a.5.5 0 0 1-.708 0l-6-6a.5.5 0 0 1 0-.708z"/>
  </svg>`;
  var upArrow = `
  <svg xmlns="http://www.w3.org/2000/svg" width="25" height="25" fill="currentColor" class="bi bi-chevron-up" viewBox="0 0 16 16">
    <path fill-rule="evenodd" d="M7.646 4.646a.5.5 0 0 1 .708 0l6 6a.5.5 0 0 1-.708.708L8 5.707l-5.646 5.647a.5.5 0 0 1-.708-.708l6-6z"/>
  </svg>`;
  $("#btn").click(function(){
    if (clicked){
      $('#btn').html(downArrow);
      clicked = false;
    } else {
      $('#btn').html(upArrow);
      clicked = true;
    }

    return false;
  });
});
