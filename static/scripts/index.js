window.onload = () => { //Uncomment out of JSFiddle
$("#hiddentable").show()
$("#logo").css('visibility', 'visible').hide().fadeIn('slow');
$("h3").delay(1000).hide().delay(800).slideDown(600).fadeIn(300);
$("h1").delay(1000).hide().animate({
  width: 'toggle'
}, 500);
$("body").show()
$("h4").delay(2000).fadeTo(300, 1)
$("#otherhiddentable").delay(2000).fadeTo(500, 1)
}; //Uncomment out of JSFiddle

