from enum import Enum


class AppResponses(Enum):
    LICENCE_PLATE_FOUND = 'LICENCE_PLATE_FOUND'
    NO_LICENCE_PLATE_FOUND = 'NO_LICENCE_PLATE_FOUND'
    UNEXPECTED_ERROR = 'UNEXPECTED_ERROR'
    FILE_NOT_ALLOWED = 'FILE_NOT_ALLOWED'

    def __str__(self):
        return self._value_
