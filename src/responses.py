from enum import Enum


class AppResponses(Enum):
    SUCCESS = 'SUCCESS'
    NO_LICENCE_PLATE_FOUND = 'NO_LICENCE_PLATE_FOUND'
    NO_EGV_INFO_FOUND = 'NO_EGV_INFO_FOUND'
    UNEXPECTED_ERROR = 'UNEXPECTED_ERROR'
    FILE_NOT_ALLOWED = 'FILE_NOT_ALLOWED'
    IMAGE_FILE_SIZE_TOO_BIG = 'IMAGE_FILE_SIZE_TOO_BIG'

    def __str__(self):
        return self._value_
