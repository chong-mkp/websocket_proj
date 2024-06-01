from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from websocket_app.consumers import PostConsumer

# Define WebSocket URL patterns
websocket_urlpatterns = [
    ('ws/posts/', PostConsumer),
    # Add more WebSocket URL patterns here as needed
]

# Configure routing with URLRouter
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            websocket_urlpatterns
        )
    ),
})
