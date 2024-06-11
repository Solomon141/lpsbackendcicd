# from django.urls import path

# urlpatterns = [
#     path('login', LoginView.as_view()),
#     path('register', RegisterView.as_view()),
#     path('registerall', RegisterView.as_view()),
# ]


from django.urls import path
from .views import UsersInGroup_OFFICERS, CreateUserView, BulkUser, LoginView, ALL_USERS

urlpatterns = [
    path('officers', UsersInGroup_OFFICERS.as_view()),
    path('allusers', ALL_USERS.as_view()),
    path('login', LoginView.as_view()),
    path('register', CreateUserView.as_view()),
    path('registerall', BulkUser.as_view()),
]