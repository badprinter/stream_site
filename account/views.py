from django.shortcuts import render
from rest_framework.views import APIView

from .form import AccountLoginForm, AccountSignUpForm


class UserLogin(APIView):
    def get(self,request):
        form = AccountLoginForm()
        return render(request,'account/login.html',{'form':form})

class UserSignup(APIView):
    def get(self, request):
        form = AccountSignUpForm()
        return render(request,'account/signup.html',{'form':form})