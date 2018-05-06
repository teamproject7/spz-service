import uuid

from src.egv_db_service import get_all_info


def create_egv_object(plate):
    info, violations, checks = get_all_info(plate['plate'])

    # no info found
    if not info:
        return {
            "id": str(uuid.uuid4()),
            "plate": plate['plate'],
            "coordinates": plate['coordinates']
        }

    # :D:D:D
    def get_info(key):
        if info[key] is None:
            return ''

        return info[key]

    return {
        "id": str(uuid.uuid4()),
        "plate": plate['plate'],
        "coordinates": plate['coordinates'],
        "vehicle": {
            "id": get_info('car_id'),
            "parameters": {
                "model": get_info('car_model'),
                "brand": get_info('car_company'),
                # "year": random.choice(YEARS),
                "color": get_info('car_color'),
            },
            "owner": {
                "id": get_info('owner_id'),
                "pid": get_info('owner_pid'),
                "fullname": "{} {}".format(get_info('owner_name'), get_info('owner_surname')),
                "violations": violations
            },
            "insurance": {
                "company": get_info('insurance_company'),
                "type": get_info('insurance_type'),
                "year": get_info('insurance_year'),
                "valid": get_info('insurance_valid')
            },
            "checks": checks
        }
    }


def get_egv_response(alpr_res):
    plates = [create_egv_object(plate) for plate in alpr_res['results']]

    return {
        "processing_time_ms": alpr_res['processing_time_ms'],
        "data": plates
    }
