
let nav = document.querySelector('.nav')
let menu = document.querySelector('.menu');
let body = document.getElementsByTagName('body')[0];
menu.addEventListener('click', () => {
    nav.classList.toggle('mobile-active');
    body.classList.toggle('nav-active');
});


let mobileNav = document.querySelector('.mobile');
for (let i = 0; i < mobileNav.children[1].querySelectorAll('.dropdown').length; i++) {

    mobileNav.children[1]
        .querySelectorAll('.dropdown')[i]
        .addEventListener('click', () => {
            mobileNav.children[1]
                .querySelectorAll('.dropdown')[i]
                .classList
                .toggle('expanded');
        });

}