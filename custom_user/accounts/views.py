from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views import View

from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .tokens import account_activation_token



class SignUpView(CreateView):
	form_class = CustomUserCreationForm
	template_name = 'accounts/register.html'

	def form_valid(self, form):
		user = form.save(commit=False)

		# user.is_active = False
		user.save()

		current_site = get_current_site(self.request)
		to = request.get('email')
		subject = 'Active Your Project Zero account'
		message = render_to_string('emails/account_activation_email.html',{
					'user': user,
					'domain': current_site.domain,
					'uid': urlsafe_base64_encode(force_byte(user.pk)),
					'token': account_activation_token.make_token(user),
					})
		user.email_user(subject, message)

		messages.success(request, ('Please Confirm your email to complete registration.'))	

		return redirect('login')


class ActivateAccount(View):

    def get(self, request, uidb64, token, *args, **kwargs):
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None

        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.email_confirmed = True
            user.save()
            messages.success(request, ('Your account have been confirmed.'))
            return redirect('login')
        else:
            messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
            return redirect('register')

	

