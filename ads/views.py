import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from ads.models import Ad, Category
from avito import settings
from users.models import User


def index(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name='dispatch')
class CategoriesListView(ListView):
    model = Category

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


@method_decorator(csrf_exempt, name='dispatch')
class CategoryCreateView(CreateView):
    model = Category
    fields = ["name"]

    def post(self, request, *args, **kwargs):
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


@method_decorator(csrf_exempt, name='dispatch')
class AdsListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.select_related("author").order_by("-price")

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get("page", 1)
        page_obj = paginator.get_page(page_number)

        ads = [
            {
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author.id,
                "author": ad.author.username,
                "price": ad.price,
                "description": ad.description,
                "is_published": ad.is_published,
                "category": ad.category.name,
                "image": ad.image.url if ad.image else None
            } for ad in page_obj]

        response = [{
            "items": ads,
            "num_pages": paginator.num_pages,
            "total": paginator.count,
        }]

        return JsonResponse(response, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class AdSingleView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author.id,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": ad.category.name,
            "image": ad.image.url if ad.image else None
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ["id",
              "name",
              "author_id",
              "author",
              "price",
              "description",
              "is_published",
              "category",
              "image"]

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        author = get_object_or_404(User, username=ad_data['author'])
        category = get_object_or_404(Category, name=ad_data['category'])

        ad = Ad.objects.create(
            name=ad_data["name"],
            author=author,
            price=ad_data["price"],
            description=ad_data["description"],
            is_published=ad_data["is_published"],
            category=category,
        )

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author.id,
            "author": ad.author.username,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "category": ad.category.name,
            "image": ad.image.url if ad.image else None

        })


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ["name",
              "price",
              "description",
              "is_published",
              "category"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)
        category = get_object_or_404(Category, name=ad_data['category'])

        self.object.name = ad_data["name"]
        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.is_published = ad_data["is_published"]
        self.object.category = category

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


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = "ad/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)
