from pydantic import BaseModel, Field


class AuthLoginRequest(BaseModel):

    email: str = Field(
        min_length=5,
        max_length=255,
    )

    password: str = Field(
        min_length=1,
        max_length=128,
    )