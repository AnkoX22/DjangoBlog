from django.urls import path
from django.contrib.auth import views as auth_views
from .views import SignUpView, RegisterView, CustomLoginView, ResetPasswordView, profile, ChangePasswordView
from mysite import settings
from django.conf.urls.static import static


urlpatterns = [
    path("signup/", RegisterView.as_view(), name="signup"),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='registration/login.html')),
    path('password_reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', profile, name='user-profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)