import json
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from pages.models import *
from .models import *
from .forms import *

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ви успішно створили новий аккаунт, саме час увійти')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    pages = Page.objects.all()
    return render(request, "users/register.html", {'form':form, "pages":pages})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            name = request.POST['username']
            pas = request.POST['password']
            user = auth.authenticate(username=name,password=pas)
            if user:
                auth.login(request,user)
                return HttpResponseRedirect(reverse('pages:index'))
    else:
        form = UserLoginForm()

    pages = Page.objects.all()
    context = {"form":form, "pages":pages}
    return render(request, "users/login.html",context)

@login_required
def single(request):
    if request.method == 'POST':
        form = UserCangeDataForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:single'))
    else:
        form = UserCangeDataForm(instance=request.user)
    return render(request, "users/single.html", {'form':form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('pages:index'))


def basket(request):
    pages = Page.objects.all()
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user,in_progress=False)

        return render(request, "users/basket.html", {'baskets': baskets, "pages":pages})
    else:
        baskett = request.COOKIES.get('baskets')
        if baskett:
            baskets = json.loads(baskett)
        else:
            baskets = {}
        total_sum = 0
        content = []
        for i in baskets:
            col,size,color = i.split(".")
            products=Product.objects.get(id=int(col))
            quantity = baskets[i]
            if products.sale:
                prise = products.prise_on_sale
            else:
                prise = products.price
            sum = prise*quantity
            total_sum += sum
            content.append({"product":products,"quantity":quantity,"price":prise,"sum":sum,
                            'size':size,'color':color})


        return render(request, "users/basket.html", {'baskets': content,"total_sum":total_sum, "pages":pages})
