from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import FreelancerPasswordResetConfirmView

urlpatterns = [
    path('', views.index, name='index'),
    path('index_2/', views.index_2, name='index_2'),
    path('404_page/', views.error_404, name='error_404'),
    path('telegram_conversation/', views.telegram_conversation, name='telegram_conversation'),
    path('about/', views.about, name='about'),
    path('User_logout/', views.User_logout, name='User_logout'),
    path('blog_grid/', views.blog_grid, name='blog_grid'),
    path('cancelled_projects/', views.cancelled_projects, name='cancelled_projects'),
    path('change_password/', views.change_password, name='change_password'),
    path('chats/', views.user_chat, name='chats'),
    path('check-room/<str:pk>', views.create_check_room, name="check-room"),
    path('messages_view/<int:user_id>/<int:room_id>', views.messages_view, name='messages_view'),
    path('company_details/', views.company_details, name='company_details'),
    path('company_gallery/<int:employer_id>/', views.company_gallery, name='company_gallery'),
    path('company_profile/<int:employer_id>/', views.company_profile, name='company_profile'),
    path('company_project/<int:employer_id>/', views.company_project, name='company_project'),
    path('company_review/<int:employer_id>/', views.company_review, name='company_review'),
    path('completed_projects/', views.completed_projects, name='completed_projects'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete_account/', views.delete_account, name='delete_account'),
    path('deposit_funds/', views.deposit_funds, name='deposit_funds'),
    path('developer_list/', views.developer_list, name='developer_list'),
    path('developer_profile/', views.developer_profile, name='developer_profile'),
    path('developer/', views.developer, name='developer'),
    path('edit_project/', views.edit_project, name='edit_project'),
    path('faq/', views.faq, name='faq'),
    path('favourites/', views.favourites, name='favourites'),
    path('favourites_list/', views.favourites_list, name='favourites_list'),
    path('invited_favourites/', views.invited_favourites, name='invited_favourites'),
    path('files/', views.files, name='files'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset/<uidb64>/<token>/', FreelancerPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('freelancer_bookmarks/', views.freelancer_bookmarks, name='freelancer_bookmarks'),
    path('freelancer_cancelled_projects/', views.freelancer_cancelled_projects, name='freelancer_cancelled_projects'),
    path('freelancer_change_password/', views.freelancer_change_password, name='freelancer_change_password'),
    path('freelancer_completed_projects/', views.freelancer_completed_projects, name='freelancer_completed_projects'),
    path('freelancer_dashboard/', views.freelancer_dashboard, name='freelancer_dashboard'),
    path('freelancer_chart/<int:freelancer_id>/', views.freelancer_chart, name='freelancer_chart'),
    path('freelancer_delete_account/', views.freelancer_delete_account, name='freelancer_delete_account'),
    path('freelancer_favourites/', views.freelancer_favourites, name='freelancer_favourites'),
    path('freelancer_files/', views.freelancer_files, name='freelancer_files'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('freelancer_invitation/', views.freelancer_invitation, name='freelancer_invitations'),
    path('freelancer_invoices/', views.freelancer_invoices, name='freelancer_invoices'),
    path('freelancer_membership/', views.freelancer_membership, name='freelancer_membership'),
    path('freelancer_milestones/', views.freelancer_milestones, name='freelancer_milestones'),
    path('freelancer_ongoing_projects/', views.freelancer_ongoing_projects, name='freelancer_ongoing_projects'),
    path('freelancer_payment/', views.freelancer_payment, name='freelancer_payment'),
    path('freelancer_portfoilo/', views.freelancer_portfoilo, name='freelancer_portfoilo'),
    path('freelancer_profile_settings/', views.freelancer_profile_settings, name='freelancer_profile_settings'),
    path('freelancer_profile/<int:freelancer_id>/', views.freelancer_profile, name='freelancer_profile'),
    path('freelancer_review/', views.freelancer_review, name='freelancer_review'),
    path('freelancer_task/', views.freelancer_task, name='freelancer_task'),
    path('freelancer_transaction_history/', views.freelancer_transaction_history, name='freelancer_transaction_history'),
    path('freelancer_verify_identity/', views.freelancer_verify_identity, name='freelancer_verify_identity'),
    path('freelancer_view_project_detail/', views.freelancer_view_project_detail, name='freelancer_view_project_detail'),
    path('freelancer_withdraw_money/', views.freelancer_withdraw_money, name='freelancer_withdraw_money'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('javascript;/', views.javascript, name='javascript'),
    path('manage_projects/', views.manage_projects, name='manage_projects'),
    path('membership_plans/', views.membership_plans, name='membership_plans'),
    path('onboard_screen_employer/', views.onboard_screen_employer, name='onboard_screen_employer'),
    path('onboard_screen/', views.onboard, name='onboard_screen'),
    path('ongoing_projects/', views.ongoing_projects, name='ongoing_projects'),
    path('pending_projects/', views.pending_projects, name='pending_projects'),
    path('post_project/', views.project_form, name='post_project'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('profile_settings/', views.profile_settings, name='profile_settings'),
    path('project_payment/', views.project_payment, name='project_payment'),
    path('project_proposals/<int:job_id>/', views.project_proposals, name='project_proposals'),
    path('freelancer_project_proposals', views.freelancer_project_proposals, name='freelancer_project_proposals'),
    path('project/', views.project, name='project'),
    path('project_details/<int:project_id>/', views.project_details, name='project_details'),
    path('review/', views.review, name='review'),
    path('delete_review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('tasks/', views.tasks, name='tasks'),
    path('invoices/', views.invoices, name='invoices'),
    path('term_condition/', views.term_condition, name='term_condition'),
    path('user_account_details/', views.user_account_details, name='user_account_details'),
    path('verify_identity/', views.verify_identity, name='verify_identity'),
    path('video_call/', views.video_call, name='video_call'),
    path('view_invoice/', views.view_invoice, name='view_invoice'),
    path('view_project_detail/', views.view_project_detail, name='view_project_detail'),
    path('voice_call/', views.voice_call, name='voice_call'),
]



