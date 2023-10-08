from datetime import datetime, timedelta

from django.shortcuts import render
from .models import Client, Order


def basket(request, user_id):
    goods = []
    client = Client.objects.filter(pk=user_id).first()
    orders = Order.objects.filter(customer=client).all()
    for order in orders:
        goods.append(order.products.all())
    goods.reverse()
    return render(request, 'internet_shop/client_orders.html', {'client': client, 'orders': orders, 'goods': goods})


def sorted_basket(request, client_id, days_ago):
    goods = []
    now = datetime.now()
    before = now - timedelta(days=days_ago)
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client, creat_at=(before, now)).all()
    for order in orders:
        goods = order.goods_id.all()
        for good in goods:
            if good not in goods:
                goods.append(good)

    return render(request, 'internet_shop/client_date_orders.html', {'client': client, 'goods': goods, 'days': days_ago})
