import os
import json

class StorageContainer:
    """Class for managing environment variables as JSON-encoded dictionaries.

    This class provides a dictionary-like interface for storing and retrieving
    data in environment variables, which are encoded as JSON strings.
    """

    MAX_LENGTH = 32000  # Conservative maximum length for compatibility with Windows

    def __init__(self, key: str = None):
        """Initialize the store with a given environment variable key.

        Args:
            key (str): The key for the environment variable.
        """
        self.key = key

    def use(self, key: str):
        """Set the environment variable key for this instance.

        Args:
            key (str): The key for the environment variable.
        """
        self.key = key
        return self

    def __getitem__(self, item: str):
        """Retrieve an item from the environment variable.

        Args:
            item (str): The key of the item to retrieve.

        Returns:
            The value associated with the item key.

        Raises:
            KeyError: If the item key is not found in the environment variable.
        """
        data = self._retrieve()
        if item not in data:
            raise KeyError(f"{item} not found in environment variable {self.key}")
        return data[item]

    def __setitem__(self, item: str, value: str):
        """Set an item in the environment variable.

        Args:
            item (str): The key of the item to set.
            value: The value to associate with the item key.

        Raises:
            ValueError: If storing the data would exceed the maximum length.
        """
        data = self._retrieve()
        data[item] = value
        self._store(data)

    def __delitem__(self, item: str):
        """Delete an item from the environment variable.

        Args:
            item (str): The key of the item to delete.

        Raises:
            KeyError: If the item key is not found in the environment variable.
        """
        data = self._retrieve()
        if item not in data:
            raise KeyError(f"{item} not found in environment variable {self.key}")
        del data[item]
        self._store(data)

    def __contains__(self, item: str):
        """Check if an item exists in the environment variable.

        Args:
            item (str): The key of the item to check.

        Returns:
            True if the item key exists, False otherwise.
        """
        data = self._retrieve()
        return item in data

    def _store(self, data: str):
        """Store data in the environment variable.

        Args:
            data (dict): The data to store.

        Raises:
            ValueError: If storing the data would exceed the maximum length.
        """
        encoded = json.dumps(data)
        if len(encoded) > self.MAX_LENGTH:
            raise ValueError(f"Storing data would exceed maximum length of {self.MAX_LENGTH}")
        os.environ[self.key] = encoded

    def _retrieve(self):
        """Retrieve data from the environment variable.

        Returns:
            The data retrieved from the environment variable, or an empty dictionary
            if the environment variable is not set or does not contain valid JSON.
        """
        if self.key not in os.environ:
            return {}
        try:
            return json.loads(os.environ[self.key])
        except json.JSONDecodeError:
            return {}

    @classmethod
    def from_env(cls, key: str):
        """Create a StorageContainer instance from an environment variable key."""
        return cls(key)
