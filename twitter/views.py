from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth.models import User

def run_migrations(request):
    """Run migrations using a view."""
    call_command('migrate')
    return HttpResponse("Migrations completed successfully!")

def create_superuser(request):
    """Create a superuser using a view."""
    username = "admin"
    email = "admin@example.com"
    password = "admin123"

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        return HttpResponse("Superuser created successfully! Use 'admin/admin123' to log in.")
    else:
        return HttpResponse("Superuser already exists.")

def home(requests):
    return render(requests, 'website/home.html')