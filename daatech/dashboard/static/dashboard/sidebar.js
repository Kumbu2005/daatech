const toggleButton = document.getElementById('toggle-btn')
const sidebar = document.getElementById('sidebar')
const accountBtn = document.getElementsByClassName('accountBtn')

function toggleSideBar(){
    sidebar.classList.toggle('close')
    toggleButton.classList.toggle('rotate')
}

function toggleActive(){
    sidebar.classList.toggle('active')
}
function showContent(id) {
    document.querySelectorAll(".content").forEach(element => {
        element.style.display = "none";
    });
    document.getElementById(id).style.display = "block";
    accountBtn.classList.toggle('account-btn-active')
}