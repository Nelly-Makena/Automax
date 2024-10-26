from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def login_view(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)

        # Check if the form is valid
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                # Log in the user and redirect to 'home' if authentication is successful
                login(request, user)
                messages.success(request, f"Your now looged in as {username}")
                return redirect('home')  # Replace 'home' with the correct URL name in your project

            else:
                messages.error(request, 'An error occurred trying to log you in....')

        else:
            # If the form is invalid, add an error message
            messages.error(request, 'Invalid form submission.')

        # Re-render the login page with the form and messages after POST request handling
        return render(request, 'login.html', {'login_form': login_form})

    else:  # Handles GET request
        # Render the login page with an empty form
        login_form = AuthenticationForm()
        return render(request, 'login.html', {'login_form': login_form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('main')
def registration_view(request):
    if request.method == 'POST':
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            user = register_form.save()
            user.refresh_from_db()
            login(request, user)  # Log in the user after registration
            messages.info(request, f"You are now registered as {user.username}")
            return redirect('home')  # Redirect to the home page after registration
    else:
        register_form = UserCreationForm()  # Create an empty form for GET requests
        messages.error(request, 'Please fill in the registration form.')

    return render(request, 'registration.html', {'register_form': register_form})