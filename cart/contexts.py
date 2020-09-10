from django.shortcuts import get_object_or_404
from programs.models import Programs

def cart_content(request):
    '''
    return contents of cart across views 
    '''

    cart = request.session.get('cart')
    cart_content = []
    program_count = 1
    

    for program_id, program_quantity in cart.items():
        program = get_object_or_404(Programs, pk=program_id) 
        program_quantity = 1 
        total = program_quantity * program.price

        cart_content.append({
            'program_id': program_id,
            'program': program,
            'program_quantity': program_quantity
        })


    context = {
        'cart_content': cart_content,
        'program_count': program_count,
        'total': total
    }

    return context 