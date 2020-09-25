from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from .models import Widget

# from .forms import WidgetForm
# Create your views here.

def home(request):
    widgets = Widget.objects.all()
    return render(request, 'index.html', {'widgets': widgets})

# def add_widget(request, widget_id):
#     form = WidgetForm(request.POST)
#     if form.is_valid():
#         new_widget = form.save(commit=False)
#         new_widget.widget_id = widget_id
#         new_widget.save()
#     return redirect('index', widget_id=widget_id)

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'
    success_url = '/'

class WidgetDelete(DeleteView):
    model = Widget
    success_url = '/'