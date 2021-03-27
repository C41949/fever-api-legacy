def to_response(self) -> dict:
    response = {**self.__dict__}
    del response['_sa_instance_state']
    return response
