from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Mountain

# baby step - usually a Model is used
# mountains = [
#   {'name': 'Katahdin', 'state': 'Maine', 'datehiked': '2017', 'elevation': 5269},
#   {'name': 'Mount Bigelow (West Peak)', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4145},
#   {'name': 'Mount Bigelow (Avery Peak)', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4090},
#   {'name': 'Crocker Mountain', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4228},
#   {'name': 'South Crocker Mountain', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4050},
# ]

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

class MountainUpdate(UpdateView):
    model = Mountain
    fields= '__all__'

class MountainDelete(DeleteView):
    model = Mountain
    success_url = '/mountains'