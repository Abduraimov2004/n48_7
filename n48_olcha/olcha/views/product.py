from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated

from olcha.models import Product, Image
from olcha.serializers import ProductSerializer, ImageSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication


class ProductListApiView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ImageListApiView(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
