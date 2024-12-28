function toggleSidebar() {
    // console.log('hello people')
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
    var element = document.getElementById('options')
    element.innerHTML += `<input class="form-control mb-2" type="text" name="option" placeholder="Option ${counter()}" aria-label="default input example">`
}