from rest_framework.viewsets import GenericViewSet
from .models import Discount, Store
from .serializers import DiscountSerializers
from rest_framework.permissions import DjangoModelPermissions, AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class DiscountViewSet(GenericViewSet):

    @swagger_auto_schema(method='post', request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'storeID': openapi.Schema(type=openapi.TYPE_STRING, description='the id of Store in string'),
            'number': openapi.Schema(type=openapi.TYPE_STRING, description='the number of discounts to create'),
            'end_date': openapi.Schema(type=openapi.TYPE_STRING, description='date discount ends'),
        }
    ))
    @action(methods=["post"], detail=False, permission_classes=[AllowAny])
    def create_discount(self, request):
        store_id = request.data['storeID']
        number = request.data['number']
        end_date = request.data['end_date']
        try:
            store = Store.objects.get(id=store_id)
        except Store.DoesNotExist:
            return Response(
                {
                    'status': False,
                    'result': 'could not find Store'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        for i in range(0, number):
            try:
                discount = Discount()
                discount.end_date = end_date
                discount.store = store
                discount.save()
            except Exception:
                continue
        discounts = Discount.objects.filter(store=store, status='active')
        discount_serializer = DiscountSerializers(data=discounts, many=True)
        discount_serializer.is_valid()
        return Response({
            'status': True,
            'result': discount_serializer.data
        }, status=status.HTTP_200_OK)


    storeID = openapi.Parameter('StoreID', openapi.IN_QUERY, description="the ID of the store", type=openapi.TYPE_STRING)
    @swagger_auto_schema(method='get', manual_parameters=[storeID])
    @action(methods=["get"], detail=False, permission_classes=[AllowAny])
    def get_discount(self, request):
        store_id = request.query_params.get('StoreID')
        try:
            store = Store.objects.get(id=store_id)
        except Store.DoesNotExist:
            return Response(
                {
                    'status': False,
                    'result': 'could not find Store'
                }, status=status.HTTP_400_BAD_REQUEST
            )
        discount = Discount.objects.filter(store=store, status='active')
        discount_serializer = DiscountSerializers(data=discount, many=True)
        discount_serializer.is_valid()
        return Response({
            'status': True,
            'result': discount_serializer.data[0]
        }, status=status.HTTP_200_OK)



