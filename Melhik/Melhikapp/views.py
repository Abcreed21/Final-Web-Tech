from admin_dashboard.views import *
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm, SendMessageForm
from django.contrib import messages
from django.contrib.auth import authenticate, login as user_login, logout
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import *
from telegram import Bot
from django.contrib.auth import update_session_auth_hash
from django.views.decorators.csrf import csrf_exempt
import requests
import random
import string

def index(request):
    reviews = Review.objects.all()
    return render(request, 'index.html', {'reviews': reviews})

def index_2(request):
    return render(request, 'index_2.html')

def job_search(request):
    categories = Category.objects.all()

    if request.method == 'GET':
        category_id = request.GET.get('category')
        location = request.GET.get('location')
        completed_projects = request.GET.get('completed_projects')
        pricing_type = request.GET.get('pricing_type')
        skills = request.GET.get('skills')
        availability = request.GET.get('availability')
        experience = request.GET.get('experience')
        hourly_rate_min = request.GET.get('hourly_rate_min')
        hourly_rate_max = request.GET.get('hourly_rate_max')
        keywords = request.GET.get('keywords')

        jobs = Job.objects.all()

        if category_id:
            jobs = jobs.filter(category_id=category_id)

        if location:
            jobs = jobs.filter(Q(country__icontains=location) | Q(city__icontains=location) | Q(zipcode__icontains=location))

        if completed_projects:
            jobs = jobs.filter(completed_projects=completed_projects)

        if pricing_type:
            jobs = jobs.filter(pricing_type=pricing_type)

        if skills:
            skills_list = skills.split(',')
            jobs = jobs.filter(skills__name__in=skills_list)

        if availability:
            availability_list = availability.split(',')
            jobs = jobs.filter(availability__in=availability_list)

        if experience:
            experience_list = experience.split(',')
            jobs = jobs.filter(experience__in=experience_list)

        if hourly_rate_min and hourly_rate_max:
            jobs = jobs.filter(hourly_rate__gte=hourly_rate_min, hourly_rate__lte=hourly_rate_max)

        if keywords:
            jobs = jobs.filter(Q(title__icontains=keywords) | Q(description__icontains=keywords))

        context = {
            'categories': categories,
            'jobs': jobs,
            'selected_category': category_id,
            'selected_location': location,
            'selected_completed_projects': completed_projects,
            'selected_pricing_type': pricing_type,
            'selected_skills': skills,
            'selected_availability': availability,
            'selected_experience': experience,
            'selected_hourly_rate_min': hourly_rate_min,
            'selected_hourly_rate_max': hourly_rate_max,
            'selected_keywords': keywords,
        }

        return render(request, 'job_search.html', context)

    context = {
        'categories': categories,
    }

    return render(request, 'job_search.html', context)

def onboard(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST, request.FILES)
    if form.is_valid():
      freelancer = form.save(commit=False)
      freelancer.is_freelancer = True
      freelancer.save()
      return redirect('login')
  else:
    form = RegistrationForm()

  return render(request, 'onboard_screen.html', {'form': form})


def onboard_screen_employer(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST, request.FILES) 
    if form.is_valid():
      employer = form.save(commit=False)
      employer.is_employer = True
      employer.save()
      return redirect('login')
  else: 
    form = RegistrationForm()

  return render(request, 'onboard_screen_employer.html', {'emp': form})

def login_view(request):
    form = Login_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email,password=password)
            if (user is not None and user.is_superuser):
                user_login(request, user)
                return redirect('admin_dashboard')
            elif user is not None and user.is_freelancer:
                user_login(request, user)
                return redirect('freelancer_dashboard')
            elif user is not None and user.is_employer:
                user_login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid Password or Email')
    return render(request, 'login.html', {'form': form})

def User_logout(request):
    logout(request)
    return redirect('index')

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

from .forms import ReviewForm

def completed_projects(request):
  if request.method == 'POST':
    form = ReviewForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('review')
  else:  
    form = ReviewForm()
  return render(request, 'completed_projects.html', {'form': form})

def review(request):
  reviews = Review.objects.all() 

  for review in reviews:
     print(review.timestamp.isoformat())

  return render(request, 'review.html', {'reviews': reviews})

@login_required
@employer_required
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


def freelancer_bookmarks(request):
    return render(request, 'freelancer_bookmarks.html')

def freelancer_cancelled_projects(request):
    return render(request, 'freelancer_cancelled_projects.html')

