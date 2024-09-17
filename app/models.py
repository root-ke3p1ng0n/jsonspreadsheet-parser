from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)

    conversion_records = relationship('ConversionRecord', back_populates='user')

class ConversionTypes(str, Enum):
    JSON_TO_EXCEL = 'json_to_excel'
    EXCEL_TO_JSON = 'excel_to_json'

class ConversionRecord(Base):
    __tablename__ = 'conversion_records'

    id = Column(Integer, primary_key=True, index=True)
    conversion_type = Column(Enum(ConversionTypes), nullable=False)
    file_path = Column(String, nullable=False)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='conversion_records')
    