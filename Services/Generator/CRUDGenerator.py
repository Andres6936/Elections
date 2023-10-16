from abc import ABC, abstractmethod
from typing import Generic, Type, Any, Optional, List, Callable

from fastapi import APIRouter

from Services.Generator.Types import T, Dependencies


class CRUDGenerator(Generic[T], APIRouter, ABC):
    __BASE_PATH: str = "/"

    def __init__(
            self,
            schema: Type[T],
            prefix: Optional[str] = None,
            tags: Optional[List[str]] = None,
            findOneRoute: bool | Dependencies = True,
            **kwargs: Any):
        """
        :param prefix: to set the path prefix for a router. Up to now, this was only possible when calling include_router.
        :param tags: OpenAPI tags to apply to all the path operations in this router.
        """
        self.schema: Type[T] = schema

        prefix = str(prefix if prefix else self.schema.__name__).lower()
        prefix = self.__BASE_PATH + prefix.strip("/")
        tags = tags or [prefix.strip("/").capitalize()]

        super().__init__(prefix=prefix, tags=tags, **kwargs)

        if findOneRoute:
            self.add_api_route(
                "",
                self.FindOne(),
                methods=["GET"],
                response_model=Optional[List[self.schema]],
                summary="Find One",
                dependencies=findOneRoute,
            )

    @abstractmethod
    def FindOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError
