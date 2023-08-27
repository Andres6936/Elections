from pydantic import BaseModel


class Pagination(BaseModel):
    """
    Page numbers are 1-based, so the first page of results will be page 1.
    """
    Page: int
    PageSize: int
