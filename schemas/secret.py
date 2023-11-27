def secretEntity(secret) -> dict:
    return {
        'id': str(secret['_id']),
        'secret': secret['secret'],
        'secret_key': secret['secret_key'],
        'password': secret['password'],
        'inserted': secret['inserted']
    }


def secretsEntity(entity) -> list:
    return [secretEntity(secret) for secret in entity]
