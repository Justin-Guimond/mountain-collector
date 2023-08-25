from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mountain

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def mountains_index(request):
    mountains = Mountain.objects.all()
    return render(request, "mountains/index.html", {
        'mountains': mountains
    })

def mountains_detail(request, mountain_id):
    mountain = Mountain.objects.get(id=mountain_id)
    return render(request, 'mountains/detail.html', {
        'mountain': mountain
    })

class MountainCreate(CreateView):
    model = Mountain
    fields = '__all__'

    def form_valid(self, form):
        # self.request.user is the logged in user
        form.instance.user = self.request.user
        return super().form_valid(form)

class MountainUpdate(UpdateView):
    model = Mountain
    fields = '__all__'

class MountainDelete(DeleteView):
    model = Mountain
    success_url = '/mountains'