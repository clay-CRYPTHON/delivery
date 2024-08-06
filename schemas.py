from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    username: str
    email: str
    password: str
    is_staff: Optional[bool] = False
    is_active: Optional[bool] = True

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'Abbbose',
                'email': 'abbossetdarov3@gmail.com',
                'password': '12345',
                'is_staff': False,
                'is_active': True,
            }
        }


class Settings(BaseModel):
    authjwt_secret_key: str = '939c73710faefc41b9f2ee3fdf5e3ab7b755d5583c41d285d6a954451de9242a'


class LoginModel(BaseModel):
    username_or_email: str
    password: str


class OrderModel(BaseModel):
    id: Optional[str]
    quantity: int
    order_status: Optional[str] = "PENDING"
    user_id: Optional[int]
    product_id: int

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "quantity": 2,
            }
        }


class OrderStatusModel(BaseModel):
    order_statuses: Optional[str] = "PENDING"

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "order_statuses": "PENDING",
            }
        }


class ProductModel(BaseModel):
    id: Optional[int]
    name: str
    price: int

    class Config:
        orm_model = True
        schema_extra = {
            "example": {
                "name": "Uzbek Plov",
                "price": 30000,
            }
        }

