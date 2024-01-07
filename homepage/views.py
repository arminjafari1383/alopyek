from django.shortcuts import render
from motor.models import Motor


def index(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        motor = Motor.objects.filter(origin__city=origin, destination__city=dest)
        f_list ={
            'flights' : flights
        }
        return render(request, 'flights/list.html', context=f_list)
    return render(request, 'main_app/index.html')