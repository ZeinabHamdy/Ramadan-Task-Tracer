from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django import forms


class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(
        label='confirm_Password',
        widget=forms.PasswordInput(),
        required=True,
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        widgets = {
            'password': forms.PasswordInput(),
            'confirm_password': forms.PasswordInput(),
        }
        
    
    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        errors = {}
        if User.objects.filter(username=username).exists():
            errors['username'] = 'اسم المستخدم موجود بالفعل'
        if User.objects.filter(email=email).exists():
            errors['email'] = 'البريد الإلكتروني موجود بالفعل'
        if password and confirm_password and password != confirm_password:
            errors['password'] = []
            errors['password'].append('كلمة المرور غير متطابقة')
        if password and len(password) < 8:
            if 'password' not in errors:
                errors['password'] = []
            errors['password'].append('كلمة المرور يجب أن تكون 8 أحرف على الأقل')

        if errors:
            raise ValidationError(errors)
        return cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=25,
        label='Username',
        required=True,
    )
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label='Password',
        required=True,
    )