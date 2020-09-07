from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, declarative_base, func

engine = create_engine('sqlite:///Resources/hawaii.sqlite', convert_unicode=True)
session = Session(engine)
Base = declarative_base()
Base.query = session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    import apply.apps.models
    Base.metadata.create_all(bind=engine)