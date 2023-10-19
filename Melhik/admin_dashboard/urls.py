from django.urls import path
from . import views
from .views import fetch_chart_data

urlpatterns = [
    path('admin/', views.admin_index, name='admin'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('data/', fetch_chart_data, name='fetch_chart_data'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('activities/', views.activities, name='activities'),
    path('categories/', views.categories, name='categories'),
    path('delete-category/<int:category_id>/', views.delete_category, name='delete-category'),
    path('data_tables/', views.data_tables, name='data_tables'),
    path('deposit/', views.deposit, name='deposit'),
    path('deposit_cancelled/', views.deposit_cancelled, name='deposit_cancelled'),
    path('deposit_completed/', views.deposit_completed, name='deposit_completed'),
    path('deposit_hold/', views.deposit_hold, name='deposit_hold'),
    path('deposit_pending/', views.deposit_pending, name='deposit_pending'),
    path('earning_employer/', views.earning_employer, name='earning_employer'),
    path('earning_freelancer/', views.earning_freelancer, name='earning_freelancer'),
    path('email_settings/', views.email_settings, name='email_settings'),
    path('employe_list/', views.employe_list, name='employe_list'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('freelance_list/', views.freelance_list, name='freelance_list'),
    path('localization_details/', views.localization_details, name='localization_details'),
    path('users/', views.users, name='users'),
    path('profile/', views.profile, name='profile'),
    path('user_active/', views.user_active, name='user_active'),
    path('user_administrator/', views.user_administrator, name='user_administrator'),
    path('user_inactive/', views.user_inactive, name='user_inactive'),
    path('user_profile/', views.user_profile, name='user_profile'),
    path('user_suspended/', views.user_suspended, name='user_suspended'),
    path('withdrawn/', views.withdrawn, name='withdrawn'),
    path('withdrawn_pending/', views.withdrawn_pending, name='withdrawn_pending'),
    path('withdrawn_cancelled/', views.withdrawn_cancelled, name='withdrawn_cancelled'),
    path('withdrawn_completed/', views.withdrawn_completed, name='withdrawn_completed'),
    path('projects/', views.projects, name='projects'),
    path('project_bidding/', views.project_bidding, name='project_bidding'),
    path('project_earnings/', views.project_earnings, name='project_earnings'),
    path('project_invoice/', views.project_invoice, name='project_invoice'),
    path('other_settings/', views.other_settings, name='other_settings'),
    path('payment_settings/', views.payment_settings, name='payment_settings'),
    path('transaction/', views.transaction, name='transaction'),
    path('transaction_onhold/', views.transaction_onhold, name='transaction_onhold'),
    path('transaction_pending/', views.transaction_pending, name='transaction_pending'),
    path('transaction_withdraw/', views.transaction_withdraw, name='transaction_withdraw'),
    path('transaction_deposit/', views.transaction_deposit, name='transaction_deposit'),
    path('transaction_completed/', views.transaction_completed, name='transaction_completed'),
    path('providers/', views.providers, name='providers'),
    path('subscription/', views.subscription, name='subscription'),
    path('subscripe_freelancer/', views.subscripe_freelancer, name='subscripe_freelancer'),
    path('reports/', views.reports, name='reports'),
    path('roles/', views.roles, name='roles'),
    path('roles_permission/', views.roles_permission, name='roles_permission'),
    path('skills/', views.skills, name='skills'),
    path('verify_identity/', views.verify_identity, name='verify_identity'),
    path('settings/', views.admin_settings, name='settings'),
    path('social_links/', views.social_links, name='social_links'),
    path('others_settings/', views.others_settings, name='others_settings'),
    path('seo_settings/', views.seo_settings, name='seo_settings'),
    path('social_settings/', views.social_settings, name='social_settings'),
    path('get_jobs_count/', views.get_jobs_count, name='get_jobs_count'),
    path('get_users_count/', views.get_users_count, name='get_users_count'),
]