document.addEventListener("DOMContentLoaded", function() {
    var inputs = document.querySelectorAll("input");
    var start = document.querySelector(".start");


    while (start.style.display === "none") {

    }

    inputs.forEach(function(input) {
        input.addEventListener("input", function(event) {
            var year = event.target.getAttribute("class");
            var correction = document.getElementById("correction-" + year);
            var suggestionP = document.querySelector(".suggestion-" + year);
            var suggestion = document.getElementById("suggestion-" + year);
            var suggested = "";
            var input = event.target.value.trim().toLowerCase();
            if (!drivers.some(driver => driver.toLowerCase() === input) && event.target.value.trim() !== "" && event.target.value.toLowerCase() !== "juan manuel fangio") {
                correction.textContent = "No driver found for " + event.target.value;
                if (event.target.value.includes(" ") || document.activeElement !== event.target) {
                    suggestionP.style.display = "block";
                    for (driver of drivers) {
                        var driverName = driver
                            .replace(/ü/g, 'u')
                            .replace(/ä/g, 'a')
                            .replace(/ë/g, 'e')
                            .replace(/ö/g, 'o')
                            .replace(/ï/g, 'i');


                        if (driverName.startsWith(event.target.value.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ').replace(/ü/g, 'u').replace(/ä/g, 'a').replace(/ë/g, 'e'))) {
                            suggested = driver;
                            break
                        }
                    }
                }

                if (suggested === "") {
                    suggestionP.style.display = "none";
                }

                else {
                    suggestion.textContent = suggested ? " " + suggested : "";
                }
            }

            else {
                correction.textContent = "";
                suggestion.textContent = "";
                suggestionP.style.display = "none";
            }

            suggestion.addEventListener("click", function() {
                event.target.value = suggested;
                correction.textContent = "";
                suggestion.textContent = "";
                suggestionP.style.display = "none";
            });

    //                  ||||||||||||||||||||
    //                  \\  to be fixed V //
    //                   \\              //
    //                    \\            //
    //                     \\          //
    //                      \\        //
    //                       \\      //
    //                        \\    //
    //                         \\  //
//                               V


/*
            var textBox = event.target;

            textBox.addEventListener("keydown", function(event) {
                console.log(suggestion.textContent.length);
                console.log(textBox.value.length + 2);
                console.log(suggestion.textContent.length !== textBox.value.length + 2);
                if (event.key === "Enter" && suggestion.textContent.length !== textBox.value.length + 2) {
                    event.target.value = suggested;
                    correction.textContent = "";
                    suggestion.textContent = "";
                    suggestionP.style.display = "none";
                    console.log("0");
                }

                else if (event.key === "Enter" && suggestion.textContent.length === textBox.value.length + 2) {
                    console.log("1");
                    textBox.value = textBox.value.split(' ').map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(' ');
                }
            });

            */
        });
    });
});