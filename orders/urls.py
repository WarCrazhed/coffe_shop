from django.urls import path
from .views import MyOrderView
from .views import CreateOrderProductView

urlpatterns = [
    path("mi-orden", MyOrderView.as_view(), name="my_order"),
    path("agregar-producto", CreateOrderProductView.as_view(), name="add_product"),
]
