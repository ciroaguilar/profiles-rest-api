from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """ Testing API View """

    def get(self, request, format=None):
        """Return the list of APIVier features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you most control over you application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello!', 'an_apiview': an_apiview})
