document.addEventListener('DOMContentLoaded', function() {
    var number_input = document.querySelector('input[type="number"]');
    var page_select = document.getElementById("form-1");
    var url = new URL(window.location.href);
    var id = url.searchParams.get("id");
    if (number_input){
        if (id > 2023) {
            id = 2022;
        }

        if (page_select.value === ""){
            var unselected = document.querySelector('.unselected');
            unselected.selected = true;
        }

        var selectedPage = url.searchParams.get("page");
        var option = page_select.querySelector('option[value="' + selectedPage + '"]');

        option.selected = true;

        number_input.value = parseInt(id, 10);
    }
});
