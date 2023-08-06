# EnvKeeper [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/christopherwoodall/blobstorage/blob/master/examples/blobstorage_example.ipynb)
### Like `localStorage`, but for `python`!

Simple Python library for managing and storing variables as JSON-encoded dictionaries in environment variables. It provides a dictionary-like interface for storing and retrieving data in environment variables, and allows for global access once stored.


## Installation

Install EnvKeeper via pip:
```bash
pip install envkeeper
```


## Usage

See the `Makefile` for a list of examples and available commands.

Here's a basic example of using BlobStorage:

```python
from envkeeper import StorageContainer

# Create an instance with an environment variable key
# Be sure to replace `'MY_VAR'` with the actual name of the environment variable you want to use.
store = StorageContainer('MY_VAR')

# Set items
store['foo'] = 'bar'
store['baz'] = 42

# Get items
print(store['foo'])  # Outputs: 'bar'
print(store['baz'])  # Outputs: 42

# Delete items
del store['foo']

# Check if a key exists
print('baz' in store)  # Outputs: True
```


## Contributing

Contributions are welcome! Please feel free to submit a pull request.


## License

This project is licensed under the terms of the MIT license.
