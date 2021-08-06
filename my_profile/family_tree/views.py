from django.shortcuts import render
import os, json
from family_tree.models import familyData, accessRecord
from family_tree.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
# Create your views here.


def index(request):
    return render(request, os.path.join('family_tree', 'index.html'))


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def tree_page(request):
    objects = [i for i in familyData.objects.values()]
    keys_values = json.loads(json.dumps(objects), parse_int=str)
    data = json.dumps(keys_values)
    data_dict = {'data': data}
    return render(request, os.path.join('family_tree', 'tree_page.html'), context=data_dict)


def contact_page(request):
    return render(request, os.path.join('family_tree', 'contact_page.html'))


def register_page(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            
            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
                
            profile.save()
            
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        
    return render(request, 'family_tree/register_page.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})

    return render(request, os.path.join('family_tree', 'register_page.html'))


def login_page(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")

        else:
            print("Someone tried to login and failed")
            print(f"Username {username} and password {password}")
            return HttpResponse("invalid login details supplied")
    else:
        return render(request,'family_tree/login_page.html', {})


