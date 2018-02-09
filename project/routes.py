from apistar import Route, Include
from apistar.handlers import docs_urls, static_urls

from project import views

routes = [
    Route('/ping_database', 'GET', views.ping_database, name='ping'),

    Route('/get_university_by_id/{_id}', 'GET', views.get_university_by_id),

    Route('/list_all_uni_as_geo_json', 'GET', views.list_all_uni_as_geo_json,
          name='list_all_uni_as_geo_json'),

    Route('/search_by_all/{text}', 'GET', views.search_by_all),

    Route('/uni_in_country/{country}', 'GET', views.uni_in_country),

    Route('/fagomraade', 'GET', views.get_fagomraader, name='get_fagomraader'),

    Include('/', docs_urls),
    Include('/static', static_urls)
]
