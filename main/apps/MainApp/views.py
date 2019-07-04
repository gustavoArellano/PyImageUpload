from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.conf import settings
from django.contrib.messages import get_messages 
from .models import User
from django import template
from django.conf import settings
import bcrypt




def index(request):
    return render(request, 'index.html')

def registerProcess(request):
    if 'userId' in request.session:
        return redirect('/home')
    else:
        errors = User.objects.RegValidation(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
        else:
            hash_pw = bcrypt.hashpw(request.POST['password'].encode('utf8'), bcrypt.gensalt())
            User.objects.create(
                name = request.POST['name'], 
                email = request.POST['email'], 
                password = hash_pw
                )

            user = User.objects.last()
            request.session['userId'] = user.id
            request.session['email'] = user.email
            return redirect('/home')
        return redirect('/')

def loginProcess(request): 
    if 'userId' in request.session:
        return redirect('/home')
    else:
        errors = User.objects.LoginValidation(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value, extra_tags = key)
        else:
            user = User.objects.get(email = request.POST['loginEmail'])
            request.session['userId'] = user.id
            request.session['name'] = user.name
            return redirect('/home')
        return redirect('/')

def home(request):
    thisUser = User.objects.get(id = request.session['userId'])
    allUsers = User.objects.all()

    context = {
        'thisUser': thisUser,
        'allUsers': allUsers
    }
    return render(request, 'home.html', context)

def logout(request): 
    request.session.clear()
    return redirect('/')

def ImageUpload(request):
    thisUser = request.session['userId']
    
    image = {
        'image': request.POST['imageUpload']
    }

    User.objects.filter(id = thisUser).update(**image)
    print('***SUCCESS***')

    
    print(thisUser)

    uploadedImage = User.objects.get(image = request.POST['imageUpload'])
    print('***************')
    print(uploadedImage)

    return redirect('/home')
