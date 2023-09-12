from fastapi import APIRouter
from app.api.transactions.create_transaction import create_transaction, CreateTranscationResponseModel

api_router = APIRouter(prefix='/api')

api_router.add_api_route('/v1/transactions', create_transaction, methods=['POST'],
                         tags=['Transaction'], response_model=CreateTranscationResponseModel)

