from enum import Enum


class AppMessages(Enum):
    LICENCE_PLATE_FOUND = 'License plate found'
    NO_LICENCE_PLATE_FOUND = 'No licence plate found'
    UNEXPECTED_ERROR = 'Unexpected error'
    FILE_NOT_ALLOWED = 'File is not allowed'

    def __str__(self):
        return self._value_
