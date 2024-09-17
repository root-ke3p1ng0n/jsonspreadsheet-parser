from pydantic import BaseModel
from enum import Enum

class ConversionTypes(str, Enum):
    JSON_TO_EXCEL = 'json_to_excel'
    EXCEL_TO_JSON = 'excel_to_json'

class ConversionRecordsBase(BaseModel):
    conversion_type: ConversionTypes
    file_path: str
    user_id: int

class ConversionRecordsCreate(ConversionRecordsBase):
    pass

class ConversionRecords(ConversionRecordsBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    conversion_records: list[ConversionRecords] = []

    class Config:
        orm_mode = True