from typing import Any, Callable, Type, Optional, List

from Services.Generator.CRUDGenerator import CRUDGenerator
from Services.Generator.Types import Dependencies, PeeweeSchema as Schema


class PeeweeCRUDRouter(CRUDGenerator[Schema]):
    def __init__(
            self,
            schema: Type[Schema],
            prefix: Optional[str] = None,
            tags: Optional[List[str]] = None,
            paginate: Optional[int] = None,
            find_one_route: bool | Dependencies = True,
            **kwargs: Any,
    ):
        super().__init__(
            schema=schema,
            prefix=prefix,
            tags=tags,
            paginate=paginate,
            find_one_route=find_one_route,
            **kwargs,
        )

    def FindOne(self, *args: Any, **kwargs: Any) -> Callable[..., Any]:
        def useRoute():
            return Schema.select('*')

        return useRoute
