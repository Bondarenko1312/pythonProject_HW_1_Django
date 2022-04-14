import json

from rest_framework.views import APIView
from rest_framework.response import Response


class Hw1View(APIView):
    def get(self, *args, **kwargs):
        try:
            with open('users.json') as file:
                data = json.load(file)
                return Response(data)
        except Exception as err:
            return Response(err)
