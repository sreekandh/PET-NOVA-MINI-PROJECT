from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
   
    path('staff_info/',views.staff_info,name='staff_info'),
    path('trainer/',views.trainer_service,name='trainer_service'),
    path('caretaker/',views.caretaker_service,name='caretaker_service'),

]