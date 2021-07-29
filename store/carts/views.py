from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart, CartProducts
from .utils import get_or_create_cart
from products.models import Product


def cart(request):
    cart = get_or_create_cart(request)
    return render(request, 'carts/cart.html', {
        'cart':cart
    })

def add(request):
    cart = get_or_create_cart(request) #Obtenemos o creamos el carrito (session o usuario)
    product = get_object_or_404(Product, pk=request.POST.get('product_id')) #Obtenemos el producto que viene en el formulario para agregar al carrito
    quantity = int(request.POST.get('quantity', 1)) #Lo pasamos a numero entero para poder actualizar su valor

    cart_product = CartProducts.objects.create_or_update_quantity(cart=cart,
                                                                    product=product,
                                                                    quantity=quantity) 
    #Como tenemos relacion ManyToMany agregamos el producto al carrito de esta manera. 
    #Agrega objeto product a la relación Cart. Como si Cart fuese una lista para agregar objetos(product)
    #Con through_defaults definimos los atributos que queremos obtener del modelo CartProducts

    return render(request, 'carts/add.html', {
        'product': product,
        'cart_product': cart_product,
        'quantity': quantity
    })

def remove(request):
    cart = get_or_create_cart(request) #Obtenemos o creamos el carrito (session o usuario)
    product = get_object_or_404(Product, pk=request.POST.get('product_id')) #Obtenemos el producto que viene en el formulario para agregar al carrito
    cart.products.remove(product)

    return redirect('carts:cart')