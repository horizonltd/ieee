from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (HTTP_200_OK, HTTP_400_BAD_REQUEST,
                                   HTTP_404_NOT_FOUND)

from rest_framework.response import Response
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from resources.models import Downloads





def advice(request):
    template = loader.get_template('advice.html')
    context = {
        'downloads': Downloads.objects.all()

    }
    return HttpResponse(template.render(context, request))


class HomePage(TemplateView):

    template_name = 'index.html'

class Advice(TemplateView):

    template_name = 'advice.html'


    def advice(request):
        template = loader.get_template('advice.html')
        context = {
            'downloads': Downloads.objects.all()

        }
        return HttpResponse(template.render(context, request))




# This view are from templates folder
class ThanksPage(TemplateView):
    template_name = "thanks.html"


class TestPage(TemplateView):
    template_name = "test.html"












@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
# @csrf_exempt
# @api_view(["GET"])
# def sample_api(request):
#     data = {'sample_data': 123}
#     return Response(data, status=HTTP_200_OK)