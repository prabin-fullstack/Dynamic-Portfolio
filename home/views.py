from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from.models import Technology,SkillCategory,Project,Contact
from .serializer import TechnologySerializer,SkillCategorySerializer,ProjectSerializer,ContactSerializer
# Create your views here.



class SkillCategoryAPIView(APIView):
    def get(self,request):
        skills = SkillCategory.objects.all()
        serialaizer = SkillCategorySerializer(skills,many=True)
        
        return Response(serialaizer.data)
    

class ProjectAPIView(APIView):
    def get(self,request):
        project = Project.objects.all()
        serializer = ProjectSerializer(project,many=True,context={"request": request})
        
        return Response(serializer.data)
    

class ContactAPIView(APIView):
    def post(self,request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(
                {"message": "Message sent successfully"},
                status=status.HTTP_201_CREATED )
            
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )