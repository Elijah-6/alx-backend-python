# Unittests and Integration Tests

This repository contains a series of Python scripts and modules designed to demonstrate the implementation of unittests and integration tests. The primary focus is on testing various functionalities of a GitHub organization client.

## Table of Contents

- [Project Structure](#project-structure)
- [Modules](#modules)
- [Testing](#testing)
- [Usage](#usage)
- [License](#license)

## Project Structure

The repository is structured as follows:

```
.
├── [client.py](client.py)
├── [fixtures.py](fixtures.py)
├── [test_client.py](test_client.py)
├── [test_utils.py](test_utils.py)
├── [utils.py](utils.py)
└── [README.md](README.md)
```

## Modules

### `client.py`

This module contains the `GithubOrgClient` class, which interacts with the GitHub API to fetch information about organizations and their repositories.

### `fixtures.py`

This module contains test fixtures used in the integration tests.

### `utils.py`

This module provides utility functions such as `access_nested_map`, `get_json`, and `memoize`.

## Testing

### `test_client.py`

This module contains unittests for the `GithubOrgClient` class using the `unittest` framework and `unittest.mock` for mocking external dependencies.

### `test_utils.py`

This module contains unittests for the utility functions defined in `utils.py`.

## Usage

To run the tests, use the following command:

```bash
python -m unittest discover
```

This command will discover and run all the tests in the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.