from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login as admin_login
from Melhikapp.forms import *
from Melhikapp.models import *
from django.http import HttpResponse
from Melhikapp.decorators import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def admin_index(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                # Fix: login() takes the request and user 
                admin_login(request, user) 
                # messages.success(request, 'You are now logged in')
                return redirect('admin_dashboard')
            else:
                messages.error(request, 'Only superadmin can log in')
                return render(request, 'admin.html', {'error': 'Only superadmin can log in'})
        else:
                messages.error(request, 'Invalid login')
                return render(request, 'admin.html', {'error': 'Invalid login'})

    return render (request , 'admin.html')

def admin_logout(request):
    logout(request)
    return redirect('index')

@login_required
@admin_user_required
def admin_dashboard(request):
    total_num_users = CustomUser.objects.count()
    total_jobs = Job.objects.count()
    reviews = Review.objects.all() 
    for review in reviews:
     print(review.timestamp.isoformat())
     
    return render(request, 'admin_dashboard.html', {'reviews': reviews, 'total_num_users': total_num_users, 'total_jobs': total_jobs})

def activities(request):
    return render(request, 'activities.html')

def categories(request):
    if request.method == 'POST':
        name = request.POST.get('category_name')
        category = Category(name=name)
        category.save()
        return redirect('categories')

    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})

def delete_category(request, category_id):
     category = Category.objects.get(id=category_id)
     category.delete()
     return redirect('categories')

def data_tables(request):
    return render(request, 'data_tables.html')

def deposit(request):
    return render(request, 'deposit.html')

def deposit_cancelled(request):
    return render(request, 'deposit_cancelled.html')

def deposit_completed(request):
    return render(request, 'deposit_completed.html')

def deposit_hold(request):
    return render(request, 'deposit_hold.html')

def deposit_pending(request):
    return render(request, 'deposit_pending.html')

def earning_employer(request):
    return render(request, 'earning_employer.html')

def earning_freelancer(request):
    return render(request, 'earning_freelancer.html')

def email_settings(request):
    return render(request, 'email_settings.html')

def employe_list(request):
    return render(request, 'employe_list.html')

def forget_password(request):
    return render(request, 'forget_password.html')

def freelance_list(request):
    return render(request, 'freelance_list.html')

def localization_details(request):
    return render(request, 'localization_details.html')

def login(request):
    return render(request, 'login.html')

def other_settings(request):
    return render(request, 'other_settings.html')

def payment_settings(request):
    return render(request, 'payment_settings.html')

def projects(request):
    jobs = Job.objects.select_related('author').all()
    total_jobs = Job.objects.count()
    context = {
        'jobs': jobs,
        'total_jobs': total_jobs
    }
    return render(request, 'projects.html', context)

def project_bidding(request):
    return render(request, 'project_bidding.html')

def project_earnings(request):
    return render(request, 'project_earnings.html')

def project_invoice(request):
    return render(request, 'project_invoice.html')

def users(request):
    freelancers = Freelancer.objects.all()

    context = {
        'freelancers': freelancers,
    }

    return render(request, 'users.html', context)

def withdrawn(request):
    return render(request, 'withdrawn.html')

def withdrawn_pending(request):
    return render(request, 'withdrawn_pending.html')

def withdrawn_cancelled(request):
    return render(request, 'withdrawn_cancelled.html')

def withdrawn_completed(request):
    return render(request, 'withdrawn_completed.html')

def transaction(request):
    return render(request, 'transaction.html')

def transaction_onhold(request):
    return render(request, 'transaction_onhold.html')

def transaction_pending(request):
    return render(request, 'transaction_pending.html')

def transaction_withdraw(request):
    return render(request, 'transaction_withdraw.html')

def transaction_deposit(request):
    return render(request, 'transaction_deposit.html')

def transaction_completed(request):
    return render(request, 'transaction_completed.html')

def providers(request):
    return render(request, 'providers.html')

def subscription(request):
    return render(request, 'subscription.html')

def subscripe_freelancer(request):
    return render(request, 'subscripe_freelancer.html')

def reports(request):
    return render(request, 'reports.html')

def roles(request):
    return render(request, 'roles.html')

def roles_permission(request):
    return render(request, 'roles_permission.html')

def skills(request):
    return render(request, 'skills.html')

def verify_identity(request):
    return render(request, 'verify_identity.html')

def settings(request):
    return render(request, 'settings.html')

def user_active(request):
    return render(request, 'user_active.html')

def profile(request):
    return render(request, 'profile.html')

def user_administrator(request):
    return render(request, 'user_administrator.html')

def user_inactive(request):
    return render(request, 'user_inactive.html')

def user_profile(request):
    return render(request, 'user_profile.html')

def user_suspended(request):
    return render(request, 'user_suspended.html')

def social_links(request):
    return render(request, 'social_links.html')

def others_settings(request):
    return render(request, 'others_settings.html')

def seo_settings(request):
    return render(request, 'seo_settings.html')

def user_suspended(request):
    return render(request, 'user_suspended.html')

def social_settings(request):
    return render(request, 'social_settings.html')