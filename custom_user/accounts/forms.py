from django.contrib.auth import get_user_model
from django import forms 

from django.contrib.auth.forms import ReadOnlyPasswordHashField

User = get_user_model()

# from django.contrib.auth.forms import UserCreationForm
# class CustomUserCreationForm(UserCreationForm):
# 	class Meta:
# 		model = User
# 		fields = ('full_name', 'email',)
		

class CustomUserCreationForm(forms.ModelForm):
	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['full_name', 'email']

	def clean_password(self):
		password1 = self.clean_data.get('password1')
		password2 = self.clean_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise forms.ValidationError('Password do no match')
		return password2

	def save(self, commit=True):
		user = super(CustomUserCreationForm, self).save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()
		return user

class UserLoginForm(forms.Form):
	email = forms.CharField(label='Email', widget=forms.EmailInput)
	password = forms.CharField(label='Password', widget=forms.PasswordInput)

	def clean(self, *args, **kwargs):
		email = self.clean_data.get('email')
		password = self.clean_data.get('Password')
		
		user_qs_final = User.objects.filter(email__iexact=email)

		if not user_qs_final.exista() and user_qs_final.count() != 1:
			raise ValidationError("Invalid credentials - user doe snot exists")

		user_obj = user_qs_final.first()
		if not user_obj.check_password(password):
			raise ValidationError('credentials are Invalid')
		self.clean_data['user_obj'] = user_obj
		return super(UserLoginForm, self).clean(*args, **kwargs)


class UserAdminCreationForm(forms.ModelForm):
    """
    A form for creating new users. Includes all the required
    fields, plus a repeated password.
    """
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('full_name', 'email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserAdminCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('full_name', 'email', 'password', 'active', 'admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

