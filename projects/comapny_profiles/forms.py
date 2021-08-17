from django import forms
from models import Employee, Manager

class ManagerForm(forms.ModelForm):
    class Meta:
        model = Manager
        fields = "__all__"

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
