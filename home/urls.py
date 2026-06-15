from django.urls import path
from . import views
urlpatterns = [
   path('skills/',views.SkillCategoryAPIView.as_view()),
   path('project/',views.ProjectAPIView.as_view()),
   path('contact/',views.ContactAPIView.as_view()),
]