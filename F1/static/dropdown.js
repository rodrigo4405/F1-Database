document.addEventListener('DOMContentLoaded', function() {
    var dropdownToggle = document.getElementById('navbarDropdown');
    var dropdownMenu = document.querySelector('.dropdown-menu');

    dropdownToggle.addEventListener('click', function(event) {
        event.preventDefault(); 
    });
});
