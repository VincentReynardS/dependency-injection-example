from dependency_injector.wiring import Provide, inject
from movie_lister_api.service.movie_service import MovieService
from movie_lister_impl.service import ServiceContainer


@inject
def main(movie_service: MovieService = Provide[ServiceContainer.movie_service]):
    movies = movie_service.get_movies_by_director(director='Vincent')
    print([movie.model_dump() for movie in movies])


if __name__ == '__main__':
    service_container = ServiceContainer()
    service_container.init_resources()
    service_container.wire(modules=[__name__])

    main()
