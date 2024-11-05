
from django.urls import path ,include
from country import views

urlpatterns = [
 
    path('',views.countries_list,name='countries_list'),
    path('/<str:country_code>', views.country_detail, name='country_detail'),

]
