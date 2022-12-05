import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from ads.models import Category


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesListView(ListView):
    model = Category

    @extend_schema(
        description="Retrieve category list",
        summary="Category list"
    )
    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by("name")

        response = [{
            "id": cat.id,
            "name": cat.name,
        } for cat in self.object_list]

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class CategorySingleView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


@extend_schema(
    description="Create category",
    summary="Create category",
    request={
        "application/json": {
            "name": "name",
            "slug": "slug"
        },
    },
    responses={
        "application/json": {
            "name": "name",
            "slug": "slug"
        }
    }
)
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def category_create_view(request):
    cat_data = json.loads(request.body)

    cat = Category.objects.create(
        name=cat_data["name"],
    )

    return JsonResponse({
        "id": cat.id,
        "name": cat.name,
    })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryUpdateView(UpdateView):
    model = Category
    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)
        self.object.name = cat_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class CategoryDeleteView(DeleteView):
    model = Category
    success_url = "cat/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
