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
        return HttpResponse(content=e, status=400)



    # Handle the event

    handler = StripeWebHookHandler(request)

    event_map = {
        'payment_intent.succeeded': handler.handle_intent_succeeded,
        'payment_intent.payment_failed': handler.handle_intent_failed
    }

    event_type = event['type']

    event_handler = event_map.get(event_type, handler.handle_event)

    response = event_handler(event)
    return response

