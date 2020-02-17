# from django import forms
# from .models import reg
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email,validate_slug
# from django.core import validators
#
#
# def Name_Begin_Values(value):
#     if value[0] != 'R':
#         raise forms.ValidationError("sorry first char must be S")
#
#
# class contactForm(forms.Form):
#     mail = forms.EmailField()
#     content=forms.CharField(widget=forms.Textarea())
#     slug_field = forms.CharField()
#
#     # def clean_mail(self):
#     #     email_passed=self.cleaned_data.get("mail")
#     #     email_req="rahul.com"
#     #     if not email_req in email_passed:
#     #         raise forms.ValidationError("not a valid mail")
#     #     return email_passed
#     def clean(self):
#         cleaned_data=super(contactForm,self).clean()
#         email_passed = cleaned_data.get("mail")
#         email_req = "rahul.com"
#         if not email_req in email_passed:
#             raise forms.ValidationError("not a valid mail")
#
#         return email_passed
# class regForm(forms.ModelForm):
#     class Meta:
#         model=reg
#         fields='__all__'
# # def user(value):
# #     if value.isalnum()!=True:
# #         raise forms.ValidationError("not ")
#
# def validate_even(value):
#     if value % 2 != 0:
#         raise forms.ValidationError(
#             ('%(value)s is not an even number'),
#             # params={'value': value},
#         )
#
#
# def Name_Begin_Value(value):
#         if value[0]!='R':
#             raise forms.ValidationError("sorry first char must be S")
#
#
# class logform(forms.Form):
#     UserName=forms.CharField(validators=[Name_Begin_Value])
#     Password=forms.CharField(widget=forms.PasswordInput)
#     mail=forms.EmailField()
#     even_field =forms.IntegerField(validators=[validate_even])
#
#
# #     def Name_Begin_Value(value):
# #         if value[0] != 'S':
# #             raise forms.ValidationError("sorry first char must be S")
# #
# #
# # class rahul(forms.Form):
# #     Name = forms.CharField(validators=[Name_Begin_Value])
# #     Salary = forms.IntegerField()
# #     opinion = forms.CharField(widget=forms.Textarea,
# #                               validators=[validators.MaxLengthValidator(30), validators.MinLengthValidator(10)])




from django import forms
from .models import User
from django.core.exceptions import ValidationError
import bcrypt
from django.db.models import Q

class loginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['user_name', 'password']
        #exclude = ['full_name', 'email']
        widgets = {
        'password': forms.PasswordInput(),
    }


CHOICES = [('Male', 'male'),('female', 'female')]

class regForm(forms.ModelForm):
    password2 = forms.CharField(max_length=100, label="Comfirm password", required=True, widget=forms.PasswordInput())
    postal_code = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect())

    class Meta:
        model = User

        fields = ['full_name', 'user_name', 'email','postal_code', 'paid','password']
        widgets = {
        'password': forms.PasswordInput(),
        }

    def clean(self):
        if self.cleaned_data['password'] != self.cleaned_data['password2']:
            print ("Passwords do not match")
            raise forms.ValidationError("Passwords do not match")
        else:
            user = User.objects.filter(Q(user_name=self.cleaned_data['user_name']) | Q(email=self.cleaned_data['email']))
            if user:
                print ("Username or Email already in use")
                raise forms.ValidationError("Username or Email already in use")
            else:
                print ("hashing password")
                unhashed_passwd = self.cleaned_data['password'].encode()
                self.cleaned_data['password'] = bcrypt.hashpw(unhashed_passwd, bcrypt.gensalt())
        #return (regForm, self).clean(*args, **kwargs)