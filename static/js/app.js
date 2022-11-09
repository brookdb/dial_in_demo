console.log("JS loaded");
var slideIndex = 0;

function showSlides() {
  var i;
  var slides = document.getElementsByClassName("mySlides");
  for (i = 0; i < slides.length; i++) {
    slides[i].style.display = "none";
  }
  slideIndex++;
  if (slideIndex > slides.length) {slideIndex = 1}

  slides[slideIndex-1].style.display = "block";
  setTimeout(showSlides, 6450); // Change image every 2 seconds
}

function toggleMobileMenu(menu) {
    menu.classList.toggle('open');
}

function app(){
  showSlides();
  toggleMobileMenu();
}
app();
