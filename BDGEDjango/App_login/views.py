from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created! You can now log in.')
            return redirect('login')  # Redirect to your login URL
        else:
            # Re-render the form with errors (important for user experience)
            return render(request, 'App_login/register.html', {'form': form})

    else:  # Handle GET requests (when the user first visits the page)
        form = UserCreationForm()  # Create a blank form
        return render(request, 'App_login/register.html', {'form': form})