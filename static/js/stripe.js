/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js

    for below code i have used codeinstitute boutique ado videos to guide me through the process of setting up stripe
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


// handle validation errors


card.addEventListener('change', function(event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-exclamation-circle"></i>
            </span>
            <span>${event.error.message}</span> `
        $(errorDiv).html(html)
        card.update({ 'disabled': false });
        $().attr('disabled', false)
    } else {
        errorDiv.textContent = '';
    }
})

// handling form submit

var form = document.getElementById("payment-form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    card.update({ 'disabled': true });
    $().attr('disabled', true);
    $('#submit-btn').attr('disabled', true);
    $('#payment-form').toggle();
    $('.payment-loading').toggle();
    // Complete payment when the submit button is clicked
    payWithCard(stripe, card, clientSecret);
});

// Calls stripe.confirmCardPayment
// If the card requires authentication Stripe shows a pop-up modal to
// prompt the user to enter authentication details without leaving your page.
var payWithCard = function(stripe, card, clientSecret) {
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card
        }
    }).then(function(result) {
        if (result.error) {
            var errorDiv = document.getElementById('card-errors');
            if (error) {
                var html = `
                        <span class="icon" role="alert">
                            <i class="fas fa-exclamation-circle"></i>
                        </span>
                        <span>${error.message}</span> `
                $(errorDiv).html(html)
                card.update({ 'disabled': false });
                $('#submit-btn').attr('disabled', false);
                $('#payment-form').toggle();
                $('.payment-loading').toggle();
            } else {
                errorDiv.textContent = '';
            }
            showError(result.error.message);
        } else {
            form.submit();
        }
    });
};