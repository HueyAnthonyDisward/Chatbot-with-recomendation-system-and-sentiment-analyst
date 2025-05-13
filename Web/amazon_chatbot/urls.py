from django.urls import path
from . import views

urlpatterns = [
    path('', views.chatbot_view, name='chatbot_view'),  # Trang gốc: hiển thị giao diện chatbot
    path('chat/', views.chat_handler, name='chat_handler'),  # Endpoint cho AJAX request
    path('new_chat/', views.new_chat, name='new_chat'),
    path('pomato/', views.home_view, name='home_view'), 
    path('cart/', views.cart_view, name='cart_view'),
    path('brand/', views.brand_view, name='brand_view'),
    path('product/', views.product_view, name='product_view'), # Endpoint cho tạo chat mới
    path('special/', views.special_view, name='special_view'), # Endpoint cho tạo chat mới
    path('contact/', views.contact_view, name='contact_view'), # Endpoint cho tạo chat mới
]