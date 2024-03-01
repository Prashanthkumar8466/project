document.addEventListener('DOMContentLoaded', function () {
    const openCartMenu = document.querySelector('#burger');
    const closeCartMenu = document.querySelector('#burger1');
    const sideMenuBar = document.querySelector('#sidemenubar');
    let cartOpen = false;
    openCartMenu.addEventListener('click', () => {
        sideMenuBar.style.width = '75%';

    });

    closeCartMenu.addEventListener('click', () => {
        sideMenuBar.style.width = '0%';
    });
});