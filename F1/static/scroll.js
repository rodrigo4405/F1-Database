window.onload = function() {
    var url = new URL(window.location.href);
    var query = url.searchParams.get("query");
    var row = document.getElementById(query);
    if (row) {
        row.scrollIntoView({ behavior: 'smooth' });
        console.log("done");
    }
};
