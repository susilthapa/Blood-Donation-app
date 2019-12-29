from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import (
    UserRegistrationForm,
    UserUpdateForm,
    ProfileUpdateForm
)
from django.contrib import messages
from django.views.generic import TemplateView


# class RegisterView(TemplateView):
#     template_name = './register.html'
#
#     def post(self, request, *args, **kwargs):
#         form = UserRegistrationForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account for {username} has been created! now you are now able to login')
#             return redirect('login')
#
#         else:
#             form = UserRegistrationForm()
#         return render(request, './register.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        if form.is_valid():
            form.save()
            # user = form.save()
            # user.refresh_from_db()
            # user.profile.terms_and_conditions = form.cleaned_data.get('terms_and_conditions')
            # user.profile.age = form.cleaned_data.get('age')
            # user.profile.blood_group = form.cleaned_data.get('blood_group')
            # user.profile.phone_number = form.cleaned_data.get('phone_number')
            # user.profile.terms_and_conditions = form.cleaned_data.get('terms_and_conditions')
            # user.profile.latitude = form.cleaned_data.get('latitude')
            # user.profile.longitude = form.cleaned_data.get('longitude')
            #
            # print(f'TERMS AND CONDITIONS = {user.profile.terms_and_conditions}')
            # user.save()
            username = form.cleaned_data.get('username')

            messages.success(request, f'Account for {username} has been created! now you are now able to login')
            return redirect('login')
    else:
        # print('FORM IS NOT POST!!')
        form = UserRegistrationForm()

    return render(request, './register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   instance=request.user.profile)
        if p_form.is_valid() and u_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f' Your Account has been UPDATED!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, './profile.html', context)


