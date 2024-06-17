
document.addEventListener('DOMContentLoaded', function () {
    const buyModal = document.getElementById('buyModal');
    const idProductHidden = document.getElementById('id_product_hidden');
    const productPrice = document.getElementById('product_price');
    const totalSaleInput = document.getElementById('total_sale');
    const piecesInput = document.getElementById('pieces');
    const productDescription = document.getElementById('product-description');
    const useExistingAddressCheckbox = document.getElementById('use_existing_address');
    const newAddressGroup = document.getElementById('new_address_group');
    const existingAddressGroup = document.getElementById('existing_address_group');

    $('#buyModal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget);
        const productId = button.data('product-id');
        const productName = button.data('product-name');
        const productPriceValue = button.data('product-price');
        const productDescriptionValue = button.data('product-description');

        const modal = $(this);
        modal.find('.modal-title').text('Comprar ' + productName);
        productDescription.textContent = productDescriptionValue;
        idProductHidden.value = productId;
        productPrice.textContent = productPriceValue;
        calculateTotal();
        document.getElementById('product_name_hidden').value = productName;
    });

    piecesInput.addEventListener('input', function () {
        calculateTotal();
    });

    useExistingAddressCheckbox.addEventListener('change', function () {
        if (useExistingAddressCheckbox.checked) {
            existingAddressGroup.style.display = 'block';
            newAddressGroup.style.display = 'none';
        } else {
            existingAddressGroup.style.display = 'none';
            newAddressGroup.style.display = 'block';
        }
    });

    function calculateTotal() {
        const price = parseFloat(productPrice.textContent);
        const pieces = parseFloat(piecesInput.value);

        if (!isNaN(price) && !isNaN(pieces)) {
            const total = price * pieces;
            totalSaleInput.value = total.toFixed(2);
        }
    }
});
