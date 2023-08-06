import asyncio
from jupyter_server.utils import url_path_join

from .paraview import ParaViewHandler
from .trame import TrameHandler
from .user import UserHandler


def setup_handlers(web_app):
    base_url = url_path_join(web_app.settings["base_url"], "jupyter-viz-extension")
    web_app.add_handlers(".*$", [
        (url_path_join(base_url, "paraview"), ParaViewHandler),
        (url_path_join(base_url, "trame"), TrameHandler),
        (url_path_join(base_url, "user"), UserHandler)
    ])
