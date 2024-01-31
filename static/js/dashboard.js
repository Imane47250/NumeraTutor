document.addEventListener('DOMContentLoaded', function() {
    const bookButtons = document.querySelectorAll('.book-button');
    const paymentForm = document.getElementById('payment-form');

    // Add click event listeners to the "Book" buttons
    bookButtons.forEach(button => {
        button.addEventListener('click', function() {
            const packageSize = this.getAttribute('data-package');
            
            // Display the payment form with the selected package size
            paymentForm.innerHTML = `
                <h2>Payment for Package ${packageSize} Courses</h2>
                <!-- Payment form elements go here (e.g., credit card input) -->
                <button id="submit-payment">Submit Payment</button>
            `;

            // Handle the payment form submission
            const submitButton = document.getElementById('submit-payment');
            submitButton.addEventListener('click', function() {
                // Handle payment processing and confirmation (e.g., with a payment gateway)
                // Once payment is successful, you can display a confirmation message
                alert(`Payment for Package ${packageSize} Courses successful!`);
                // You can also redirect the user to a confirmation page or update their account accordingly
            });
        });
    });
});
