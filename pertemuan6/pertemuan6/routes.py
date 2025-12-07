def includeme(config):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    
    # API Routes
    config.add_route('api_models', '/api/models')
    config.add_route('api_model_detail', '/api/models/{id}')

