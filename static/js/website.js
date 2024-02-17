
const openCartmenu =document.querySelector('#burger')
const closeCartmenu =document.querySelector('#burger1')
const sideMenuBar =document.querySelector('#sidemenubar')
let cartopen=false;
openCartmenu.addEventListener ('click',()=>{
    sideMenuBar.style.width='75%';    
})
closeCartmenu.addEventListener("click",()=>{
    sideMenuBar.style.width='0%';
})
// slide image
let slideIndex=0;
const slides = document.querySelectorAll('.slide');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

function Slideshow(n){
    if(n>=slides.length){
        slideIndex =0;

    }else if (n<0){
        slideIndex=slides.length - 1;
    }
    slides.forEach((slide)=>{
        slide.style.display ="none";
    });
    slides[slideIndex].style.display="block";

}
function nxtslide(){
    slideIndex++;
    Slideshow(slideIndex);
}
prevBtn.addEventListener('click',()=>{
    slideIndex--;
    Slideshow(slideIndex);
});
nextBtn.addEventListener('click',nxtslide);
function autoslide(){
    nxtslide();
    setTimeout(autoslide,3000)
}
autoslide();
Slideshow(slideIndex);