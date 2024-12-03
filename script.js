// Функция для показа модального окна
function showModal() {
    document.getElementById('modal').style.display = 'block';
}

// Функция для закрытия модального окна
function closeModal() {
    document.getElementById('modal').style.display = 'none';
}

// Закрытие модального окна при клике вне его содержимого
window.onclick = function(event) {
    if (event.target == document.getElementById('modal')) {
        closeModal();
    }
}
