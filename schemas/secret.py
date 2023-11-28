def secretEntity(secret) -> dict:
    return {
        'id': str(secret['_id']),
        'secret': secret['secret'],
        'secret_key': secret['secret_key'],
        'password': secret['password'],
        'inserted': secret['inserted']
    }

def secret_keyEntity(secret) -> dict:
    return {
        'secret_key': secret['secret_key']
    }


def secretsEntity(entity) -> list:
    return [secretEntity(secret) for secret in entity]
