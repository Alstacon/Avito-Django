import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.viewsets import ModelViewSet

from ads.models import Ad, Category
from ads.serializers import AdSerializer, AdDetailSerializer


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


class AdViewSet(ModelViewSet):
    queryset = Ad.objects.all()
    default_serializer = AdSerializer
    serializers = {
        'retrieve': AdDetailSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.default_serializer)

    def list(self, request, *args, **kwargs):
        cat_names = request.GET.getlist("category")
        if cat_names:
            self.queryset = self.queryset.filter(
                category__id__in=cat_names
            )

        ad_name = request.GET.get("name", None)
        if ad_name:
            self.queryset = self.queryset.filter(
                name__icontains=ad_name
            )

        loc_name = request.GET.get("location", None)
        if loc_name:
            self.queryset = self.queryset.filter(
                author__location__name__icontains=loc_name
            )

        price_from = request.GET.get("price_from", None)
        price_to = request.GET.get("price_to", None)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ["image"]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES["image"]
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author_id": self.object.author.id,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category": self.object.category.name,
            "image": self.object.image.url if self.object.image else None
        })
