def secretEntity(item) -> dict:
    return {
        'id': str(item['_id']),
        'secret': item['secret'],
        'url': item['url'],
        'password': item['password']
    }

def secretsEntity(entity) -> list:
    return [secretEntity(item) for item in entity]