

let index = 0;
const slides = document.querySelector('.slides');
const totalSlides = document.querySelectorAll('.slides img').length;
const thumbnails = document.querySelectorAll('.thumbnails img');

document.querySelector('.next').addEventListener('click', () => {
  index = (index + 1) % totalSlides;
  updateCarousel();
});

document.querySelector('.prev').addEventListener('click', () => {
  index = (index - 1 + totalSlides) % totalSlides;
  updateCarousel();
});

thumbnails.forEach((thumbnail, i) => {
  thumbnail.addEventListener('click', () => {
    index = i;
    updateCarousel();
  });
});

function updateCarousel() {
  const width = slides.clientWidth;
  slides.style.transform = `translateX(${-index * width}px)`;

  // Обновляем активное состояние миниатюр
  thumbnails.forEach((thumbnail, i) => {
    if (i === index) {
      thumbnail.classList.add('active');
    } else {
      thumbnail.classList.remove('active');
    }
  });
}

// Устанавливаем первую миниатюру как активную
thumbnails[0].classList.add('active');




