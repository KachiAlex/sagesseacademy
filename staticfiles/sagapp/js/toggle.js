var navSect = document.querySelector('#topnav');
var buttonclik = document.querySelector('.navbutton');
var xmenu = document.querySelector('#transmenu');


buttonclik.addEventListener('click', megamic);

function megamic(){
    if(navSect.classList.contains('toggled')){
        navSect.classList.remove('toggled');
        xmenu.classList.add('change');
    }
    else{
        navSect.classList.add('toggled');
        xmenu.classList.remove('change');
    }
};



