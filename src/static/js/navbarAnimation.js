// var elements = document.querySelectorAll('.header-section .header-bottom .container .main-menu li a');

const tl = gsap.timeline();

tl.from('.header-info', {
    duration: 1,
    delay: 0.9,
    stagger: 0.2,
    x: 500,
    opacity: 0,
    ease: 'power3.inOut'
}, 'test')
tl.from('.header-bottom a', {
    duration: 1,
    delay: 0.9,
    x: 500,
    stagger: 0.2,
    opacity: 0,
    ease: 'power3.inOut'
}, 'test')
tl.from('#infor-switch', {
    x: 100,
    opacity: 0,
    ease: 'power3.inOut'
})