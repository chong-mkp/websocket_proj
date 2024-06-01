import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from graphql_ws.django import GraphQLWSConsumer
import websocket_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

# Get the Django ASGI application
django_asgi_app = get_asgi_application()

# Define WebSocket URL patterns and routing configuration
websocket_urlpatterns = websocket_app.routing.websocket_urlpatterns

# Configure ASGI application with WebSocket routing
application = ProtocolTypeRouter({
    'http': django_asgi_app,  # Use Django ASGI application for HTTP
    'websocket': AuthMiddlewareStack(  # Apply authentication middleware for WebSocket
        URLRouter(
            websocket_urlpatterns  # Use WebSocket URL patterns for routing
        )
    ),
    'graphql': GraphQLWSConsumer(django_asgi_app), 
})
