from django.shortcuts import render, redirect

from .models import ChickenPart, Customer
from .forms import CustomerForm


def customer_info(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            request.session['customer_id'] = customer.id
            return redirect('menu')
    else:
        form = CustomerForm()
    return render(request, 'orders/customer_info.html', {'form': form})

def menu(request):
    parts = ChickenPart.objects.order_by('name')
    return render(request, 'orders/menu.html', {'parts': parts})