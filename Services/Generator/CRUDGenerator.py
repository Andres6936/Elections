from abc import ABC, abstractmethod
from typing import Generic, Type, Any, Optional, List, Callable

from fastapi import APIRouter, HTTPException

from Services.Generator.Types import T, Dependencies


class CRUDGenerator(Generic[T], APIRouter, ABC):
    __BASE_PATH: str = "/"

    def __init__(
            self,
            schema: Type[T],
            prefix: Optional[str] = None,
            tags: Optional[List[str]] = None,
            find_one_route: bool | Dependencies = True,
            find_many_route: bool | Dependencies = True,
            insert_one_route: bool | Dependencies = True,
            insert_many_route: bool | Dependencies = True,
            update_one_route: bool | Dependencies = True,
            update_many_route: bool | Dependencies = True,
            delete_one_route: bool | Dependencies = True,
            delete_many_route: bool | Dependencies = True,
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

        if find_one_route:
            self.AddRouter(
                "/{serial}",
                self.FindOne(),
                methods=["GET"],
                response_model=None,
                summary="Find One",
                dependencies=find_one_route,
            )

        if find_many_route:
            self.AddRouter(
                "",
                self.FindMany(),
                methods=["GET"],
                response_model=None,
                summary="Find Many",
                dependencies=find_many_route,
            )

        if insert_one_route:
            self.AddRouter(
                "",
                self.InsertOne(),
                methods=["POST"],
                response_model=None,
                summary="Insert One",
                dependencies=insert_one_route,
            )

        if insert_many_route:
            self.AddRouter(
                "/batch",
                self.InsertMany(),
                methods=["POST"],
                response_model=None,
                summary="Insert Many",
                dependencies=insert_many_route,
            )

        if update_one_route:
            self.AddRouter(
                "/{serial}",
                self.UpdateOne(),
                methods=["PUT"],
                response_model=None,
                summary="Update One",
                dependencies=update_one_route,
            )

        if update_many_route:
            self.AddRouter(
                "/batch",
                self.UpdateMany(),
                methods=["PUT"],
                response_model=None,
                summary="Update Many",
                dependencies=update_many_route,
            )

        if delete_one_route:
            self.AddRouter(
                "/{serial}",
                self.DeleteOne(),
                methods=["DELETE"],
                response_model=None,
                summary="Delete One",
                dependencies=delete_one_route,
            )

        if delete_many_route:
            self.AddRouter(
                "/batch",
                self.DeleteMany(),
                methods=["DELETE"],
                response_model=None,
                summary="Delete Many",
                dependencies=delete_many_route,
            )

    def AddRouter(
            self,
            path: str,
            endpoint: Callable[..., Any],
            dependencies: bool | Dependencies,
            error_responses: Optional[List[HTTPException]] = None,
            **kwargs: Any,
    ) -> None:
        dependencies = [] if isinstance(dependencies, bool) else dependencies
        responses: Any = (
            {err.status_code: {"detail": err.detail} for err in error_responses} if error_responses else None
        )
        super().add_api_route(path, endpoint, dependencies=dependencies, responses=responses, **kwargs)

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

    @abstractmethod
    def FindMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError

    @abstractmethod
    def InsertOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError

    @abstractmethod
    def InsertMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError

    @abstractmethod
    def UpdateOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError

    @abstractmethod
    def UpdateMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError

    @abstractmethod
    def DeleteOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError

    @abstractmethod
    def DeleteMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        """
        The Callable type hint indicates that the value is an object that can be called like a function.
        The ... syntax indicates that the number and types of arguments that the object can take are not specified.
        The Any type hint indicates that the object can return any value.

        In other words, the Callable[..., Any] type hint indicates that the value is an object that can be called
        like a function, and it can take any number and types of arguments, and it can return any value.
        """
        raise NotImplementedError
