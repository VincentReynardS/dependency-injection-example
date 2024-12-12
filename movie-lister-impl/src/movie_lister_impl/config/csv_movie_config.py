from pydantic_settings import BaseSettings, SettingsConfigDict


class CSVMovieConfig(BaseSettings):
    """
    A configuration class containing details about movies' csv file
    """

    model_config = SettingsConfigDict(
        env_file='settings.env', env_prefix='csv_', env_file_encoding='utf-8'
    )
    csv_file_path: str
    csv_delimiter: str
