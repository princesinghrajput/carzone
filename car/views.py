from django.shortcuts import render, get_object_or_404
from car.models import Car
# Create your views here.
def cars(request):
    cars = Car.objects.order_by("-created_date")
    data = {
        'cars': cars,
    }
    return render(request, 'car/cars.html', data)

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id) #take th primary key and get the data from the database
    data = {
        'single_car': single_car,
    }
    return render(request, 'car/car_detail.html',data)