@login_required
def freelancer_change_password(request):
  if request.method == 'POST':
    form = PasswordChangingForm(request.user, request.POST)
    if form.is_valid():  
      user = form.save()
      update_session_auth_hash(request, user)
      messages.success(request, 'Password updated!')   
      return redirect('review')
    else:
      messages.error(request, 'Please correct the error below.')
  else: 
    form = PasswordChangeForm(request.user)
  return render(request, 'freelancer_change_password.html', {'form': form})

def user_chat(request):
  chat_room = ChatRoom.objects.filter(user = request.user)
  context = {
      'users' : chat_room
  }
  return render(request, 'chats.html',context)



def messages_view(request, user_id, room_id):
    chat_room = ChatRoom.objects.filter(user = request.user)
    form = SendMessageForm(request.POST or None)
    receiver_user = CustomUser.objects.get(pk = user_id)
    room = ChatRoom.objects.get(pk = room_id)
    if request.method == 'POST':
        if form.is_valid():
            msg = form.save(commit=False)
            msg.chat =  room
            msg.sender = request.user
            msg.receiver = receiver_user
            msg.save() 


    room = ChatRoom.objects.get(id = room_id)
    message = Message.objects.filter(chat = room)
    user = CustomUser.objects.get(pk = user_id)
    context= {
        'user_message' : message,
        'user' : user,
        'form' : form,
        'users' : chat_room,
    }
    
    return render(request, 'chats.html', context)



def freelancer_completed_projects(request):
    return render(request, 'freelancer_completed_projects.html')


@login_required
@freelancer_required
def freelancer_dashboard(request):
    return render(request, 'freelancer_dashboard.html')

def freelancer_delete_account(request):
    from django.contrib.auth import logout
from django.contrib import messages
from django.shortcuts import redirect

@login_required
def freelancer_delete_account(request):
  if request.method == 'POST':
    form = DeleteAccountForm(request.POST)
    if form.is_valid():
      if form.cleaned_data['password'] == request.user.password:
        request.user.delete()
        logout(request)
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')
      else:
        messages.error(request, 'Incorrect password provided.')
  else:
    form = DeleteAccountForm()

  return render(request, 'freelancer_delete_account.html', {'form': form})

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

@login_required
def freelancer_profile_settings(request):
  if request.method == 'POST':
    form = FreelancerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
      freelancer_profile = form.save(commit=False)
      freelancer_profile.user.is_freelancer = request.user.is_freelancer
      freelancer_profile.save()
      messages.success(request, 'You have completed your profile')
      return redirect ('freelancer_profile')
  else:
    form = FreelancerForm()
  context = {
    'form': form
    }
  return render(request, 'freelancer_profile_settings.html', context)


# freelancer_profile view

@login_required
def freelancer_profile(request):
    user = CustomUser.objects.all()
    freelancer_profile = Freelancer.objects.get(user=request.user)
    print(freelancer_profile)
    context = {
        'freelancer_profile': freelancer_profile,
        'users': user
    }

    return render(request, 'freelancer_profile.html', context)



def freelancer_project_proposals(request):
    return render(request, 'freelancer_project_proposals.html')

def freelancer_review(request):
    return render(request, 'freelancer_review.html')

def freelancer_task(request):
    return render(request, 'freelancer_task.html')

def freelancer_transaction_history(request):
    transactions = Transaction.objects.filter()

    formatted_transactions = []
    for transaction in transactions:
        paid_on = transaction.paid_on.strftime('%d %b %Y, %I:%M%p')
        formatted_transactions.append({
            'employer_name': transaction.first_name + ' ' + transaction.last_name,
            'amount': transaction.amount,
            'status': transaction.payment_method,
            'paid_on': paid_on
        })

    context = {'transactions': formatted_transactions}
    return render(request, 'freelancer_transaction_history.html', context)

def freelancer_verify_identity(request):
    return render(request, 'freelancer_verify_identity.html')

def freelancer_view_project_detail(request):
    return render(request, 'freelancer_view_project_detail.html')

