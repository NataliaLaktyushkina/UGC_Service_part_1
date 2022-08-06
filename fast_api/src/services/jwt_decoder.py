from http import HTTPStatus
from typing import Union

import jwt

from core.config import settings


def jwt_decoder(token: str) -> Union[dict, int]:
    try:
        decode_token = jwt.decode(jwt=token, key=settings.JWT_SECRET_KEY, algorithms=settings.JWT_ALGORITHM)
        return decode_token
    except jwt.ExpiredSignatureError:
        # Signature has expired
        return HTTPStatus.UNAUTHORIZED
