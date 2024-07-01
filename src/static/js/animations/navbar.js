const tl = gsap.timeline();

tl.from('.header-info', {
    duration: 1,
    delay: 0.9,
    stagger: 0.2,
    x: 500,
    opacity: 0,
    ease: 'power3.inOut'
}, 'sameTimeAnimation')

tl.from('.header-bottom a', {
    duration: 1,
    delay: 0.9,
    x: 500,
    stagger: 0.2,
    opacity: 0,
    ease: 'power3.inOut'
}, 'sameTimeAnimation')

tl.from('#infor-switch', {
    x: 100,
    opacity: 0,
    ease: 'power3.inOut'
})