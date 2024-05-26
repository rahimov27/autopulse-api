from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["id", "IMEI"]

    def create(self, request, *args, **kwargs):
        data = request.data
        car_id = data.get("id")
        if car_id:
            if Car.objects.filter(id=car_id).exists():
                return Response(
                    {"detail": "A car with this ID already exists."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    @action(detail=False, methods=["get"])
    def search_by_imei(self, request, *args, **kwargs):
        imei = request.query_params.get("imei", None)
        if imei is not None:
            try:
                car = Car.objects.get(IMEI=imei)
                serializer = self.get_serializer(car)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Car.DoesNotExist:
                return Response(
                    {"detail": "Car with this IMEI does not exist."},
                    status=status.HTTP_404_NOT_FOUND,
                )
        return Response(
            {"detail": "IMEI parameter is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )
