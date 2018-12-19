from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from . import models
# Create your views here.
class Template_views(TemplateView):
    template_name = 'first/index.html'

class School_Listview(ListView):
    context_object_name = 'schools'
    model =models.School
    template_name = 'first/list_view.html'



class School_detailview(DetailView):
    context_object_name = 'school_details'
    model = models.School
    #template_name = 'first/school_details.html'

class SchoolCreateView(CreateView):
    fields = ('name','principal','location')
    model = models.School

class SchoolUpdateView(UpdateView):
    fields =('name','principal')
    model = models.School

class SchoolDeleteView(DeleteView):
    success_url = reverse_lazy('first:list')
    model = models.School
