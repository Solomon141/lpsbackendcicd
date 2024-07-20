from django.urls import path
from .views import UsersInGroup_OFFICERS, CreateUserView, BulkUser, LoginView, ALL_USERS
from .views import UserDetail

urlpatterns = [
    path('officers', UsersInGroup_OFFICERS.as_view()),
    path('allusers', ALL_USERS.as_view()),
    path('login', LoginView.as_view()),
    path('register', CreateUserView.as_view()),
    path('registerall', BulkUser.as_view()),
    path('user/<int:pk>', UserDetail.as_view(), name='user-detail'),
]