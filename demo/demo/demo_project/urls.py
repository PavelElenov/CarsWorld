from django.urls import path

from demo.demo_project.views import show_home_page, show_profile, register_user, \
    login_user, log_out, add_img, show_cars, add_car_to_cart, show_accessories, add_accessory_to_cart, show_cart, \
    delete_item_from_cart, buy_products_in_cart

urlpatterns = [
    path('', show_home_page, name='home'),
    path('profile/', show_profile, name="profile"),
    path("profile/login/", login_user, name="login"),
    path("profile/register/", register_user, name="register"),
    path("profile/delete/", log_out, name="log_out"),
    path("profile/add_img/", add_img, name="add_img"),
    path("cars/", show_cars, name="cars"),
    path("cars/add_to_card/", add_car_to_cart, name="add_car"),
    path("accessories/", show_accessories, name="accessories"),
    path("accessories/add_accessory/", add_accessory_to_cart, name="add accessory"),
    path("cart/", show_cart, name="cart"),
    path("cart/delete_item/<int:id>/<type>/", delete_item_from_cart, name="delete item"),
    path("cart/but_products", buy_products_in_cart, name="buy"),
]