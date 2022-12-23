from django.urls import path


from .views import AcceuilView, UpdateUserView

urlpatterns = [
    path('acceuil', AcceuilView.as_view(), name='acceuil'),
    path('update', UpdateUserView.as_view(), name='update-user'),
]