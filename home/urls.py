from django.urls import path
from.import views

urlpatterns = [
    path('admini',views.index,name="index"),
    path('signup.html',views.signup,name="signup"),
    path('',views.loginn,name="login"),
    


]