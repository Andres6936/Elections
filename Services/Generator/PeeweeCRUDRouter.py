from typing import Any, Callable, Type, Optional, List

from playhouse.shortcuts import model_to_dict

from Services.Generator.CRUDGenerator import CRUDGenerator
from Services.Generator.Types import Dependencies, PeeweeSchema as Schema


class PeeweeCRUDRouter(CRUDGenerator[Schema]):
    def __init__(
            self,
            schema: Type[Schema],
            prefix: Optional[str] = None,
            tags: Optional[List[str]] = None,
            find_one_route: bool | Dependencies = True,
            **kwargs: Any,
    ):
        self.schema = schema
        super().__init__(
            schema=schema,
            prefix=prefix,
            tags=tags,
            find_one_route=find_one_route,
            **kwargs,
        )

    def FindOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial)
            return model_to_dict(response)

        return route

    def FindMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route():
            response = self.schema.select().limit(5)
            items = []
            for item in response.dicts():
                items.append(item)
                print(item)
            return items

        return route

    def InsertOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial).__data__
            return response

        return route

    def InsertMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial).__data__
            return response

        return route

    def UpdateOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial).__data__
            return response

        return route

    def UpdateMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial).__data__
            return response

        return route

    def DeleteOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial).__data__
            return response

        return route

    def DeleteMany(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def route(serial: str):
            response = self.schema.get(serial).__data__
            return response

        return route
