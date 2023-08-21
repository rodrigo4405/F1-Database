document.addEventListener("DOMContentLoaded", function() {
    var next = document.getElementById("next");
    var previous = document.getElementById("previous");
    var pages = {
        "Drivers": "https://library.sportingnews.com/2023-03/GettyImages-1247767495.jpg",
        "Constructors": "https://www.goodwood.com/globalassets/.road--racing/race/historic/2020/4-april/most-successful-f1-teams/nine-most-successful-f1-teams-1-ferrari-f1-2008-barcelona-felipe-massa-ferrari-f2008-rainer-schlegelmilch-motorsport-images-goodwood-24042020.jpg?crop=(0,188,2600,1651)&width=1600",
        "Circuits": "https://maxvelocity.events/wp-content/uploads/2019/04/Circuit-de-Monaco-Monaco.jpg",
        "Seasons": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f0/Ferrari_Formula_1_lineup_at_the_N%C3%BCrburgring.jpg/1024px-Ferrari_Formula_1_lineup_at_the_N%C3%BCrburgring.jpg",
    }
    var categories = ["Drivers", "Constructors", "Circuits", "Seasons"]
    var title = document.querySelector(".homepage-title");
    var current = title.textContent;
    var main = document.querySelector('main');
    var button = document.querySelector(".button-link");
    var link = document.getElementById("image-button");

    next.addEventListener('click', function(event) {
        var currentIndex = categories.indexOf(current);
        var nextIndex = (currentIndex + 1) % categories.length;
        current = categories[nextIndex];
        main.style.backgroundImage = `url('${pages[current]}')`;

        setTimeout(function() {
            title.textContent = current;
            button.textContent = "See all the " + current.toLowerCase();
            link.href = "/" + current.toLowerCase();
        }, 100);
    });

    previous.addEventListener('click', function(event) {
        var currentIndex = categories.indexOf(current);
        var previousIndex = (currentIndex - 1 + categories.length) % categories.length;
        current = categories[previousIndex];
        main.style.backgroundImage = `url('${pages[current]}')`;

        setTimeout(function() {
            title.textContent = current;
        }, 100);
    });
});