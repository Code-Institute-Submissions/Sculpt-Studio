

def cart_content(request):
    '''
    return contents of cart across views 
    '''

    cart_content = []
    total_cost = 0

    context = {
        'cart_content': cart_content,
        'total_cost': total_cost,
    }

    return context 