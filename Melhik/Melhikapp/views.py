import os
import telegram
from admin_dashboard.views import *
from django.shortcuts import render, redirect
from .forms import FreelancerForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def index(request):
    return render(request, 'index.html')

def index_2(request):
    return render(request, 'index_2.html')

def register(request):
    if request.method == 'POST':
        account_type = request.POST.get('account-type')
        if account_type == 'freelancer':
            # Handle freelancer registration
            return redirect('onboard_screen')
        elif account_type == 'employer':
            # Handle employer registration
            return redirect('onboard_screen_employer')
    return render(request, 'register.html')


def onboard_screen(request):
    if request.method == 'POST':
        form = FreelancerForm(request.POST, request.FILES)
        if form.is_valid():
            # Handle validated data
            return redirect('success_page')
    else:
        form = FreelancerForm()
    return render(request, 'onboard_screen.html', {'form': form})


def error_404(request):
    return render(request, '404_page.html')

def about(request):
    return render(request, 'about.html')

def blog_grid(request):
    return render(request, 'blog_grid.html')

def cancelled_projects(request):
    return render(request, 'cancelled_projects.html')

def change_password(request):
    return render(request, 'change_password.html')

def chats(request):
    return render(request, 'chats.html')

def company_details(request):
    return render(request, 'company_details.html')

def company_gallery(request):
    return render(request, 'company_gallery.html')

def company_profile(request):
    return render(request, 'company_profile.html')

def company_project(request):
    return render(request, 'company_project.html')

def company_review(request):
    return render(request, 'company_review.html')

def completed_projects(request):
    return render(request, 'completed_projects.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def delete_account(request):
    return render(request, 'delete_account.html')

def deposit_funds(request):
    return render(request, 'deposit_funds.html')

def developer_details(request):
    return render(request, 'developer_details.html')

def developer_list(request):
    return render(request, 'developer_list.html')

def developer_profile(request):
    return render(request, 'developer_profile.html')

def developer(request):
    return render(request, 'developer.html')

def edit_project(request):
    return render(request, 'edit_project.html')

def faq(request):
    return render(request, 'faq.html')

def favourites(request):
    return render(request, 'favourites.html')

def invited_favourites(request):
    return render(request, 'invited_favourites.html')

def favourites_list(request):
    return render(request, 'favourites_list.html')

def files(request):
    return render(request, 'files.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def freelancer_bookmarks(request):
    return render(request, 'freelancer_bookmarks.html')

def freelancer_cancelled_projects(request):
    return render(request, 'freelancer_cancelled_projects.html')

def freelancer_change_password(request):
    return render(request, 'freelancer_change_password.html')

def freelancer_chats(request):
    return render(request, 'freelancer_chats.html')

def freelancer_completed_projects(request):
    return render(request, 'freelancer_completed_projects.html')

def freelancer_dashboard(request):
    return render(request, 'freelancer_dashboard.html')

def freelancer_delete_account(request):
    return render(request, 'freelancer_delete_account.html')

def freelancer_favourites(request):
    return render(request, 'freelancer_favourites.html')

def freelancer_files(request):
    return render(request, 'freelancer_files.html')

def freelancer_invitation(request):
    return render(request, 'freelancer_invitations.html')

def freelancer_invoices(request):
    return render(request, 'freelancer_invoices.html')

def freelancer_membership(request):
    return render(request, 'freelancer_membership.html')

def freelancer_milestones(request):
    return render(request, 'freelancer_milestones.html')

def freelancer_ongoing_projects(request):
    return render(request, 'freelancer_ongoing_projects.html')

def freelancer_payment(request):
    return render(request, 'freelancer_payment.html')

def freelancer_portfoilo(request):
    return render(request, 'freelancer_portfoilo.html')

def javascript(request):
    return render(request, 'javascript;.html')

def freelancer_profile_settings(request):
    return render(request, 'freelancer_profile_settings.html')

def freelancer_profile(request):
    return render(request, 'freelancer_profile.html')

def freelancer_project_proposals(request):
    return render(request, 'freelancer_project_proposals.html')

def freelancer_review(request):
    return render(request, 'freelancer_review.html')

def freelancer_task(request):
    return render(request, 'freelancer_task.html')

def freelancer_transaction_history(request):
    return render(request, 'freelancer_transaction_history.html')

def freelancer_verify_identity(request):
    return render(request, 'freelancer_verify_identity.html')

def freelancer_view_project_detail(request):
    return render(request, 'freelancer_view_project_detail.html')

def freelancer_withdraw_money(request):
    return render(request, 'freelancer_withdraw_money.html')

def login(request):
    email = None
    password = None
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
    try: 
        user = User.objects.get(email=email)
    except:
        messages.error(request, 'User does not exist')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Email OR Password does not exist')
    return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect ('dashboard')


def manage_projects(request):
    return render(request, 'manage_projects.html')

def membership_plans(request):
    return render(request, 'membership_plans.html')

def onboard_screen_employer(request):
    return render(request, 'onboard_screen_employer.html')

def onboard_screen(request):
    return render(request, 'onboard_screen.html')

def ongoing_projects(request):
    return render(request, 'ongoing_projects.html')

def pending_projects(request):
    return render(request, 'pending_projects.html')

def post_project(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        # Get data from form
        title = request.POST.get('title')
        price_type = request.POST.get('price_type')
        hourly_rate = request.POST.get('hourly_rate')
        duration = request.POST.get('duration')
        tags = request.POST.get('tags')
        period_type = request.POST.get('period_type')
        start_date = request.POST.get('start_date')
        reference_links = request.POST.get('reference_links')
        description = request.POST.get('description')

        # Create new job
        job = Job.objects.create(
            title=title,
            price_type=price_type,
            hourly_rate=hourly_rate,
            duration=duration,
            tags=tags,
            period_type=period_type,
            start_date=start_date,
            reference_links=reference_links,
            description=description
        )
        # Redirect to job detail view
        return redirect('project', job_id=job.id)

    return render(request, 'post_project.html', {'categories': categories})


def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def profile_settings(request):
    return render(request, 'profile_settings.html')

def project_details(request):
    return render(request, 'project_details.html')

def project_payment(request):
    return render(request, 'project_payment.html')

def project_proposals(request):
    return render(request, 'project_proposals.html')

def project(request):
    return render(request, 'project.html')

def review(request):
    return render(request, 'review.html')

def tasks(request):
    return render(request, 'tasks.html')

def term_condition(request):
    return render(request, 'term_condition.html')

def user_account_details(request):
    return render(request, 'user_account_details.html')

def verify_identity(request):
    return render(request, 'verify_identity.html')

def video_call(request):
    return render(request, 'video_call.html')

def view_invoice(request):
    return render(request, 'view_invoice.html')

def view_project_detail(request):
    return render(request, 'view_project_detail.html')

def voice_call(request):
    return render(request, 'voice_call.html')

def invoices(request):
    return render(request, 'invoices.html')

