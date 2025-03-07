function toggleMenu() {
    const menu = document.querySelector('.navbar .menu');
    menu.classList.toggle('active');
}

const  btnClick = document.querySelector('.btnbs');

function btnAlert() {
    alert('Button is not Active')
btnClick.addEventListener('click',btnAlert);
}
