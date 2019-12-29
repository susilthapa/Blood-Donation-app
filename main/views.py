from django.shortcuts import render, get_object_or_404
# from users.forms import SearchBloodForm
from users.models import Profile
from django.contrib import messages
from django.views.generic import TemplateView
from math import radians, cos, sin, asin, sqrt
from haversine import haversine, Unit


def home(request):
    # print(f'USER = {current_user}')
    return render(request, './home.html')


donors = []
# donors_in_10km = []


class SearchView(TemplateView):
    template_name = './home.html'

    def post(self, request, *args, **kwargs):
        donors.clear()
        print(f'DONOR IN 5KM ARRAY INSIDE POST = {donors}')
        blood_group = request.POST.get('blood_group')
        if not blood_group:
            messages.error(request, 'Select Blood Group')
            return render(request, './home.html')
        radius = int(request.POST.get('radius'))
        print(f'PRINT EXTEND = {radius}')
        print(f'BLOOD GROUP = {blood_group}')
        destination_user = Profile.objects.filter(blood_group=blood_group).exclude(user=request.user)
        # destination_user = Profile.objects.filter(user=request.user)
        print(f'Users with matching blood group: {destination_user}')

        current_user = Profile.objects.get(user=request.user)

        source_lat = current_user.latitude
        source_lon = current_user.longitude
        # print(f'SOURCE_LAT = {source_lat}')
        context = {}

        for dest_user in destination_user:
            print(dest_user)
            print(f'DESTINATION BLOOD GROUP = {dest_user.blood_group}')
            lat2 = dest_user.latitude
            print(f'DESTINATION LAT = {lat2}')
            lon2 = dest_user.longitude
            source = (source_lat, source_lon)
            destination = (lat2, lon2)
            distance = haversine(source, destination)
            print(f'RESULT = {distance}')

            if distance <= radius:
                # if dest_user not in donors_in_5km:
                donors.append(dest_user)
                print(f'USERS in {radius}km distance = {donors}')
                title = f'Information of donor within {radius}km radius'

                distance = round(distance, 2)
                context = {
                    'donors': donors,
                    'distance': distance,
                    'title': title,
                    'blood_group': blood_group
                }
        if donors:
            messages.success(request, f'Found Donor of Blood Group {blood_group} within {radius}km range:')
        else:
            messages.error(request, f'Donor with blood group {blood_group} not found!')
        return render(request, './home.html', context)
