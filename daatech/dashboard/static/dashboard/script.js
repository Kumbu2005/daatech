function showContent(id) {
    document.querySelectorAll(".content").forEach(element => {
        element.style.display = "none";
    });
    document.getElementById(id).style.display = "block";
}

const popup = document.getElementById("popup");
const openPopup = document.getElementById("openPopup");
const closePopup = document.getElementById("closePopup");

openPopup.addEventListener("click", function() {
    popup.style.display = "flex";
});

closePopup.addEventListener("click", function() {
    popup.style.display = "none";
});