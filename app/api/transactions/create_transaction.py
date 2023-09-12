from fastapi import Header
from sqlalchemy.orm import Session
from fastapi.exception_handlers import HTTPException
from app.api_models import BaseResponseModel
from app.utils.db import db_engine
from app.models.transaction import Transaction


class CreateTranscationResponseModel(BaseResponseModel):
    class Config:
        json_schema_extra = {
            'example': {
                'data': {
                    'id': 1,
                    'url': '/app/v1/transactions/1'
                },
                'meta': {},
                'success': True,
                'code': 200,
                'message': 'Success'
            }
        }


async def create_transaction(user_id: int = Header(0, alias='X-Consumer-ID')):
    if user_id == 0:
        raise HTTPException(403, detail='Anda tidak punya hak akses')

    with Session(db_engine) as session:
        transaction = Transaction(user_id=user_id)
        session.add(transaction)
        session.commit()

        return CreateTranscationResponseModel(
            data={
                'id': transaction.id,
                'url': f'/api/v1/transactions/{transaction.id}'
            }
        )
