from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from datetime import timedelta
from Ex008.models import Order, Client, Good

def client_orders_by_time(request, client_id):
    goods = {7:[], 30:[], 365:[]}
    client = get_object_or_404(Client, pk=client_id)
    orders_7 = Order.objects.filter(client = client).filter(reg_data__gte = timezone.now().date() - timedelta(days=7))
    orders_30 = Order.objects.filter(client = client).filter(reg_data__gte = timezone.now().date() - timedelta(days=30))
    orders_365 = Order.objects.filter(client = client).filter(reg_data__gte = timezone.now().date() - timedelta(days=365))
    for order in orders_7:
        goods[7] = order.good.all()
    for order in orders_30:
        goods[30] = order.good.all()
    for order in orders_365:
        goods[365] = order.good.all()
    return render(request, 'Ex007/client_orders.html', {'client': client, 'goods': goods})
