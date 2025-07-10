from django.urls import path
from .views.main_views import index,createlist,editlist,deletelist
from .views.auth_views import login_page,register_page,logoutpage

urlpatterns = [
    
        path('',index,name='index'),
        path('register/',register_page,name='register_page'),
        path('login/',login_page,name='login_page'),
        path('createlist/',createlist,name='createlist'),
        path('logout/',logoutpage,name='logoutpage'),
        path('editlist/<int:id>/',editlist,name='editlist'),
        path('deletelist/<int:id>/',deletelist,name='deletelist'),
]