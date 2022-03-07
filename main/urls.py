from django.urls import path
from .views import *

app_name = 'Main'

urlpatterns = [
    path('', home_page, name='HomePage'),
    path('login/', login_page, name='Login'),
    path('register/', register_page, name='Register'),
    path('dashboard/edit-<slug:article_id>/', dashboard_page, name='Dashboard'),
    path('logout/', logout_page, name='Logout'),
    path('article/<uuid:article_id>/', view_page, name='Article'),
    path('del/<uuid:article_id>/', delete_article, name='Delete')
]
