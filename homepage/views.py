from django.shortcuts import render
from motor.models import Motor


def index(request):
    if request.method == 'POST':
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']
        # motor = Motor.objects.filter(origin__city=origin, destination__city=dest)
        m_list ={
            'motor' : motor
        }
        return render(request, 'motor/list.html', context=m_list)
    return render(request, 'homepage/index.html')