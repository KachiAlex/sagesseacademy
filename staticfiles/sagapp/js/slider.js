
var slides = document.querySelectorAll('.slide');
var btns = document.querySelectorAll('.slbtn');
let currentSlide = 1;

//Manual Slider control
var manualNav = function (manual) {
    slides.forEach((slide) => {
        slide.classList.remove('active');

        btns.forEach((slbtn) => {
            slbtn.classList.remove('active');
        });
    });

    slides[manual].classList.add('active');
    btns[manual].classList.add('active');
}

btns.forEach((slbtn, i) => {
    slbtn.addEventListener("click", () => {
        manualNav(i);
    });
});

// Auto slide
var repeat = function (activeClass) {
    let active = document.getElementsByClassName('active');
    let i = 1;

    var repeater = () => {
        setTimeout(function () {
            [...active].forEach((activeSlide) => {
                activeSlide.classList.remove('active')
            });

            slides[i].classList.add('active');
            btns[i].classList.add('active');
            i++;

            if (slides.length == i) {
                i = 0;
            }
            if (i >= slides.length) {
                return;
            }
            repeater();
        }, 9000);
    }
    repeater();
}
repeat();