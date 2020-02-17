# from django.shortcuts import render,redirect
# from .forms import regForm,logform
# from django.http import HttpResponse
# from .models import reg
# from myapp import forms
# from .forms import contactForm
# from django.views.generic import FormView
# from django.core.exceptions import ValidationError
# # Create your views here.
#
# class contact(FormView):
#     form_class = contactForm
#     template_name = 'form.html'
#     success_url = '/'
# def regis(request):
#      form=regForm()
#      if request.method =='POST':
#          form=regForm(request.POST)
#          if form.is_valid():
#              form.save()
#              return redirect('/login/')
#          else:
#              return HttpResponse('error')
#      return render(request,'index.html',{'forms':form})
#
# def log(request):
#     form = logform()
#     if request.method=='POST':
#          form=logform(request.POST)
#          if form.is_valid():
#             un=request.POST.get('UserName')
#             pw=request.POST.get('Password')
#             em=request.POST.get('mail')
#             ev = request.POST.get('even_field')
#
#             db=reg.objects.filter(UserName=un,Password=pw,Mail=em,even_field=ev)
#             if db:
#                 return HttpResponse("validation are succes")
#             else:
#                 return HttpResponse('error')
#
#     # else:
#     #     form=logform(request.POST)
#     return render(request,'login.html',{'form':form})
#
#
# def deepak(request):
#     form=forms.rahul()
#     if request.method=='POST':
#         form=forms.rahul(request.POST)
#     if form.is_valid():
#         print("validation are succes")
#         print(form.cleaned_data['Name'])
#         print(form.cleaned_data['Salary'])
#     return render(request,'myapp/mypage.html',{'form':form})
#
#
#
# # def changepassword(request):
# #     if request.method=='GET':
# #         #form = employeedetails.objects.filter(employee_id=request.session['user']['id'])
# #         return render(request, 'changepassword.html', {'forms': form})
# #     if request.method=='POST':
# #         try:
# #             form = employeedetails.objects.get(employee_password=request.POST['oldpass'],employee_id=request.session['user']['id'])
# #             if request.POST['newpass'] == request.POST['confirmpass']:
# #                 form.employee_password=request.POST['newpass']
# #                 form.save()
# #                 #messages.add_message(request, messages.SUCCESS, "password updated succesfully!")
# #                 return redirect('/dashboard/')
# #         except:
# #             #messages.add_message(request, messages.SUCCESS, "please enter correct password ")
# #             return redirect('/changepsw/')



from django.shortcuts import render, redirect
from django.contrib import messages
from . import forms
from . import models
from django.http import HttpResponse
import bcrypt

def login(request):
    if 'user_id' not in request.session:
        context = {}

        if request.method == "POST" and 'password2' in request.POST:
            reg_Form = forms.regForm(request.POST or None)
            context.update({'regForm': reg_Form})

            if reg_Form.is_valid():
                print
                "It is inside valid"
                print
                ("errors")
                reg_Form.save()

        else:
            form = forms.loginForm(request.POST or None)
            context.update({'loginForm': form})
            if form.is_valid():
                user_info = models.login(form.cleaned_data['user_name'], form.cleaned_data['password'])
                if user_info == "wrong":
                    messages.error(request, 'Username or Password is invalid.')
                else:
                    request.session['user_id'] = user_info[0]['id']

        return render(request, 'index.html', context)

    else:
        return redirect('/')

        # else:
        #     form = forms.loginForm(request.POST or None)
        #     context.update({'loginForm':form})
        #     if form.is_valid():
        #         user_info = models.login(form.cleaned_data['user_name'], form.cleaned_data['password'])
        #         if user_info == "wrong":
        #             messages.error(request, 'Username or Password is invalid.')
        #         else:
        #             request.session['user_id'] = user_info[0]['id']

    #     return render(request, 'index.html',{'context':context})
    #
    # else:
    #     return redirect('/')


def login1(request):
    context=forms.loginForm()
    if 'user_id' not in request.session:


        form = forms.loginForm(request.POST or None)

        if form.is_valid():
            user_info = form.cleaned_data['user_name'], form.cleaned_data['password']
            if user_info == "wrong":
                messages.error(request, 'Username or Password is invalid.')
            else:
                 return HttpResponse('s')



    return render(request, 'index.html', {'context':context})

