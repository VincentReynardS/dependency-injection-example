build-movie-lister-cli-app:
	uv remove movie-lister-impl && \
	uv remove movie-lister-api && \
	uv remove vrs-common && \
	uv add ../vrs-common/dist/vrs_common-0.1.0-py3-none-any.whl && \
	uv add ../movie-lister-api/dist/movie_lister_api-0.1.0-py3-none-any.whl && \
	uv add ../movie-lister-impl/dist/movie_lister_impl-0.1.0-py3-none-any.whl && \
	uv build