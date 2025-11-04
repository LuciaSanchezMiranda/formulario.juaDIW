// Animación de entrada del formulario
const formCard = document.getElementById('form-card');
window.addEventListener('load', () => {
    formCard.classList.remove('opacity-0', 'translate-y-10');
    formCard.classList.add('opacity-100', 'translate-y-0');
});

// Flash messages que se desvanecen
const flashMessages = document.querySelectorAll('.flash-message');
flashMessages.forEach(msg => {
    setTimeout(() => {
        msg.style.transition = 'opacity 1s ease';
        msg.style.opacity = '0';
    }, 3000); // se desvanece después de 3s
});

// Animación de clic en el botón
const btn = document.getElementById('submit-btn');
btn.addEventListener('mousedown', () => {
    btn.style.transform = 'scale(0.95)';
});
btn.addEventListener('mouseup', () => {
    btn.style.transform = 'scale(1)';
});
