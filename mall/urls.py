"""mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, re_path
from django.views.static import serve
from .settings import MEDIA_ROOT
import xadmin
from goods.view_base import GoodsListViewSet, CategoryViewset,BannerViewset
from users.views import UserViewset,SmsCodeViewset
from user_operation.views import UserFavViewset,LeavingMessageViewset,AddressViewset
from trade.views import ShoppingCartViewset,OrderViewset

from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

router = DefaultRouter()

# 配置goods的url,这个basename是干啥的
router.register(r'goods', GoodsListViewSet, base_name="goods")

# 配置Category的url
router.register(r'categories', CategoryViewset, base_name="categories")

# 配置users的url
router.register(r'users', UserViewset, base_name="users")

# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, base_name="userfavs")

# 配置用户留言的url
router.register(r'messages', LeavingMessageViewset, base_name="messages")

# 收货地址
router.register(r'address', AddressViewset, base_name="address")

# 购物车
router.register(r'shopcarts', ShoppingCartViewset, base_name="shopcarts")

# 订单相关url
router.register(r'orders', OrderViewset, base_name="orders")

# 首页banner轮播图url
router.register(r'banners', BannerViewset, base_name="banners")

# 配置codes的url
router.register(r'codes', SmsCodeViewset, base_name="codes")

urlpatterns = [

    # path('xadmin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),

    # 富文本相关url
    path('ueditor/', include('DjangoUeditor.urls')),

    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),

    # router的path路径
    re_path('^', include(router.urls)),

    path('docs/', include_docs_urls(title='olex生鲜超市文档')),

    path('api-auth/', include('rest_framework.urls')),

    # drf自带的token授权登录,获取token需要向该地址post数据
    # path('api-token-auth/', views.obtain_auth_token),

    path('api-token-auth/', obtain_jwt_token),

    path('login/', obtain_jwt_token),

    path('jwt-auth/', obtain_jwt_token),

]
# urlpatterns += [
#     path('api-token-auth/', views.obtain_auth_token)
# ]
