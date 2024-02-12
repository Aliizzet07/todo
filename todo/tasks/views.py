from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth import logout
from .models import*
from .forms import*
from django.contrib.auth.views import LoginView , LogoutView

from tasks.api.serializer import TaskSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



class CustomLoginView(LoginView):
    template_name = 'tasks/base.login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


@api_view(['GET'])
def completed_tasks(request):
     tasks = Task.objects.filter(complete=True)
     serializer=TaskSerializer(tasks,many=True)
     return Response(serializer.data)

@api_view(['GET'])
def uncompleted_tasks(request):
     tasks = Task.objects.filter(complete=False)
     serializer=TaskSerializer(tasks,many=True)
     return Response(serializer.data)


@api_view(['POST'])
def tasks_post(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
@api_view(['POST'])
def updateTask(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['DELETE'])
def deleteTask(request, id):
        try:
            tasks = Task.objects.get(pk=id)
            tasks.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)




def user_logout(req):
    logout(req)
    return redirect('base.login')