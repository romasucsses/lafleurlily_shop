from rest_framework.views import APIView
from rest_framework.response import Response
from cache_control.cache_logic import *
from .pagination import ReviewsPagination
from rest_framework.permissions import AllowAny
from utils.get_table import get_model_by, get_serializer


class ShopViewAPI(APIView):
    permission_classes = [AllowAny]

    def get_category(self):
        return None

    def get(self, request, db: str):
        category = self.get_category()
        order_by = request.query_params.get("order_by", "name")
        model = get_model_by(db, 'Product', 'products')
        queryset = model.objects.all().order_by(order_by)
        cache_name = f"{PRODUCTS_LIST_CACHE_NAME}_{db}_orderby_{order_by}"
        serializer = get_serializer(db, 'Product')

        if category:
            queryset = queryset.filter(category=category)
            cache_name = cache_name + f"_category_{category}"

        result = get_or_set_cache(
            queryset=queryset,
            serializer=serializer,
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
        model = get_model_by(db, "Product", 'products')
        serializer = get_serializer(db, 'Product')
        result = get_or_set_cache(
            queryset=model.objects.get(slug_url=uniq_url_slug),
            serializer=serializer,
            cache_name=f"{PRODUCT_DETAIL_CACHE_NAME}_{db}_{uniq_url_slug}",
            type_data='detail',
            cache_duration=CACHE_DURATIONS_24h
        )
        return Response(result)


class ReviewsAPI(APIView, ReviewsPagination):
    permission_classes = [AllowAny]

    def getProduct(self, product_id, model):
        try: 
            return model.objects.get(pk=product_id)
        except Exception as e:
            return e

    def get(self, request, product_id, db):
        model = get_model_by(db, "Reviews", "products")
        product = self.getProduct(product_id, model)
        reviews = self.paginate_queryset(model.objects.filter(product=product), request)
        serializer = get_serializer(db, 'Reviews')
        if reviews is None:
            return Response("Have not one yet")
        else:
            result = get_or_set_cache(
                queryset=reviews,
                serializer=serializer,
                cache_name=f"{REVIEWS_LIST_CACHE_NAME}_{db}_{product_id}",
                type_data='list',
                cache_duration=CACHE_DURATIONS_24h
            )
            return self.get_paginated_response(result)

    def post(self, request, product_id, db):
        serializer = get_serializer(db, 'Reviews')
        new_review = serializer(data=request.data)
        if new_review.is_valid():
            product = self.getProduct(product_id, db)
            new_review.save(product=product)

            return Response('New Review Added Successful')
        return Response('Not Added!')


class ListStoresAPIView(APIView):
    permission_classes = [AllowAny]


    def get(self, request, db: str):
        model = get_model_by(db, 'Stores', 'products')
        queryset = model.objects.all()
        cache_name = f"{SHIPPING_ADDRESS_DETAIL_CACHE_NAME}_{db}"
        serializer = get_serializer(db, 'Stores')

        result = get_or_set_cache(
            queryset=queryset,
            serializer=serializer,
            cache_name=cache_name,
            type_data='list',
            cache_duration=CACHE_DURATIONS_24h
        )

        return Response(result)