from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from websocket_app.consumers import PostConsumer
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


websocket_urlpatterns = [
    path('/ws/posts/', PostConsumer),
]

graphql_urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]

application = ProtocolTypeRouter({
    'websocket': URLRouter(websocket_urlpatterns),
})

urlpatterns = graphql_urlpatterns
