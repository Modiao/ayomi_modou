from django.urls import path


from .views import LoginView, LogoutView

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('Logout', LogoutView.as_view(), name='logout'),

]