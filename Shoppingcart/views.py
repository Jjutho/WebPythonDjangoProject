from decimal import Decimal
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import PaymentForm
from .models import ShoppingCart, ShoppingCartItem


def show_shopping_cart(request):
    if request.method == 'POST':
        if 'empty' in request.POST:
            ShoppingCart.objects.get(myuser=request.user).delete()

            context = {'shopping_cart_is_empty': True,
                       'shopping_cart_items': None,
                       'amount': 0.0}
            return render(request, 'shopping-cart.html', context)

        elif 'pay' in request.POST:
            return redirect('shopping-cart-pay')

    else:  # request.method == 'GET'
        shopping_cart_is_empty = True
        shopping_cart_items = None
        total = Decimal(0.0)  # Default without Decimal() would be type float!

        myuser = request.user
        if myuser.is_authenticated:
            shopping_carts = ShoppingCart.objects.filter(myuser=myuser)
            if shopping_carts:
                shopping_cart = shopping_carts.first()
                shopping_cart_is_empty = False
                shopping_cart_items = ShoppingCartItem.objects.filter(shopping_cart=shopping_cart)
                total = shopping_cart.get_total()

        context = {'shopping_cart_is_empty': shopping_cart_is_empty,
                   'shopping_cart_items': shopping_cart_items,
                   'total': total}
        return render(request, 'shopping-cart.html', context)


@login_required(login_url='/useradmin/login/')
def pay(request):
    shopping_cart_is_empty = True
    paid = False
    form = None

    if request.method == 'POST':
        myuser = request.user
        form = PaymentForm(request.POST)
        form.instance.myuser = myuser
        if form.is_valid():
            form.save()
            paid = True

            # Empty the shopping cart
            ShoppingCart.objects.get(myuser=myuser).delete()
        else:
            print(form.errors)

    else:  # request.method == 'GET'
        shopping_carts = ShoppingCart.objects.filter(myuser=request.user)
        if shopping_carts:
            shopping_cart = shopping_carts.first()
            shopping_cart_is_empty = False
            form = PaymentForm(initial={'amount': shopping_cart.get_total()})

    context = {'shopping_cart_is_empty': shopping_cart_is_empty,
               'payment_form': form,
               'paid': paid,}
    return render(request, 'pay.html', context)