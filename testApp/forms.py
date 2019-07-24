from django import forms
from django.core import validators
from django.contrib.auth.models import User
from testApp.models import UserProfileInfo
# custom validators
def check_name(value):
    if value[0].lower() != "s":
        raise forms.ValidationError("Letter must  be starts with 'S' ")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site','profile_pic')

class simpleForm(forms.Form):
    name = forms.CharField(validators=[check_name])
    email = forms.EmailField()
    verify_email = forms.EmailField(label="Enter email correct")
    address = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False,widget=forms.HiddenInput) #validators=[validators.MaxValueValidator(0)]

    def clean(self):
        print("here clean method Excutes!..")
        total_clean_data = super().clean()
        email = total_clean_data['email']
        verify_email = total_clean_data['verify_email']
        if email != verify_email:
            raise forms.ValidationError("enter emial correctly!..")
# hi sankar
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError("OH bot catched!..")
