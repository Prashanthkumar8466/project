document.addEventListener('DOMContentLoaded', function () {
    const openCartMenu = document.querySelector('#burger');
    const closeCartMenu = document.querySelector('#burger1');
    const sideMenuBar = document.querySelector('#sidemenubar');
    const body = document.body;
    let cartOpen =false;
    openCartMenu.addEventListener('click', () => {
        sideMenuBar.style.width = '85%';
        body.style.overflow = 'hidden';
        html.style.overflow = 'hidden'; 
        cartOpen = true;
    });

    closeCartMenu.addEventListener('click', () => {
        sideMenuBar.style.width = '0%';
        body.style.overflow = 'auto';
        html.style.overflow = 'auto'; 
        cartOpen = false;
    });
});