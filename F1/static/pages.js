document.addEventListener('DOMContentLoaded', function() {
    var table = document.getElementById("table");
    var next = document.getElementById("next");
    var rows = table.querySelectorAll("tbody tr");
    var numRowsToShow = 17;  
    var currentDisplayIndex = 0;

    function updateRowDisplay() {
        for (var i = 0; i < rows.length; i++) {
            rows[i].style.display = i >= currentDisplayIndex && i < currentDisplayIndex + numRowsToShow ? "table-row" : "none";
        }
    }

    updateRowDisplay();

    next.addEventListener('click', function(event) {
        currentDisplayIndex += numRowsToShow;
        if (currentDisplayIndex >= rows.length) {
            currentDisplayIndex = 0;
        }
        updateRowDisplay();
    });
});
