def secretEntity(secret) -> dict:
    return {
        'id': str(secret['_id']),
        'secret': secret['secret'],
        'url': secret['url'],
        'password': secret['password']
    }

def secretsEntity(entity) -> list:
    return [secretEntity(secret) for secret in entity]