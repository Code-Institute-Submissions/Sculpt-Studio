from django.http import HttpResponse

"""
Code Institute boutique ado video used to support in implementing webhook handler
"""
class StripeWebHookHandler:
    """
    Handle stripe webhooks
    """
    def __init__(self, request):
        self.request = request


    def handle_event(self, event):
        """
        handle webhook event
        """
        return HttpResponse(
            content = f'Webhook received: {event:['type']}',
            status = 200)
