from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from rest_framework import permissions, authentication, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
import requests
import json


@api_view(["GET", ])
@permission_classes((permissions.AllowAny,))
# @csrf_exempt
def token_login(request):
    if (not request.GET["username"]) or (not request.GET["password"]):
        return Response({"detail": "Missing username and/or password"}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=request.GET["username"], password=request.GET["password"])
    if user:
        if user.is_active:
            login(request, user)
            try:
                my_token = Token.objects.get(user=user)
                username = user.username
                return Response({"token": "{}".format(my_token.key), "username": "{}".format(username)},
                                status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"detail": "Could not get token"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "Inactive account"}, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"detail": "Invalid User Id of Password"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", ])
@login_required
@permission_classes((permissions.IsAuthenticated,))
@authentication_classes((authentication.TokenAuthentication, authentication.SessionAuthentication))
def tm_get_events(request):
    """
    Make a GET request to the ticketmaster API with the strings entered by the user
    :param request: Incoming request search and city string
    :return: Result in Json
    """

    search = request.query_params.get("search", "")
    if search:
        search = search.lower()

    city = request.query_params.get("city", "")
    if city:
        city = city.lower()

    date_time = datetime.now() + timedelta(days=7)

    end_date_time = datetime.strftime(date_time, "%Y-%m-%dT00:00:00Z")

    base_url = 'https://app.ticketmaster.com/discovery/v2/'
    tm_key = 'BabzejjEdlmaAhyC7DoWWAYyb8u66r5u'

    try:
        response = requests.get(base_url + 'events.json?classificationName=' + search +
                                '&city=' + city + '&endDateTime=' + end_date_time + '&apikey=' + tm_key)
        response_content = json.loads(response.content)
        response_list = response_content['_embedded']['events']

        event_list = []
        for item in response_list:

            event = {
                "name": item['name'],
                "url": item['url'],
                "image": item['images'][0]['url'],
                "date": item['dates']['start']['localDate'],
                "time": item['dates']['start']['localTime'],
                "location": item['_embedded']['venues'][0]['location']
            }
            event_list.append(event)

        return Response(event_list, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({"detail": e}, status=status.HTTP_400_BAD_REQUEST)

