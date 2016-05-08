from scraper.models import Scraper
from scraper.serializers import ScraperSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from crystal_knows_scraper import CrystalKnows

class ScraperCrystalKnows(APIView):
    """
    List all data about people searched, or search for info on new Person.
    """
    def get(self, request, format=None):
        scraper = Scraper.objects.all()
        serializer = ScraperSerializer(scraper, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        ##############Scrape post data########################
        interesting_person = CrystalKnows(request.data)
        new_data = interesting_person.scraper_crystal_knows()
        ######################################################
        serializer = ScraperSerializer(data=new_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
