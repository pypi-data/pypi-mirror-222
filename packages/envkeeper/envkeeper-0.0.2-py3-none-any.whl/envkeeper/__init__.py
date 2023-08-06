from .container import StorageContainer


# TODO: Match javascripts localStorage API.
def new(key: str):
    return StorageContainer.from_env(key)
