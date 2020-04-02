from rest_framework.generics import *
from .serializers import *
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

class UserListView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()






