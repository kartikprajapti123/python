from django.urls import path
from app import views
urlpatterns=[
    path('',views.index,name="kartik"),
    path('<int:id>/',views.details,name="kartik"),
    
]