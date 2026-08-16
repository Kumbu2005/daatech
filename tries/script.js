function showContent(id) {
    document.querySelectorAll(".content").forEach(element => {
        element.style.display = "none";
    });
    document.getElementById(id).style.display = "block";
}