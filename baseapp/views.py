from django.shortcuts import render, redirect
from .models import Table
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout

# jobs = [
#     {"id": 1, "role": "Agricultural Engineer", "location": "Enugu"},
#     {"id": 2, "role": "Horticulturist", "location": "Nassarawa"},
#     {"id": 3, "role": "Agricultural Manager", "location": "Osun"},
#     {"id": 4, "role": "Data Entry Intern", "location": "Lagos"},
#     {"id": 5, "role": "Solar Engineer", "location": "Benue"},
#     {"id": 6, "role": "Intern Farmer", "location": "Ogun"},
#     {"id": 7, "role": "Irrigator", "location": "Ekiti"},
# ]


jobs = Table.objects.all()
# Create your views here.
def home(requests):
    return render(requests, '../templates/index.html')

#view for the careers page
def careers(requests):
    no_of_jobs = len(jobs)
    context = {"jobs": jobs, "no_of_jobs": no_of_jobs}
    return render(requests, '../templates/careers.html', context)

#view for each job, in a new page
def careerDesc(requests, pk):
    job = None
    for i in jobs:
        if i['id'] == int(pk):
            job = i
    context = {'job': job}
    return render(requests, '../templates/description.html', context)

#this view would render out the 404 page, 404 means page not found
def error404(request, exception):
    return render(request, '404.html')

#the reason why we cant use login is because there is a built in function called login
def loggin(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "This user does not exist")
            user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('careers')
        else:
            messages.error(request, "error")
 
    context = {'page': page}
    return render(request, '../templates/login_register.html', context)

#the view for the sign up page
def sign_up(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('careers')
        else:
            messages.error(request, "An error occured during registration")

    context = {'page': page, 'form': form}
    return render(request, '../templates/login_register.html', context)

#this view would log out the user from the current page
def logoutUser(request):
    logout(request)
    return redirect('home')
#    return HttpResponse("logged out")
    #return redirect('home')

    #if page == 'careers':
    #  return redirect('careers')
    #elif page == 'home':
    #   return redirect('home') 


#this view would render out the application page.
def applicationPage(request):
    return render(request, '../templates/applicationPage.html')