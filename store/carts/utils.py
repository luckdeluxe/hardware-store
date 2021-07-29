from .models import Cart

def get_or_create_cart(request):
    """Consultamos si la session tiene un usuario identificado, caso contrario guardamos None.
        Si la session ya posé un carro, lo retornamos de la DB. Caso contrario creamos uno."""
    if request.user.is_authenticated: #Si hay usuario identificado guardarlo en la variable user, en caso contrario guardar None
        user = request.user
    else:
        user = None
  
    cart_id = request.session.get('cart_id')  #Buscamos el ID del carrito mediante la session
    cart = Cart.objects.filter(cart_id=cart_id).first() #Buscamos en la DB el ID del carrito de la session (si es que existe)
    
    if cart is None: # Si la busqueda anterior da como resultado None, creamos uno y se lo asignamos al user (en caso de estar authenticado)
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()

    request.session['cart_id'] = cart.cart_id #Agregamos al dict session el cart_id que acabamos de crear en la instancia ' cart'

    return cart