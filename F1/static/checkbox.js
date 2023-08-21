document.addEventListener('DOMContentLoaded', function() {
    var checkbox = document.getElementById("checkbox");
    var table = document.getElementById("table");
    var tab = window.location.pathname;

    var active_drivers = [1, 4, 857, 858, 852, 846, 855, 840, 847, 844, 830, 848, 842, 832, 815, 817, 807, 825, 822, 839];
    var tracks = [3, 77, 1, 73, 79, 21, 6, 4, 7, 70, 9, 11, 13, 39, 14, 15, 22, 78, 69, 32, 18, 80, 24];

    if (checkbox) {
        checkbox.addEventListener('change', function() {
            var rows = table.querySelectorAll("tbody tr");
            rows.forEach(function(row) {
                if (tab === "/drivers") {
                    var td = row.querySelector(":nth-child(1)");
                    var driverId = parseInt(td.textContent);

                    if (active_drivers.includes(driverId)) {
                        row.style.display = checkbox.checked ? "table-row" : "none";
                    } else {
                        row.style.display = "none";
                    }
                }

                else if (tab === "/circuits") {
                    var td = row.querySelector(":nth-child(1)");
                    var trackId = parseInt(td.textContent);
                    console.log(trackId);

                    if (tracks.includes(trackId)) {
                        row.style.display = checkbox.checked ? "table-row" : "none";
                    } else {
                        row.style.display = "none";
                    }
                }

                else if (tab === "/constructors") {
                    var td = row.querySelector(":nth-child(4)");

                    if (td.textContent.startsWith("2023")) {
                        row.style.display = checkbox.checked ? "table-row" : "none";
                    } else {
                        row.style.display = "none";
                    }
                }
            });

            if (!checkbox.checked) {
                rows.forEach(function(row) {
                    row.style.display = "table-row";
                });
            }
        });
    }
});
