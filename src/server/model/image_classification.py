from pydantic import BaseModel


class TagsDTO(BaseModel):
    tags: list[str]


class TagsResponse(BaseModel):
    success: bool = True
    data: TagsDTO
