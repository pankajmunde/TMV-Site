from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages
from django.views.generic import CreateView
from django.contrib.auth.forms import AuthenticationForm
from .models import User
from .form import CustomerSignUpForm


class CustomerRegister(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = '../templates/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/admissions')


def login_request(request):
    if request.user.is_authenticated:
        return redirect('/admissions')

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                next_url = request.GET.get('next')
                if not next_url:
                    return redirect("/admissions")
                return redirect(next_url)
                # return redirect('/admissions')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, '../templates/login.html',
                  context={'login_form': AuthenticationForm()})


def logout_view(request):
    logout(request)
    return redirect('/')

