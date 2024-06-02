import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import websocket_app.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'websocket_proj.settings')

# Configure ASGI application with WebSocket routing
application = ProtocolTypeRouter({
    'http': get_asgi_application(),  # Use Django ASGI application for HTTP
    'websocket': URLRouter(
        websocket_app.routing.websocket_urlpatterns
    )
})
