from typing import Any

from infrastructure.di.exception.dependency_not_found import DependencyNotFound


class Container:

    def __init__(self):
        self._dependencies: dict[type, Any] = {}

    def __setitem__[INSTANCE](
        self,
        key: type[INSTANCE],
        value: INSTANCE,
    ) -> None:
        self._dependencies[key] = value

    def __getitem__[INSTANCE](
        self,
        item: type[INSTANCE],
    ) -> INSTANCE:
        dependency = self._dependencies.get(item)

        if not dependency:
            raise DependencyNotFound(f"Dependency '{item}' is not found.")

        return dependency
