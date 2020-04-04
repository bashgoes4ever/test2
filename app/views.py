from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import *


class AppView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.GET.get('id'):
            if request.GET.get('api_key'):
                app = Application.objects.get(id=request.GET.get('id'))
                if app.api_key == request.GET.get('api_key'):
                    return Response(AppSerializer(app).data)
                else:
                    return Response({
                        'status': 403,
                        'message': 'Wrong Api Key'
                    })
            else:
                return Response({
                        'status': 403,
                        'message': 'Access denied. Provide Api Key.'
                    })
        else:
            return Response({
                    'status': 403,
                    'message': 'Provide application ID and Api Key.'
                })

    def patch(self, request):
        if request.data['id']:
            if request.data['api_key']:
                app = Application.objects.get(id=request.data['id'])
                if app.api_key == request.data['api_key'] and request.data['data']:
                    app.data.clear()
                    for i in request.data['data'].split(','):
                        app.data.add(AppData.objects.get(id=i))
                    return Response({'status': '200'})
                else:
                    return Response({
                        'status': 403,
                        'message': 'Wrong Api Key'
                    })
            else:
                return Response({
                        'status': 403,
                        'message': 'Access denied. Provide Api Key.'
                    })
        else:
            return Response({
                    'status': 403,
                    'message': 'Provide application ID and Api Key.'
                })


class KeyView(APIView):
    permission_classes = [permissions.AllowAny]

    def patch(self, request):
        if request.data['id']:
            if request.data['api_key']:
                app = Application.objects.get(id=request.data['id'])
                if app.api_key == request.data['api_key']:
                    app.create_new_api_key()
                    app.save()
                    return Response(AppSerializer(app).data)
                else:
                    return Response({
                        'status': 403,
                        'message': 'Wrong Api Key'
                    })
            else:
                return Response({
                        'status': 403,
                        'message': 'Access denied. Provide Api Key.'
                    })
        else:
            return Response({
                    'status': 403,
                    'message': 'Provide application ID and Api Key.'
                })