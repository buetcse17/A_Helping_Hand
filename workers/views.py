from django.shortcuts import render, redirect
from customers.forms import WorkerRegisterForm
from django.contrib import messages
# Create your views here.

# TODO FARDIN 2 : complete worker registration form same as customer registration form, check customers/views.py
def register(request):
    if 'loggedIn' in request.session and request.session['loggedIn'] == True:
            return render(request, 'home_worker/home.html', {'loggedIn': request.session['loggedIn']})
    if request.method == 'POST':
        form = WorkerRegisterForm(request.POST)
        if form.is_valid():

            return redirect('home_worker-home')
    else:
        form = WorkerRegisterForm()
    return render(request, 'workers/reg_as_worker.html', {'form' : form})