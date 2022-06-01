from http.client import HTTPResponse
from django.shortcuts import render
from django.views.generic import (View,
                                TemplateView,
                                ListView,
                                DetailView,
                                CreateView,
                                UpdateView,
                                DeleteView,)
from app1.models import School,Student
from django.urls import reverse_lazy
# Create your views here.

"""class CBView(View):
    def get(self,request):
        return HttpResponse("welcome")

class CBView2(View):
    def get(self,request):
        return HttpResponse("app1 page")"""

class TemplateViewIndex(TemplateView):
    template_name= "app1/index.html"

"""    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = "Django Data"
        return context"""

class SchoolListView(ListView):
    context_object_name = 'schools'
    model = School
    template_name = 'app1/schoollist.html'

class SchoolDetailView(DetailView):
    context_object_name = 'schoolDetails'
    model = School
    template_name = 'app1/schooldetail.html'

class SchoolCreateView(CreateView):
    model = School
    fields = ('name','principal','loc')

class SchoolUpdateView(UpdateView):
    fields = ('name','principal')
    model = School

class SchoolDeleteView(DeleteView):
    model = School
    success_url = reverse_lazy("app1:list")

