from rest_framework.views import APIView
from .serializers import ProductSerializer, ReviewSerializer
from .models import Product, Reviews
from rest_framework.response import Response
from cache_control.cache_logic import *
from .pagination import ReviewsPagination
from rest_framework.permissions import AllowAny



class ShopViewAPI(APIView):
    permission_classes = [AllowAny]

    def get_category(self):
        return None

    def get(self, request, db: str):
        category = self.get_category()
        order_by = request.query_params.get("order_by", "name")
        queryset = Product.objects.using(db).all().prefetch_related('category').order_by(order_by)
        cache_name = f"{PRODUCTS_LIST_CACHE_NAME}_{db}_orderby_{order_by}"

        if category:
            queryset = queryset.filter(category=category)
            cache_name = cache_name + f"_category_{category}"

        result = get_or_set_cache(
            queryset=queryset,
            serializer=ProductSerializer,
            cache_name=cache_name,
            type_data='list',
            cache_duration=CACHE_DURATIONS_24h
        )

        return Response(result)


class WineViewAPI(ShopViewAPI):
    def get_category(self):
        return 1


class SparklingViewAPI(ShopViewAPI):
    def get_category(self):
        return 2


class DetailProductViewAPI(APIView):
    permission_classes = [AllowAny]

    def get(self, request, uniq_url_slug, db: str):

        result = get_or_set_cache(
            queryset=Product.objects.using(db).get(slug_url=uniq_url_slug).prefetch_related('category'),
            serializer=ProductSerializer,
            cache_name=f"{PRODUCT_DETAIL_CACHE_NAME}_{db}_{uniq_url_slug}",
            type_data='detail',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)


class ReviewsAPI(APIView, ReviewsPagination):
    permission_classes = [AllowAny]

    def getProduct(self, product_id, db):
        try: 
            return Product.objects.using(db).get(pk=product_id)
        except Exception as e:
            return e

    def get(self, request, product_id, db):
        product = self.getProduct(product_id, db)
        reviews = self.paginate_queryset(Reviews.objects.using(db).filter(product=product), request)
        if reviews is None:
            return Response("Have not one yet")
        else:
            result = get_or_set_cache(
                queryset=reviews,
                serializer=ReviewSerializer,
                cache_name=f"{REVIEWS_LIST_CACHE_NAME}_{db}_{product_id}",
                type_data='list',
                cache_duration=CACHE_DURATIONS_24h
            )
            return self.get_paginated_response(result)

    def post(self, request, product_id, db):
        new_review = ReviewSerializer(data=request.data)
        if new_review.is_valid():
            product = self.getProduct(product_id, db)
            new_review.save(product=product)

            return Response('New Review Added Successful')
        return Response('Not Added!')
