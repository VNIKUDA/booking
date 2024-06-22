document.addEventListener('DOMContentLoaded', function () {
    const bookingForm = document.getElementById('bookingForm');

    bookingForm.addEventListener('submit', function (event) {
        event.preventDefault();

        // Очистка повідомлень про помилки
        const formControls = bookingForm.querySelectorAll('.form-control');
        formControls.forEach(control => {
            control.classList.remove('is-invalid');
            control.classList.remove('is-valid');
        });

        // Перевірка валідності полів
        let formIsValid = true;
        formControls.forEach(control => {
            if (control.value === '') {
                control.classList.add('is-invalid');
                formIsValid = false;
            } else {
                control.classList.add('is-valid');
            }
        });

        if (formIsValid) {
            bookingForm.submit();
        } else {
            // Відображення повідомлення про помилки
            alert('Please fill in all required fields.');
        }
    });
});
