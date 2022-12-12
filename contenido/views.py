from django.shortcuts import render
from django.views.generic import CreateView
from django.shortcuts import redirect
from .forms import NewUserForm

# Create your views here.
class RegisterView(CreateView):
  template_name = "registration/register.html"
  form_class = NewUserForm

  def form_valid(self, form):
      form.save()
      return redirect('login')