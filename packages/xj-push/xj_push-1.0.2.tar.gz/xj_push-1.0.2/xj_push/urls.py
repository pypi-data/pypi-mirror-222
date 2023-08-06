# 应用名称
from django.urls import re_path

app_name = 'push'
from .service_register import register
from .apis.push_apis import PushApis

register()
urlpatterns = [

    re_path(r'^wechat/?$', PushApis.template_send, name="模板推送"),

]
