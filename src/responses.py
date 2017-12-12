from enum import Enum


class AppResponses(Enum):
    SUCCESS = 'SUCCESS'
    NO_LICENCE_PLATE_FOUND = 'NO_LICENCE_PLATE_FOUND'
    UNEXPECTED_ERROR = 'UNEXPECTED_ERROR'
    FILE_NOT_ALLOWED = 'FILE_NOT_ALLOWED'

    def __str__(self):
        return self._value_
