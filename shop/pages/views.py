from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from .models import *
import json
import requests
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib import auth
from users.models import User

def index(request):
    # if request.user.is_authenticated:
    #     backet = Basket.objects.filter(user=request.user)
    # else:
    co = Product.objects.filter(visible=True).count() -4
    if co < 0:
        news = Product.objects.filter(visible=True)[:]
    else:
        news = Product.objects.filter(visible=True)[co:]
    backet = Basket.objects.all()

    content = {
        'sales':ActionCatogory.objects.first(),
        'baskets': backet,
        'cats' : Subcategories.objects.all(),
        'products' : Product.objects.filter(visible=True) ,
        'news' : news,
        'pages' : Page.objects.all()
    }

    return render(request, "pages/main2.html",content)

def category_view(request,slug):
    cat = Subcategories.objects.get(slug=slug)
    products = Product.objects.filter(subcategory=cat,visible=True)
    # cats = Subcategories.objects.all()
    pages = Page.objects.all()
    return render(request, "pages/cats.html",{'cat':cat, 'products':products,"pages":pages})


def sales(request):
    pages = Page.objects.all()
    products = Product.objects.filter(sale=True,visible=True)
    cat = ActionCatogory.objects.first()
    return render(request, "pages/cats.html", {'cat':cat, 'products':products,"pages":pages})

def pages(request, page_slug):
    pages = Page.objects.all()
    return render(request, "pages/page.html",{"page":Page.objects.get(slug=page_slug),'pages':pages})





def single(request, slug_prod=None):

    product = Product.objects.get(slug=slug_prod)
    photos = Photos.objects.filter(parent=product)
    co = Product.objects.filter(visible=True).count() - 8
    if co < 0:
        news = Product.objects.filter(visible=True)[:]
    else:
        news = Product.objects.filter(visible=True)[co:]
    coms = Comments.objects.filter(product=product)
    con_num = coms.count()
    cat = Subcategories.objects.get(slug=product.subcategory)

    if request.method == "POST" and request.user.is_authenticated:
        Comments.objects.create(user=request.user, product=product, comment=request.POST['comment'])
        return HttpResponseRedirect(reverse('pages:single', kwargs={'slug_prod': product.slug}))
    size = []
    if product.size:
        size = product.size.split(",")

    color = []
    if product.color:
        color = product.color.split(",")


    formCom = CommentCreateForm()
    pages = Page.objects.all()
    return render(request, "pages/single2.html", {'cat': cat, 'product': product,'news':news,
                                                  'coms':coms,"formCom":formCom,'photos':photos,
                                                  'con_num':con_num, "pages":pages, 'size':size,
                                                  "color":color})


def add_to_basket(request, product_id):
    product = Product.objects.get(id=product_id)
    if product.visible:
        size = request.POST.get('size')
        color = request.POST.get('color')

        quantity = int(request.POST.get('quantity', 1))
        if request.user.is_authenticated:
            baskets = Basket.objects.filter(user=request.user, product=product, size=size, color=color)
        else:

            basket = request.COOKIES.get('baskets', '{}')
            baskets = json.loads(basket)
            query = f'{product_id}.{size}.{color}'
            if query in baskets:
                baskets[query] += quantity
            else:
                baskets[query] = quantity
            baskets = json.dumps(baskets)
            response = HttpResponseRedirect(request.META['HTTP_REFERER'])
            response.set_cookie('baskets', baskets, max_age=2419200)
            return response

        if not baskets.exists():
            Basket.objects.create(user=request.user, product=product, quantity=quantity, size=size, color=color)
        else:
            baskets = baskets.first()
            baskets.quantity += quantity
            baskets.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def thanks(request):
    si = None
    if request.method == "POST":
        si = True

        if request.user.is_authenticated:
            baskets = Basket.objects.filter(user=request.user,in_progress=False)
            order = Order.objects.create(name=request.POST['name'], surname=request.POST['surname'],
                                         phone=request.POST['phone'], svaluedesteny=request.POST['sd'],
                                         city=request.POST['city'], adress=request.POST['adress'],
                                         message=request.POST['message-message'], total_sum=baskets.total_sum())

            requests.get(
                f'https://api.telegram.org/bot610в5819:AAвE_DчdIMVPа2аMWyоMМ30Pvbrнnxт0SpLm6QреAz0/sendMessage?chat_id=-9244880055535350125&text=Новый заказ\n{order.id}')

            if baskets:
                for i in baskets:
                    OrderBasket.objects.create(order=order,product=i.product,size=i.size,color=i.color,quantity=i.quantity)
                    # i.in_progress = True
                    i.delete()
        else:

            basket = request.COOKIES.get('baskets', '{}')
            baskets = json.loads(basket)
            order = Order.objects.create(name=request.POST['name'], surname=request.POST['surname'],
                                         phone=request.POST['phone'], svaluedesteny=request.POST['sd'],
                                         city=request.POST['city'], adress=request.POST['adress'],
                                         message=request.POST['message-message'], total_sum=0)
            requests.get(
                f'https://api.telegram.org/bot610в5819:AAвE_DчdIMVPа2аMWyоMМ30Pvbrнnxт0SpLm6QреAz0/sendMessage?chat_id=-9244880055535350125&text=Новый заказ\n{order.id}')

            s = 0
            for i in baskets:
                prod = Product.objects.get(id=i.split('.')[0])
                OrderBasket.objects.create(order=order, product=prod, size=i.split('.')[1], color=i.split('.')[2],
                                           quantity=baskets[i])
                s += (prod.prise_on_sale if prod.sale else prod.price) * baskets[i]
                # i.in_progress = True
            order.total_sum = s
            order.save()

            response = render(request, "pages/thanks.html",{"si":si})
            response.set_cookie('baskets', '', max_age=0)
            return response




    return render(request, "pages/thanks.html",{"si":si})

def remove_basket(request, basket_id, prod_id, size, color):
    if request.user.is_authenticated:

        basket = Basket.objects.get(id=basket_id)
        basket.delete()
        return HttpResponseRedirect(request.META['HTTP_REFERER'])
    else:
        basket = request.COOKIES.get('baskets', '{}')
        baskets = json.loads(basket)

        # Удаляем товар, если он есть в корзине
        query = f'{prod_id}.{size}.{color}'
        if query in baskets:
            del baskets[query]

        # Если корзина не пуста, обновляем cookie
        baskets = json.dumps(baskets)
        response = HttpResponseRedirect(request.META['HTTP_REFERER'])
        response.set_cookie('baskets', baskets, max_age=2419200)
        return response

