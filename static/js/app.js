console.log("JS loaded");
function showOptions() {
  const burger = document.querySelector('.burger');
  const nav = document.querySelector('nav');
  console.log(nav);

  burger.addEventListener('click', function(){
        burger.classList.toggle('change');
        nav.classList.toggle('show-nav');
        console.log('event triggered');
    });
}

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


function app(){

  showOptions();
  showSlides();
}
app();
