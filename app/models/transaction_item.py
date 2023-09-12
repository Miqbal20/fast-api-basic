from app.models import Base
import sqlalchemy as sq


class TransactionItem(Base):
    __tablename__ = 'transaction_item'

    id = sq.Column('id', sq.Integer, primary_key=True)
    user_id = sq.Column('user_id', sq.Integer)
    transaction_id = sq.Column('transaction_id', sq.Integer)
    created_at = sq.Column('created_at', sq.DateTime)
    modified_at = sq.Column('modified_at', sq.DateTime)
    product_id = sq.Column('product_id', sq.Integer)
    product_name = sq.Column('product_name', sq.String)
    price = sq.Column('price', sq.Integer)
    qty = sq.Column('qty', sq.Integer)
    total = sq.Column('total', sq.Integer)

