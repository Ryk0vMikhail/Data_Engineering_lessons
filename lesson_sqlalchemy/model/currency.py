from sqlalchemy import Column, Integer, VARCHAR, Date, Float, TIMESTAMP

from .base import Base

class Currency(Base):
    __tablename__='wether'
    id = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    location = Column(VARCHAR(50), nullable=False)
    date = Column(Date, nullable=False)
    min_temp_day = Column(Float, nullable=False)
    max_temp_day = Column(Float, nullable=False)
    avg_temp_day = Column(Float, nullable=False)
    date_created = Column(TIMESTAMP, nullable=False, index=True)