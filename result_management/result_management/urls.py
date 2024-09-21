from django.contrib import admin
from django.urls import path
from results import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('results/', views.student_results, name='student_results'),
]
