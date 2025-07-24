from rest_framework import generics
from .models import Burger
from .serializers import BurgerSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class BurgerListCreateView(generics.ListCreateAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

class BurgerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Burger.objects.all()
    serializer_class = BurgerSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
