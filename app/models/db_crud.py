# all db crud operations
from sqlalchemy import Table
from app.extensions import db

def return_single_record(table: Table, **kwargs) -> Table:
    """return a single record from db"""

    return table.query.filter_by(**kwargs).first()


def return_all_record(table: Table) -> list[Table]:
    return table.query.filter_by(**kwargs).all()


def save_record(table: Table, **data) -> Table:
    """saves data to db and returns the record"""

    record = table(**data)

    db.session.add(record)
    db.session.commit()
    db.session.refresh(record)

    return record
