function toggleSidebar() {
    var sidebar = document.getElementById('sidebar');
    if (sidebar.style.left === '0px') {
        sidebar.style.left = '-250px';
    } else {
        sidebar.style.left = '0px';
    }
}

function toggleNestedMenu(menuId, element) {
    var nestedMenu = document.getElementById(menuId);
    var icon = element.querySelector('i');
    if (nestedMenu.style.display === 'block') {
        nestedMenu.style.display = 'none';
        icon.classList.replace('fa-chevron-up', 'fa-chevron-down');
    } else {
        nestedMenu.style.display = 'block';
        icon.classList.replace('fa-chevron-down', 'fa-chevron-up');
    }
}

function openClassMenuModal() {
    $('#classMenuModal').modal('show');
    console.log('clicked');
}

function createCounter() {
    
    let count = 0; // This acts like a static variable

    return function() {
        count++;
        return count;
    }
}

const counter = createCounter();

function addOptions()
{
    var count = counter()
    var element = document.getElementById('options')
    element.innerHTML += `<input class="form-control mb-2" type="text" name="option" placeholder="Option ${count}" aria-label="default input example">`
    element = document.getElementById('answer')
    element.innerHTML += `<option value="${count}">${count}</option>`
}

document.addEventListener("DOMContentLoaded", function(event) {
   
    const showNavbar = (toggleId, navId, bodyId, headerId) =>{
    const toggle = document.getElementById(toggleId),
    nav = document.getElementById(navId),
    bodypd = document.getElementById(bodyId),
    headerpd = document.getElementById(headerId)

    // Validate that all variables exist
    if(toggle && nav && bodypd && headerpd){
        toggle.addEventListener('click', ()=>{
            // show navbar
            nav.classList.toggle('show')
            // change icon
            toggle.classList.toggle('bx-x')
            // add padding to body
            bodypd.classList.toggle('body-pd')
            // add padding to header
            headerpd.classList.toggle('body-pd')
        })
    }
    }

    showNavbar('header-toggle','nav-bar','body-pd','header')

    /*===== LINK ACTIVE =====*/
    const linkColor = document.querySelectorAll('.nav_link')

    function colorLink(){
        if(linkColor){
            linkColor.forEach(l=> l.classList.remove('active'))
            this.classList.add('active')
        }
    }
    linkColor.forEach(l=> l.addEventListener('click', colorLink))

    // Your code to run since DOM is loaded and ready
});