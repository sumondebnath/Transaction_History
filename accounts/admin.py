# from typing import Any
from django import forms
from django.contrib import admin
# from django.contrib.auth.models import Group
from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.core.exceptions import ValidationError

from accounts.models import CustomUser

# Register your models here.

class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password Does Not Matched!")
        
        return password2
    
    def save(self, commit=True):
        user = super().save(commit=False)

        user.set_password(self.cleaned_data["password1"])

        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta: 
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email", "password", "is_active", "is_admin"]



class UserAdmin(admin.ModelAdmin):
# class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ["username", "first_name", "last_name", "email", "is_admin"]
    # list_filter = ["is_admin"]

    # fieldsets = [
    #     (None, {"fields": ["email", "password"]}),
    #     # ("Personal info", {"fields": ["date_of_birth"]}),
    #     ("Permissions", {"fields": ["is_admin"]}),
    # ]
    # add_fieldsets = [
    #     (
    #         None,
    #         {
    #             "classes": ["wide"],
    #             "fields": ["email", "password1", "password2"],
    #         },
    #     ),
    # ]
    # search_fields = ["email"]
    # ordering = ["email"]
    # filter_horizontal = []


admin.site.register(CustomUser, UserAdmin)

# admin.site.unregister(Group)