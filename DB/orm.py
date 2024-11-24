from DB.models import UsersOrm
from DB.database import sync_engine, Base, session_factory



def create_tables():
    print("Creating")
    sync_engine.echo=True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)


def insert_workers():
    with session_factory() as session:
        worker_jack = UsersOrm(user_name="Jack")
        worker_michael = UsersOrm(user_name="Michael")
        session.add_all([worker_jack, worker_michael])
        session.commit()