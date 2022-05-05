from audioop import reverse
from re import template
from tkinter.tix import MAX
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import date, datetime
from django.contrib import messages
from django.db.models import Max
from pymysql import NULL
from django.core.mail import send_mail
from django.core.mail import send_mass_mail
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView,PasswordResetDoneView

from users.models import RatesComments,Tarrifs

class MyPasswordChangeView(PasswordChangeView):
    template_name='admindash/edit_user.html'
    success_url = reverse_lazy('pass-change-done-view')

class MyPasswordDoneView(PasswordResetDoneView):
    template_name='admindash/users.html'
# Admin Dashboard
def dashAdmin(request):
    users= User.objects.all().count()
    comments = RatesComments.objects.all().count()
    participants = RatesComments.objects.values('username').distinct().count()
    
    return render(request,'admindash/dashboard.html',
                  {'users':users,'comments':comments,
                   'participants':participants})
# Display all tarrifss
def tarrifs(request):    
    tarrif =  Tarrifs.objects.all().order_by('-update_date')
    return render(request,'admindash/tarrifs.html',{'tarrif':tarrif})
# Edit all tarrifs
def edit_tarrifs(request,tarrifs_id):
    if request.method == 'POST':
        price = request.POST['price']
        print('The tarif is ' + str(tarrifs_id))
        reasons = request.POST['reason']
        edittarrif = Tarrifs.objects.get(pk=tarrifs_id)
        edittarrif.price = price
        print(edittarrif.price)
        edittarrif.comment=reasons
        Tarrifs.objects.filter(pk=tarrifs_id).update(amount=price,update_date=timezone.now())
    
        return redirect('admin-tarrifs') 
    else:
        tarrif=Tarrifs.objects.get(pk=tarrifs_id)
        return render(request,'admindash/edit_tarrif.html',{'tarrif':tarrif})
# Show all comments on each tarrif
def comments(request,tarrifs_id):
    rates = Tarrifs.objects.get(pk=tarrifs_id)
    print('The rate is ' + str(rates.tarrif_number))
    comments_list = RatesComments.objects.filter(rate=rates.tarrif_number)
    return render(request,'admindash/comments.html',{'comments_list':comments_list})
#Show all comments
def all_comments(request):
    comment_list = RatesComments.objects.all()
    print(comment_list)
    return render(request,'admindash/comments.html',{'comment_list':comment_list})
# Delete  tarrifs
def delete_tarrifs(request,tarrifs_id):
    delete_tarrif = Tarrifs.objects.get(pk=tarrifs_id)
    delete_tarrif.delete()
    return redirect('admin-tarrifs')
# Add new tarrif
def new_tarrif(request):
    if request.method == 'POST':
        names = request.POST['names']
        price= request.POST['price']
        comments = request.POST['reason']
        tarrif = Tarrifs.objects.order_by('-tarrif_number').first()
        
        if tarrif == NULL:
            number_tarrif = 1000
            #new_tarif = Tarrifs.objects.create(name=names,tarrif_number=number_tarrif,amount=price,update_date=timezone.now(),comment=comments,username=str(request.user))
        else:
            number_tarrif = int(tarrif.tarrif_number) + 1 
            #new_tarif = Tarrifs.objects.create(name=names,tarrif_number=number_tarrif,amount=price,update_date=timezone.now(),comment=comments,username=str(request.user))
        #new_tarif.save()
        subject='Bikita Rural District Consultation Platform'        
        from_email =  'webikita69@gmail.com'       
        recievers = []
        for user in User.objects.all():
            username=user.username
            recievers.append(user.email) 
            messag = f'Hi { username }. ' + comments       
            send_mail(subject,messag,from_email,recievers,fail_silently=False)
        return redirect('admin-tarrifs')

# View all users
def view_users(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request,'admindash/users.html',{'users':users})

# Show all user comments 
def show_user_comments(request,user_id):
    rates= User.objects.get(pk=user_id)
    comments=RatesComments.objects.filter(username=rates.username)
    counts=comments.count()
    return render(request,'admindash/user_comments.html',{'comments':comments,'counts':counts })

# edit userprofile
def edit_user(request,user_id):
    if request.method == 'POST':
        username=request.POST['username']
        name = request.POST['names']
        surname= request.POST['surname']
        email = request.POST['email']
        ward = request.POST['ward']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:            
            User.objects.filter(username=username).update(first_name=name,last_name=surname,email=email,password=password1)
            return redirect('view-users')
        else:
            messages.info(request,'password not matching')
            return redirect('edit-user')
    else:
        users = User.objects.get(pk=user_id)
        return render(request,'admindash/edit_user.html',{'users':users})

# delete user profile
def delete_user(request,user_id):
    delete_user = User.objects.get(pk=user_id)
    delete_user.delete()
    return redirect('view-users')

def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']  
        names= request.POST['name'] 
        surname= request.POST['surname']
        ward= request.POST['ward']     
        email = request.POST['emails']
        password1 = request.POST['password1']
        password2 = request.POST['password2']  

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register-user')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
                return redirect('view-users')
            else:
                user = User.objects.create(username=username,first_name=names,last_name=surname,password=password1,email=email)
                subject='Bikita Rural District Consultation Platform'
                messag = f'Hi {username}. Welcome to Bikita Rural District Council Online Budget Platform. You have updates on everything that happens on the budget'
                from_email =  'webikita69@gmail.com'
                recipient_list=[email]
                send_mail(subject,messag,from_email,recipient_list,fail_silently=False)
                user.save()
            
    return redirect('view-users')