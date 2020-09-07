/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js

    for below code i have used codeinstitute boutique ado videos to guide me through the process
    while trying to keep it my own project specific

*/


var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1)
var clientSecret = $('#id_client_secret').text().slice(1, -1)
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();


var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};

var card = elements.create('card', { style: style });
card.mount('#card-element');


/* handle validation errors */

// Show the customer the error from Stripe if their card fails to charge

card.AddEvenListener('change', function(event) {
    var errorDiv = document.getElementById('#card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span>${event.error.message}</span> `
    } else {
        errorDiv.textContent = '';
    }
})