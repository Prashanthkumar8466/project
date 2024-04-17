var vaccumbtn = document.querySelector('#Vaccum');
var Designbtn = document.querySelector('#Design');
var Hexacopterbtn = document.querySelector('#Hexacopter');
var Vaccumcontent = document.querySelector('#Vaccum-content');
var Designcontent = document.querySelector('#Design-content');
var Hexacoptercontent = document.querySelector('#Hexacopter-content');
var closebtn = document.querySelector('#close');
var Designclosebtn = document.querySelector('#Designclose');
var Hexacopterclosebtn = document.querySelector('#Hexacopterclose');
vaccumbtn.addEventListener('click', () => {
    Hexacoptercontent.style.display = 'none';
    Designcontent.style.display = 'none';
    Vaccumcontent.style.display = 'block';  
});
Designbtn.addEventListener('click', () => {
    Vaccumcontent.style.display = 'none';
    Designcontent.style.display = 'block';
    Hexacoptercontent.style.display = 'none';
});
Hexacopterbtn.addEventListener('click', () => {
    Vaccumcontent.style.display = 'none';
    Hexacoptercontent.style.display = 'block';
    Designcontent.style.display = 'none';
});
closebtn.addEventListener('click', () => {
    Vaccumcontent.style.display = 'none';  
});
Designclosebtn.addEventListener('click', () => { 
    Designcontent.style.display = 'none';
});
Hexacopterclosebtn.addEventListener('click', () => { 
    Hexacoptercontent.style.display = 'none';
});