document.addEventListener('DOMContentLoaded', function () {
    const themeOptions = document.querySelectorAll('.theme-option');
    const body = document.body;

    themeOptions.forEach((option) => {
        option.addEventListener('click', function () {
            const theme = option.getAttribute('data-theme');

            if (theme === 'dark') {
                body.classList.add('dark-theme');
            } else {
                body.classList.remove('dark-theme');
            }
        });
    });
});
