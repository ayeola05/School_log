from django.shortcuts import render
from django.urls import reverse_lazy
from basic_app.models import Profile
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.

class HomeView(TemplateView):
	template_name = 'basic_app/home.html'

class ProfileListView(ListView):
	model = Profile

class ProfileDetailView(DetailView):
	model = Profile

class ProfileCreateView(CreateView):
	model = Profile
	fields = '__all__'

class ProfileUpdateView(UpdateView):
	model = Profile
	fields = '__all__'

class ProfileDeleteView(DeleteView):
	model = Profile
	context_object_name = 'profile_delete'
	success_url = reverse_lazy('basic_app:list') 