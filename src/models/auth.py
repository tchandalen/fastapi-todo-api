from pydantic import BaseModel, Field, EmailStr

class RegisterRequest(BaseModel):
    name: str = Field(..., max_length=100)
    email: EmailStr = Field(...)
    password: str = Field(..., min_length=8)


class LoginRequest(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)


class ProfileResponse(BaseModel):
    id: str
    name: str
    avatar: str | None
    email: str

class ProfileWithTokenResponse(ProfileResponse):
    token: str