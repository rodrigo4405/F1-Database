document.addEventListener('DOMContentLoaded', function() {
    var start = document.querySelector(".start");
    var quiz = document.querySelector(".quiz");
    var time_seconds = 0;
    var time_minutes = 0;
    var timeDisplay = document.getElementById("time");
    var intervalId;

    if (!start) {
        var inputs = document.querySelectorAll("input");
        inputs.forEach(function(input) {
            inputText = input.getAttribute("placeholder");
            input.value = inputText;
            input.setAttribute("placeholder", "");
        });
    }


    if (start) {
        start.addEventListener('click', function(event) {
            start.style.display = 'none';

            setTimeout(function() {
                quiz.style.display = 'block';
                timeDisplay.scrollIntoView();
                intervalId = setInterval(updateTime, 1000);
            }, 500);
        });
    }
        var submitButton = document.getElementById("check-button");

        if (submitButton) {
            submitButton.addEventListener('click', function(event) {
                var time = timeDisplay.textContent;
                localStorage.setItem('time', time);

                var inputValues = {};

                var inputFields = document.querySelectorAll('input[type="text"]');
                inputFields.forEach(function (inputField) {
                    var year = inputField.getAttribute('name');
                    var value = inputField.value;
                    inputValues[year] = value;
                });


               
            });
        }

        var timeResult = document.querySelector(".time-result");

        if (timeResult) {
            var lastTime = localStorage.getItem('time');
            var time = lastTime.split(" : ");
            var minutes = time[0];
            var seconds = time[1];
            if (minutes === "1"){
                timeResult.textContent = minutes + " minute and " + seconds + " seconds";
            }

            else if (minutes === "0") {
                timeResult.textContent = seconds + " seconds";
            }

            else {
                timeResult.textContent = minutes + " minutes and " + seconds + " seconds";
            }
        }


    function updateTime() {
        time_seconds++;
        if (time_seconds === 60) {
            time_seconds = 0;
            time_minutes++;
        }
        if (time_seconds < 10) {
            timeDisplay.textContent = time_minutes + " : 0" + time_seconds;

        }
        else {
            timeDisplay.textContent = time_minutes + " : " + time_seconds;
        }
    }
});
