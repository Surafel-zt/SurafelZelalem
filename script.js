function viewassignments() {
    var x = document.getElementById("assignments-container");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}