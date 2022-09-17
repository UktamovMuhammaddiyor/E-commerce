from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json
from .credientals import TOKEN, URL, BOT_API
import requests
# Create your views here.
@csrf_exempt
def get_post(request):

    return HttpResponse('salom')
def jonat(request):
    sh = shopitem.objects.all()
    a = []
    for i in sh:
        a.append(f'{i.product.subcategory.category.name} dan.{i.product.name}ni {i.quantity} ta {i.total}')
    request_to_bot('sendMessage', {
        'chat_id': 1618456770,
        'text': f"{a} | {request.user} dan {i.sho.total} narxga buyurtma qildi"
    })
    return redirect('index')
@require_http_methods(['GET', 'POST'])
def setwebhook(request):
    response = requests.post(BOT_API + 'setWebhook?url=' + URL).json()
    return HttpResponse(f'{response}')
def request_to_bot(type, data):
    return requests.post(BOT_API + type, data)
def index(request):
    ext = Closes.objects.all()
    cats = Category.objects.all()
    subcats = SubCategory.objects.all()

    return render(request, 'index.html', {'Closes':ext, 'cats':cats, 'subcats':subcats})
def single(request):
    id = request.GET.get('id')
    ext = Closes.objects.all()
    cats = Category.objects.all()
    subcats = SubCategory.objects.all()
    product = Product.objects.get(id=id)
    return render(request, 'single.html', {'product': product, 'Closes':ext, 'cats':cats, 'subcats':subcats})
def men(request):
    id = request.GET.get('cat')
    ext = Closes.objects.all()
    cats = Category.objects.all()
    subcats = SubCategory.objects.all()
    products = Product.objects.filter(subcategory_id=id)

    return render(request, 'men.html', {'products':products, 'Closes':ext, 'cats':cats, 'subcats':subcats})
def xato(request):
    return render(request, '404.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def checkout(request):
    user = request.user
    try:
        sh = shop.objects.get(client=user, status=0)
        product = shopitem.objects.filter(sho=sh)
    except:
        sh='0'
        product = ''
    ext = Closes.objects.all()
    cats = Category.objects.all()
    subcats = SubCategory.objects.all()
    return render(request, 'checkout.html', {'products': product, 'Closes':ext, 'cats':cats, 'subcats':subcats, 'sh':sh})
def och(request):
    user = request.user
    id = request.GET.get('id')
    sho = shop.objects.get(client=user, status=0)
    sh = shopitem.objects.get(id=id)
    sho.total -= sh.total
    sho.save()
    sh.delete()
    return redirect('checkout')
def index_single(request):
    return render(request, 'index_single.html')
def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print(username, password, User.objects.get(username=username))
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'Email yoki login xato'})
        # users = AllUser.objects.all()
        # for i in users:
        #     if i.email == request.POST['email'] and i.password == request.POST['password']:
        #         return HttpResponse('Hush kelibsiz')
        #     elif i == users[len(users) - 1]:
        #         return render(request, 'login.html', {'error': 'Email yoki login xato'})
    else:
        return render(request, 'login.html', {'error': ''})
def register(request):
    if request.method == 'POST':

        new_user = User.objects.create(username=request.POST['username'])
        new_user.last_name = request.POST['lastname']
        new_user.password = make_password(request.POST['password1'])
        new_user.email = request.POST['email']
        new_user.save()

        # subject = 'welcome to GFG world'
        # message = f'Hi {new_user.username}, thank you for registering in geeksforgeeks.'
        # email_from = settings.EMAIL_HOST_USER
        # recipient_list = ['mdrx1800@gmail.com', ]
        # send_mail(subject, message, email_from, recipient_list)
        # print(new_user)
    return render(request, 'register.html')
def Logout(request):
    logout(request)
    return redirect('login')

def addcart(request):
    user = request.user
    id = request.GET.get('id')
    try:
        sh = shop.objects.get(client=user, status=0)
    except:
        sh = shop.objects.create(client=user)
    print(sh)
    product = Product.objects.get(id=id)
    if product.discount:
        shitem = shopitem.objects.create(sho=sh, product_id=id, quantity=1, total=product.discount)
    else:
        shitem = shopitem.objects.create(sho=sh, product_id=id, quantity=1, total=product.price)
    sh.total += shitem.total
    sh.save()

    return redirect('index')
def search(request):
    product = Product.objects.all()
    result = Product.objects.filter(name__icontains=request.GET.get("search"))
    print(result)
    return render(request, 'men.html', {
        'result': result
    })

