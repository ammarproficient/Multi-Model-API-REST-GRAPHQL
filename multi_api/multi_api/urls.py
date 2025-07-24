from django.contrib import admin
from django.urls import path, include
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('model_api.urls')),  # REST API
    path('token/', obtain_auth_token),  # login to get token
    path('graph/', csrf_exempt(GraphQLView.as_view(graphiql=True))),  # GraphQL
]
