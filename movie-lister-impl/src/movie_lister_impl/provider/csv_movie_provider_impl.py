import csv
from typing import List

from dependency_injector.wiring import Provide, inject
from movie_lister_api.provider.movie_provider import MovieProvider
from movie_lister_api.service.model.movie import Movie

from ..config import ConfigContainer
from ..config.csv_movie_config import CSVMovieConfig


class CSVMovieProviderImpl(MovieProvider):
    @inject
    def __init__(
        self,
        csv_movie_config: CSVMovieConfig = Provide[ConfigContainer.csv_movie_config],
    ):
        self.csv_movie_config = csv_movie_config

    def get_movies_by_director(self, director: str) -> List[Movie]:
        all_movies = self._find_all()

        return [movie for movie in all_movies if movie.director == director]

    def _find_all(self) -> List[Movie]:
        with open(self.csv_movie_config.csv_file_path) as csv_file:
            csv_reader = csv.reader(
                csv_file, delimiter=self.csv_movie_config.csv_delimiter
            )
            next(csv_reader)  # skip the header
            return [
                Movie(title=row[0], year=int(row[1]), director=row[2])
                for row in csv_reader
            ]
