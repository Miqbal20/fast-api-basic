from app.models import Base
import sqlalchemy as sq


class Transaction(Base):
    __tablename__ = 'transaction'

    id = sq.Column('id', sq.Integer, primary_key=True)
    user_id = sq.Column('user_id', sq.Integer)
    created_at = sq.Column('created_at', sq.DateTime)
    modified_at = sq.Column('modified_at', sq.DateTime)
    status = sq.Column('status', sq.Integer)
    total = sq.Column('total', sq.Integer)
