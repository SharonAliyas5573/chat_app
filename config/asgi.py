import os
import sys
from pathlib import Path
 
from django.core.asgi import get_asgi_application
# This allows easy placement of apps within the interior

 
ROOT_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.append(str(ROOT_DIR / "chat_app"))
 
# If DJANGO_SETTINGS_MODULE is unset, default to the local settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
 
# This application object is used by any ASGI server configured to use this file.
django_application = get_asgi_application()
 
# Import websocket application here, so apps from django_application are loaded first
from config import routing  # noqa isort:skip
 
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa isort:skip
from chat_app.chats.middleware import TokenAuthMiddleware
 
application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": TokenAuthMiddleware(URLRouter(routing.websocket_urlpatterns)),
    }
)