from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .form import CustomerSignUpForm
from django.contrib.auth.decorators import login_required


class CustomerRegister(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/admissions')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/admissions')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'login_form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')


def home_view(request):
    return render(request, 'index-2.html')


@login_required
def admissions_view(request):
    return render(request, 'form.html')