from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import status
from rest_framework.views import APIView
import json
from awards_app.models import User, Award

class UserView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        user_id = request.data.get("user_id")
        name = request.data.get("name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        location = request.data.get("location")
        picture = request.data.get("picture")
        awards = request.data.get("awards")

        try:
            user = User(user_id=user_id, name=name, email=email, phone=phone, location=location, picture=picture, awards=awards)
            user.save()
            return JsonResponse({"success": "Data saved successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be saved"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, user_id=None):
        if user_id:
            try:
                user = User.objects.filter(user_id=user_id).values('user_id','name', 'email', 'phone', 'location', 'picture', 'awards')
                return JsonResponse(list(pizza_specification), safe=False)
            except:
                return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                pizza_specification = PizzaSpecification.objects.all().values('pizza_size','pizza_toppings')
                return JsonResponse(list(pizza_specification), safe=False)
            except:
                return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user_id):
        user_id = request.data.get("user_id")
        name = request.data.get("name")
        email = request.data.get("email")
        phone = request.data.get("phone")
        location = request.data.get("location")
        picture = request.data.get("picture")
        awards = request.data.get("awards")
        try:
            user = User.objects.filter(user_id=user_id).update(user_id=user_id, name=name, email=email, phone=phone, location=location, picture=picture, awards=awards)
            return JsonResponse({"success": "Data updated successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be updated"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id=None):
        try:
            if user_id:
                user = User.objects.filter(user_id=user_id).delete()
            else:
                User.objects.all().delete()
            return JsonResponse({"success": "Data deleted successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be deleted"}, status=status.HTTP_400_BAD_REQUEST)

class AwardView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        award_id = request.data.get("award_id")
        title = request.data.get("title")
        points = request.data.get("points")

        try:
            award = Award(award_id=award_id, title=title, points=points)
            award.save()
            return JsonResponse({"success": "Data saved successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be saved"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, award_id=None):
        if award_id:
            try:
                award = Award.objects.filter(award_id=award_id).values('award_id','title', 'points')
                return JsonResponse(list(award), safe=False)
            except:
                return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                award = Award.objects.all().values('award_id','title', 'points')
                return JsonResponse(list(award), safe=False)
            except:
                return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, award_id):
        award_id = request.data.get("award_id")
        title = request.data.get("title")
        points = request.data.get("points")

        try:
            award = Award.objects.filter(award_id=award_id).update(award_id=award_id, title=title, points=points)
            return JsonResponse({"success": "Data updated successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be updated"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id=None):
        try:
            if award_id:
                award = Award.objects.filter(award_id=award_id).delete()
            else:
                Award.objects.all().delete()
            return JsonResponse({"success": "Data deleted successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be deleted"}, status=status.HTTP_400_BAD_REQUEST)
