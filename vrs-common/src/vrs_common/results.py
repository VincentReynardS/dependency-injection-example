from dataclasses import dataclass
from typing import Generic, Optional, TypeVar

T = TypeVar('T')


@dataclass
class ProviderResult(Generic[T]):
    data: Optional[T]
    error: Optional[Exception]
    error_message: Optional[str]

    @classmethod
    def successful(cls, data: Optional[T]):
        return cls(data=data, error=None, error_message=None)

    @classmethod
    def failed(
        cls, error: Optional[Exception] = None, error_message: Optional[str] = None
    ):
        return cls(data=None, error=error, error_message=error_message)

    def is_successful(self):
        return self.error is None and self.error_message is None


@dataclass
class Result(Generic[T]):
    data: Optional[T]
    error: Optional[Exception]
    error_message: Optional[str]

    @classmethod
    def successful(cls, data: Optional[T]):
        return cls(data=data, error=None, error_message=None)

    @classmethod
    def failed(
        cls, error: Optional[Exception] = None, error_message: Optional[str] = None
    ):
        return cls(data=None, error=error, error_message=error_message)

    def is_successful(self):
        return self.error is None and self.error_message is None

    @classmethod
    def from_provider_result(cls, provider_result: ProviderResult):
        return Result(
            data=provider_result.data,
            error=provider_result.error,
            error_message=provider_result.error_message,
        )
