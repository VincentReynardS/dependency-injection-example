from pydantic_settings import BaseSettings, SettingsConfigDict


class CSVMovieConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='settings.env', env_prefix='csv_', env_file_encoding='utf-8'
    )
    csv_file_path: str
    csv_delimiter: str
