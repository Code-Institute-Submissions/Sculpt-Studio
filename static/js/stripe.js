var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1)
var clientSecret = $('#id_client_secret').text().slice(1, -1)
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();


var style = {
    base: {
        color: "#32325d",
        fontFamily: 'Arial, sans-serif',
        fontSmoothing: "antialiased",
        fontSize: "16px",
        "::placeholder": {}
    },
    invalid: {
        fontFamily: 'Arial, sans-serif',
        color: "#fa755a",
    }
};

var card = elements.create("card", { style: style });
// Stripe injects an iframe into the DOM
card.mount("#card-element");


var form = document.getElementById("payment-form");
form.addEventListener("submit", function(event) {
    event.preventDefault();
    // Complete payment when the submit button is clicked
    payWithCard(stripe, card, data.clientSecret);
});

var payWithCard = function(stripe, card, clientSecret) {
    loading(true);
    stripe
        .confirmCardPayment(clientSecret, {
            payment_method: {
                card: card
            }
        })
        .then(function(result) {
            if (result.error) {
                // Show error to your customer
                showError(result.error.message);
            } else {
                // The payment succeeded!
                orderComplete(result.paymentIntent.id);
            }
        });
};