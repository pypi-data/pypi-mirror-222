from .container import StorageContainer


def new(key: str):
    return StorageContainer.from_env(key)
