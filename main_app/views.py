from django.shortcuts import render


# baby step - usually a Model is used
mountains = [
  {'name': 'Katahdin', 'state': 'Maine', 'datehiked': '2017', 'elevation': 5269},
  {'name': 'Mount Bigelow (West Peak)', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4145},
  {'name': 'Mount Bigelow (Avery Peak)', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4090},
  {'name': 'Crocker Mountain', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4228},
  {'name': 'South Crocker Mountain', 'state': 'Maine', 'datehiked': '2017', 'elevation': 4050},
]

# Create your views here.
def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def mountains_index(request):
    return render(request, "mountains/index.html", {
        'mountains': mountains
    })
