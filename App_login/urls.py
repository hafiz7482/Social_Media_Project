from django.urls import path
from django.contrib.auth import views as auth_view
from App_login import views
from App_login.forms import MyPasswordChangeForm, MyPasswordResetForm, MySetPasswordForm

app_name = "App_login"

urlpatterns = [
    path('registration/', views.RegistrationView, name='registration'),
    path('login/', views.LoginView, name='login'),
    path('profile-edit/', views.edit_profile, name='edit'),
    path('logout/', views.Logout, name='logout'),
    path('profile/', views.ProfileDetails, name='profile'),
    path('user-info/<username>/', views.UserInfo, name='user_info'),
    path('follow/<username>/', views.FollowView, name='follow'),        
    path('unfollow/<username>/', views.UnFollowView, name='unfollow'),

# Change password
    path('password-change/', auth_view.PasswordChangeView.as_view(template_name='App_login/change_password.html', form_class=MyPasswordChangeForm, success_url='/accounts/passwordchangedone'), name = 'passwordchange'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name='App_login/password_change_done.html'),name='passwordchangedone'),

# Reset Password
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='App_login/password_reset.html',form_class=MyPasswordResetForm), name = 'password_reset' ),
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view(template_name='App_login/password_reset_done.html'), name = 'password_reset_done' ),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view(template_name='App_login/password_reset_confirm.html', form_class= MySetPasswordForm), name = 'password_reset_confirm' ),
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view(template_name='App_login/password_reset_complete.html'), name = 'password_reset_complete' ),


]
