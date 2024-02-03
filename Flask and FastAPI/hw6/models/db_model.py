import databases
import sqlalchemy

DATABASE_URL = "sqlite:///sql_app.db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

tasks = sqlalchemy.Table(
    "tasks",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("name", sqlalchemy.String(64)),
    sqlalchemy.Column("description", sqlalchemy.String(128)),
    sqlalchemy.Column("status_complete", sqlalchemy.Boolean),
)

engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata.create_all(engine)
