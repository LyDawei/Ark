from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^api/v1/animals/(?P<pk>[0-9]+)$',
        views.get_animal,
        name='get_animal'),
    url(r'^api/v1/animals$',
        views.get_animals,
        name='get_animals'),
    url(r'^api/v1/get_animal_list_in_room/(?P<room>[0-9]+)$',
        views.get_animals_list,
        name='get_animals_list'
        ),
    url(r'^api/v1/checked-out-animals$',
        views.get_checked_out_animals,
        name='get_checked_out_animals'),
    url(r'^api/v1/checked-out-animals/(?P<room>[0-9]+)$',
        views.get_animals_in_room,
        name='get_animals_in_room'),
    url(r'^api/v1/post-check-out-animal$',
        views.post_check_out_animal,
        name='post_check_out_animal'),
    url(r'^api/v1/post-check_in-animal$',
        views.post_check_in_animal,
        name='post_check_in_animal')
]
