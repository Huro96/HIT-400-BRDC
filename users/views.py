from operator import index
from unicodedata import name
from unittest import result
from xml.dom.minidom import Element
from django.contrib.auth.models import User
#from translate import Translator
import googletrans
from googletrans import *
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from datetime import date, datetime

from admindash.views import comments
from .models import UnwantedWords,BlockContacts,RatesComments,Tarrifs,Projects


# views for settings 

# User Dashboard view.
def users(request):    
    return render(request,'users/dashboard.html')
# Project views page
def projects(request):    
    return render(request,'users/projects.html')
# allcomments views page
def tarrifs(request):
    tarrifs= Tarrifs.objects.all() 
    projects= Projects.objects.all()
    #projects = 
    return render(request,'users/comments.html',{'tarrifs':tarrifs,'projects':projects})
# Comments Page
def post_tarrif_comments(request):    
    if request.method == 'POST':
        user= BlockContacts.objects.filter(username=request.user).count()
        if user >= 1:
            print(user)
            messages.success(request,("You have been blocked to use this platform because you have used inapprpriate words"))
            return redirect('proposed-rates')
        else:
            print(user)
            rates = request.POST['rate_number']
            com= request.POST['comment']
            comments = request.POST['comment'].split()               
            x= ' '.join(comments).split()        
            myList =x 
            print(myList)
            index = 0 
            find=0
            while index < len(myList):
                element=myList[index]
                result = UnwantedWords.objects.filter(name=element).count()
                find = find + result          
                index += 1
            if find >= 1:
                blockContact = BlockContacts.objects.create(username=str(request.user),date=timezone.now())
                blockContact.save()                 
            else: 
                             
                newComment = RatesComments.objects.create(username = str(request.user),rate= rates ,comment=com,date=datetime.now())
                newComment.save()
                #translator= Translator()
                #texts = request.POST['comment']
                #translation = translator.translate(texts,dest='en')
                #print(translation.text) 
                
            return redirect('proposed-rates') 
    else:
        rates= Tarrifs.objects.all()        
        return render(request,'users/rates.html',{'rates':rates})

    # Show Comments
def show_comments(request,tarrif_list_id):
    rates = Tarrifs.objects.get(pk=tarrif_list_id)
    comments=RatesComments.objects.filter(rate=rates.tarrif_number)
    counts=comments.count()
    print(counts)    
    return render(request,'users/allcomments.html',{'counts':counts,'rates':rates,'comments':comments})
def project_comments(request,project_list_id):
    rates= Projects.objects.get(pk=project_list_id)
    comments=RatesComments.objects.filter(rate=rates.rate_number)
    counts=comments.count()
    return render(request,'users/allcomments.html',{'rates':rates,'counts':counts,'comments':comments})


# Delete comments
def delete_comments(request,com_id):
    rates_number= RatesComments.objects.get(pk=com_id)
    rates_number.delete()
    findproject=Projects.objects.filter(rate_number = rates_number.rate).count()  
    if findproject > 0:
        rates= Projects.objects.get(rate_number = rates_number.rate)   
    else:
        rates=Tarrifs.objects.get(tarrif_number=rates_number.rate)
    comments=RatesComments.objects.filter(rate=rates_number.rate)
    counts=comments.count()
    return render(request,'users/allcomments.html',{'counts':counts,'rates':rates,'comments':comments})

   
    
    