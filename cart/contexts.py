from django.shortcuts import get_object_or_404
from programs.models import Programs

def cart_content(request):
    '''
    return contents of cart across views 
    '''
    cart_content = []
    program_count = 1
    total = 0
    cart = request.session.get('cart', {})
    

    for program_id, program_data in cart.items():
        program = get_object_or_404(Programs, pk=program_id) 
        program_quantity = program_data 
        total += program_quantity * program.price

        cart_content.append({
            'program_id': program_id,
            'program': program,
            'program_quantity': program_quantity,
        })


    context = {
        'cart_content': cart_content,
        'program_count': program_count,
        'total': total
    }

    return context 