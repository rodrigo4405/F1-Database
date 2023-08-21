document.addEventListener('DOMContentLoaded', function() {
    var textbox = document.querySelector('.report-input');

    if (textbox) {
        textbox.addEventListener('keydown', function(event) {
            if (event.key === 'Enter') {
                event.preventDefault();
            }
        });
    }
});