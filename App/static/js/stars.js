
document.addEventListener("DOMContentLoaded", function () {
    const stars = document.querySelectorAll('#rating-stars .fa-star');
    const ratingInput = document.getElementById('rating_product');

    stars.forEach(star => {
        star.addEventListener('click', function () {
            const ratingValue = this.getAttribute('data-value');
            ratingInput.value = ratingValue;

            // Reset all stars
            stars.forEach(s => s.classList.remove('checked'));

            // Highlight selected stars
            for (let i = 0; i < ratingValue; i++) {
                stars[i].classList.add('checked');
            }
        });
    });
});
