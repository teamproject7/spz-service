from enum import Enum


class AppMessages(Enum):
    LICENCE_PLATE_FOUND = 'License plate found'
    NO_LICENCE_PLATE_FOUND = 'No licence plate found'
    UNEXPECTED_ERROR = 'Unexpected error'
    FILE_NOT_ALLOWED = 'File is not allowed'
    IMAGE_FILE_SIZE_TOO_BIG = 'Image file is too big. Limit is 1MB'

    def __str__(self):
        return self._value_
