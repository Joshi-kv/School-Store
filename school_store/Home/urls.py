from django.urls import path
from . import views

urlpatterns = [
    path('',views.home_page,name='home'),
    path('contact/',views.contact,name='contact'),
    path('enquiry/',views.enquiry,name='enquiry'),
    path('get_courses/<int:dpt_id>',views.get_courses,name='get_courses'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout')
]
