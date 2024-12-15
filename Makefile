build-vrs-common:
	uv build vrs-common/

build-movie-lister-api:
	cd movie-lister-api; \
	uv remove vrs-common && \
	uv add ../vrs-common/dist/vrs_common-0.1.0-py3-none-any.whl && \
	uv build

build-movie-lister-impl:
	cd movie-lister-impl; \
	uv remove movie-lister-api && \
	uv remove vrs-common && \
	uv add ../vrs-common/dist/vrs_common-0.1.0-py3-none-any.whl && \
	uv add ../movie-lister-api/dist/movie_lister_api-0.1.0-py3-none-any.whl && \
	uv build

build-local-libraries: build-vrs-common build-movie-lister-api build-movie-lister-impl
