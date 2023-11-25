
from django.urls import path
from . import views
from .views import success_page


urlpatterns = [
    path('', views.index, name='index'),  # This is the root URL
    path('polling_unit/<int:polling_unit_uniqueid>/',
         views.polling_unit_result, name='polling_unit_result'),
    path('lga_summed_result/', views.lga_summed_result, name='lga_summed_result'),
    path('store_polling_unit_result/', views.store_polling_unit_result,
         name='store_polling_unit_result'),
    path('success/', success_page, name='success_page'),

]
