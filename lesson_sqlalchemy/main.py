import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from model.base import Base
from model.currency import Currency
from config import SQLALCHEMY_DATABASE_URI
from function_wether import get_wether

engine = create_engine(SQLALCHEMY_DATABASE_URI)

Base.metadata.create_all(bind=engine)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
session_local = sessionLocal

l_dict = get_wether('Lipetsk', 3)

for day in l_dict:
    new_wether = Currency(
        location = day['location'],
        date = day['date'],
        min_temp_day = day['min_temp'],
        max_temp_day = day['max_temp'],
        avg_temp_day = day['avg_temp'],
        date_created = datetime.datetime.now(datetime.UTC)
    )
    session_local.add(new_wether)

session_local.commit()



print(get_wether('Moscow', 3))
