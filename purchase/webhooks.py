from django.http import HttpResponse
from django.conf import settings
from purchase.webhook_handler import StripeWebHookHandler
import stripe
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


@require_POST
@csrf_exempt
def webhook(request):
    """
    Listen to webhooks 
    """
    stripe.api_key = settings.STRIPE_SECRET_KEY
    endpoint_secret = settings.STRIPE_ENDPOINT_KEY

    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
        payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        # Invalid payload
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        # Invalid signature
        return HttpResponse(status=400)
    except Exception as e:
        return HttpResponse(contetn=e, status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        payment_intent = event.data.object # contains a stripe.PaymentIntent
        print('PaymentIntent was successful!')
    elif event.type == 'payment_method.attached':
        payment_method = event.data.object # contains a stripe.PaymentMethod
        print('PaymentMethod was attached to a Customer!')
    # ... handle other event types
    else:
        # Unexpected event type
        return HttpResponse(status=400)

    

    print('Success!')
    return HttpResponse(status=200)
