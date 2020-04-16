let menuElem = document.getElementById('menuid');
let titleElem = menuElem.querySelector('.title');


titleElem.onclick = function() {
    menuElem.classList.toggle('open');
};

menuElem.onclick = function openMenu() {
    menuElem.classList.toggle('active');
}

