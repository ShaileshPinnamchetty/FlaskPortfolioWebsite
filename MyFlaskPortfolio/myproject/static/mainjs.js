$(document).ready(function() {
var movementStrength = 35;
var height = movementStrength / $(window).height();
var width = movementStrength / $(window).width();
$("body").mousemove(function(e){
          var pageX = e.pageX - ($(window).width() / 1);
          var pageY = e.pageY - ($(window).height() / 1);
          var newvalueX = width * pageX * -1 - 10;
          var newvalueY = height * pageY * -1 - 10;
          $(this).css("background-position", newvalueX+"px     "+newvalueY+"px");
});
});

//$('body').mousemove(function(e){
//      var moveX = (e.pageX * -1 / 15);
//      var moveY = (e.pageY * -1 / 15);
//      $(this).css('background-position', moveX + 'px ' + moveY + 'px ')
//      })