@csrf_exempt
def freelancer_withdraw_money(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        payment_method = request.POST.get('payment_method')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        tx_ref = first_name + '-tx-' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))

        if payment_method == 'Chapa':
            # Prepare the data for the Chapa API
            data = {
                'public_key': 'CHAPUBK_TEST-HJ7z9xGJpf4MFH6PjfpI7G45BFLCFrxf',
                'tx_ref': tx_ref,
                'amount': amount,
                'currency': 'ETB',
                'email': email,
                'first_name': first_name,
                'last_name': last_name,
                'phone_number': phone_number,
                'title': 'Thank you for choosing Chapa. Your withdrawal has been processed.',
                'description': 'Paying with Confidence with Chapa.',
                'meta[title]': 'test'
            }

            # Make a POST request to the Chapa API
            response = requests.post('https://api.chapa.co/v1/hosted/pay', data=data)

            # Check the response from the Chapa API (you'll need to adjust this based on the actual response format)
            if response.status_code == 200:
                Transaction.objects.create(
                    amount=amount,
                    payment_method=payment_method,
                    email=email,
                    first_name=first_name,
                    last_name=last_name,
                    tx_ref=tx_ref,
                )
                return HttpResponse('Withdrawal processed successfully.')
            else:
                return redirect('https://checkout.chapa.co/checkout/payment/V38JyhpTygC9QimkJrdful9oEjih0heIv53eJ1MsJS6xG')

        elif payment_method == 'Yene Pay':
            # Call Yene Pay API here
            return HttpResponse('Thank you for choosing Yene Pay. Your withdrawal has been processed.')

        else:
            return HttpResponse('Invalid payment method selected.')

    else:
        return render(request, 'freelancer_withdraw_money.html')


def logoutUser(request):
    logout(request)
    return redirect ('index')

def forgot_password(request):
  form = ForgotPasswordForm()
  if request.method == 'POST':
    form = ForgotPasswordForm(request.POST)
    if form.is_valid():
      user_name = form.cleaned_data['user_name']
      try:
          user = CustomUser.objects.get(username=user_name) 
      except CustomUser.DoesNotExist:
          messages.error(request, 'User not found')
      else:
          password = user.password
          messages.success( request, f'Your password is: {password}')
          return redirect('login')
  return render(request, 'forgot_password.html', {'form': form})

def manage_projects(request):
    return render(request, 'manage_projects.html')

def membership_plans(request):
    return render(request, 'membership_plans.html')

def ongoing_projects(request):
    return render(request, 'ongoing_projects.html')

def pending_projects(request):
    return render(request, 'pending_projects.html')

@employer_required
@login_required
def project_form(request):
    form = JobForm()
    if request.method == 'POST':
        form = JobForm(request.POST)
        print("*********post method entered**********")
        print(form.errors)
        print(form.is_valid())

        if form.is_valid():
            job = form.save()
            bot_token = '6575514030:AAFO2CwLOdy7dkZKyMosGNmZuVMPXHL0ZlQ'
            chat_id = '-1001913256564'
            text = (
                f"New project added: {job.project_title}\n"
                f"Category: {job.category_type}\n" 
                f"Price: {job.price}\n Birr"
                f"Duration: {job.duration}\n"
                f"Start Date: {job.start_date}\n" 
                f"Reference Links: {job.reference_links}\n"
                f"Description: {job.project_description}"
            )
         
            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'

            data = {
                'chat_id': chat_id,
                'text': text
            }
            
            response = requests.post(url, data=data)

            if response.status_code == 200:
                print('Message sent!')
            else:
                print('Error sending message:')
                print(response.text)

            return redirect('project', job.pk)
        
    context = {
        'form': form,
        'categories': Category.objects.all(),
    }
    return render(request, 'post_project.html', context)

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def profile_settings(request):

  if request.method == 'POST':
    form = FreelancerForm(request.POST, request.FILES)
    if form.is_valid():
      freelancer_profile = form.save(commit=False)
      freelancer_profile.user = request.user
      freelancer_profile.save()
      return redirect('user-account-details')
  else:
    form = FreelancerForm()
  context = {
    'form': form
    }
  return render(request, 'profile_settings.html', context)


def user_account_details(request):
  freelancer_profile = Freelancer.objects.get(user=request.user)
  context = {
    'profile': freelancer_profile
  }
  return render(request, 'user-account-details.html', context)

def project_details(request):
    return render(request, 'project_details.html')

def project_payment(request):
    return render(request, 'project_payment.html')

def project_proposals(request):
    return render(request, 'project_proposals.html')

def project(request):
  jobs = Job.objects.all()
  return render(request, 'project.html', {'jobs': jobs})

def tasks(request):
    return render(request, 'tasks.html')

def term_condition(request):
    return render(request, 'term_condition.html')


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

