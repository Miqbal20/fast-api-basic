from app.models import Base
import sqlalchemy as sq


class Product(Base):
    __tablename__ = 'product'

    id = sq.Column('id', sq.Integer, primary_key=True)
    barcode = sq.Column('barcode', sq.String)
    name = sq.Column('name', sq.String)
    price = sq.Column('price', sq.Integer)
    is_active = sq.Column('is_active ', sq.SmallInteger)
    created_at = sq.Column('created_at', sq.DateTime)
    modified_at = sq.Column('modified_at', sq.DateTime)

