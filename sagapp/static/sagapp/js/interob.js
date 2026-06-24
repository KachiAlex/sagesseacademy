const sectionOne = document.querySelector(".partevents");

const options = {
    root: null,
    threshold: 1,
    rootMargin: "1px"
};

const observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (!entry.isIntersecting) {
            return;
        };
        entry.target.classList.toggle("partevents1set");
        console.log(entry.target)
    })
}, options);

observer.observe(sectionOne);