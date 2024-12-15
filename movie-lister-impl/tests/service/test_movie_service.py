from unittest.mock import Mock

import pytest
from movie_lister_api.provider import MovieProvider
from movie_lister_api.service.model import Movie
from movie_lister_impl.service import MovieServiceImpl
from vrs_common.results import ProviderResult


class TestMovieServiceImpl:
    @pytest.fixture
    def mock_movie_provider(self) -> MovieProvider:
        return Mock()

    @pytest.fixture
    def movie_service_impl(self, mock_movie_provider) -> MovieServiceImpl:
        return MovieServiceImpl(movie_provider=mock_movie_provider)

    def test_get_movies_by_director__should_return_success(
        self, movie_service_impl: MovieServiceImpl, mock_movie_provider: MovieProvider
    ):
        mock_movie_provider.get_movies_by_director.return_value = (
            ProviderResult.successful(
                data=[Movie(title='Python', year=2024, director='Vincent')]
            )
        )

        result = movie_service_impl.get_movies_by_director(director='Vincent')

        assert result.is_successful()
        assert result.data == [Movie(title='Python', year=2024, director='Vincent')]

    def test_get_movies_by_director__provider_returns_empty__should_return_success(
        self, movie_service_impl: MovieServiceImpl, mock_movie_provider: MovieProvider
    ):
        mock_movie_provider.get_movies_by_director.return_value = (
            ProviderResult.successful(data=[])
        )

        result = movie_service_impl.get_movies_by_director(director='Vincent')
        mock_movie_provider.get_movies_by_director.assert_called_with(
            director='Vincent'
        )

        assert result.is_successful()
        assert result.data == []

    def test_get_movies_by_director__provider_returns_failed__should_return_failed(
        self, movie_service_impl: MovieServiceImpl, mock_movie_provider: MovieProvider
    ):
        error_message = 'Test exception'
        exception = Exception(error_message)

        mock_movie_provider.get_movies_by_director.return_value = ProviderResult.failed(
            error=exception, error_message=error_message
        )

        result = movie_service_impl.get_movies_by_director(director='Vincent')
        mock_movie_provider.get_movies_by_director.assert_called_with(
            director='Vincent'
        )

        assert not result.is_successful()
        assert result.error == exception
        assert result.error_message == error_message
