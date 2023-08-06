import os
import base64
from werkzeug.wrappers import Request, Response, request
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.middleware.shared_data import SharedDataMiddleware
from werkzeug.debug import DebuggedApplication
from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from ..components.sessions import session_manager
from ..components.blueprint import Blueprint
from werkzeug.urls import url_encode
from itsdangerous import URLSafeTimedSerializer
import json
import mimetypes
from urllib.parse import quote as url_quote, quote_plus as url_quote_plus, urlencode as url_encode
from werkzeug.utils import send_from_directory, safe_join
import importlib

class Zylo:
    def __init__(self, __name__=None):
        self.template_folder = 'views'
        self.url_map = Map()
        self.static_folder = "static"
        self.error_handlers = {}
        self.middlewares = []
        self.template_env = Environment(loader=FileSystemLoader(self.template_folder))
        self.host = None
        self.port = None
        self.debug = None
        self.secret_key = os.urandom(24)
        self.serializer = URLSafeTimedSerializer(base64.urlsafe_b64encode(self.secret_key))
        self.blueprints = []
        self.__name__ = __name__
        self.config = {}

    def get_config(self, key, default=None):
        return self.config.get(key, default)

    def load_settings_from_module(self, module_name):
        try:
            module = importlib.import_module(module_name)
            self.host = module.HOST
            self.port = module.PORT
            self.debug = module.DEBUG
        except ImportError:
            pass

    def load_settings(self):
        self.load_settings_from_module('settings')

    def load_routes(self):
        try:
            urls_module = importlib.import_module('urls')
            urlpatterns = getattr(urls_module, 'urlpatterns', [])
            for route, *args in urlpatterns:
                if callable(args[0]):
                    view_func = args[0]
                    methods = args[1] if len(args) > 1 else None
                else:
                    view_func = args[1]
                    methods = args[2] if len(args) > 2 else None
                self.add_url_rule(route, view_func, methods=methods)
        except ImportError:
            pass

    def validate_backend(self, backend):
        supported_backends = ['zylo.template.backends.DjangoTemplates']
        if backend not in supported_backends:
            raise ValueError(f"Zylo template engine doesn't support this backend: {backend}")

    def setup_template_env(self):
        templates = self.get_config('TEMPLATES')
        if templates:
            backend = templates[0].get('BACKEND')
            dirs = templates[0].get('DIRS', [])
        else:
            backend = None
            dirs = []

        if backend:
            self.validate_backend(backend)
            if backend == 'zylo.template.backends.DjangoTemplates':
                self.template_env = Environment(
                    loader=FileSystemLoader(dirs),
                    autoescape=True  # Enable autoescaping for security
                )
            else:
                # Handle other custom template backends if needed
                pass
        else:
            self.template_env = Environment(
                loader=FileSystemLoader(self.template_folder),
                autoescape=True  # Enable autoescaping for security
            )
            
    def set_template_folder(self):
        dirs = self.config.get('DIRS')
        if dirs:
            dirs = self.template_folder = dirs[0]
            return dirs

    def update_config(self):
        self.load_settings()
        self.setup_template_env()
        self.set_template_folder()
        self.load_routes()

    def add_url_rule(self, route, view_func, methods=None):
        methods = methods or ['GET']
        def wrapped_view_func(request, **values):
            return view_func(request, **values)
        self.url_map.add(Rule(route, endpoint=view_func.__name__, methods=methods))
        setattr(self, view_func.__name__, wrapped_view_func)

    def route(self, rule, methods=['GET']):
        def decorator(handler):
            self.add_url_rule(rule, handler.__name__, handler, methods)
            return handler

        return decorator

    def errorhandler(self, code):
        def decorator(handler):
            self.error_handlers[code] = handler
            return handler

        return decorator

    def use(self, middleware):
        self.middlewares.append(middleware)

    def config(self):
        return self.config

    def url_for_static(self, filename):
        return f'/static/{filename}'

    def serve_static(self, filename):
        static_path = os.path.join(self.static_folder, filename)
        if os.path.isfile(static_path):
            mimetype, _ = mimetypes.guess_type(static_path)
            if mimetype:
                return Response(open(static_path, 'rb').read(), mimetype=mimetype)
        raise NotFound()

    def register_blueprint(self, blueprint):
        self.blueprints.append(blueprint)

    def handle_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            handler = getattr(self, endpoint)
            response = handler(request, **values)
        except NotFound as e:
            response = self.handle_error(404, e, request)
        except HTTPException as e:
            response = e
        return response

    def handle_error(self, code, error, request):
        handler = self.error_handlers.get(code)
        if handler:
            return handler(error, request)
        else:
            return error
        
    def runserver(self, host=None, port=None, debug=None, secret_key=None):
        self.update_config()
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if debug is not None:
            self.debug = debug
        if secret_key is not None:
            self.secret_key = secret_key

        if self.debug:
            app = DebuggedApplication(self, evalex=True)
        else:
            app = self

        from werkzeug.serving import run_simple
        run_simple(self.host, self.port, app, use_reloader=True)

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        for blueprint in self.blueprints:
            if request.path.startswith(blueprint.url_prefix):
                request.blueprint = blueprint
                response = blueprint.wsgi_app(environ, start_response)
                return response

        session_id = request.cookies.get('session_id')
        session_data = session_manager.load_session(session_id)
        request.session = session_data
        response = self.handle_request(request)
        session_id = session_manager.save_session(request.session)

        # Make sure response is a valid Response object before setting the cookie
        if isinstance(response, Response):
            response.set_cookie('session_id', session_id, secure=True, httponly=True)

        return response(environ, start_response)

    def __call__(self, environ, start_response):
        app = self.wsgi_app
        for middleware in reversed(self.middlewares):
            app = middleware(app)
        return app(environ, start_response)

