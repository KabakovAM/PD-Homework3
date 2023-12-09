from django.shortcuts import render, get_object_or_404
from Ex007.models import Order, Client, Good

def client_orders(request, client_id):
    goods = {}
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client = client)
    for order in orders:
        goods[order] = order.good.all()
    return render(request, 'Ex007/client_orders.html', {'client': client, 'goods': goods})
