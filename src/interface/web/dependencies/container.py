from fastapi import Request

from infrastructure.di.container import Container


def get_di_container(request: Request) -> Container:
    return request.state.container
