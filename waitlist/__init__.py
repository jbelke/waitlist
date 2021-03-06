from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.include('pyramid_jinja2')
    # config.add_jinja2_search_path("wondrous:templates")

    # add paths
    config.add_route('home', '/waitlist')


    config.scan()
    return config.make_wsgi_app()
