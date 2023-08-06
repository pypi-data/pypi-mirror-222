![PyPI - License](https://img.shields.io/pypi/l/pydeum)
![PyPI](https://img.shields.io/pypi/v/pydeum?label=version)
![GitHub issues](https://img.shields.io/github/issues/Iodeum/pydeum)

> **IMPORTANT**
> This project is not released yet

# 1. Installation

```shell
pip3 install pydeum
```

# 2. Usage

You can use ```pydeum``` in many different ways, such as to get transactions or check addresses.

## 2.1. Transactions

```python
import pydeum as pyd

# Add a transaction to the mempool
pyd.push("from_address", "to_address", 100)

# Review a transaction
pyd.check("from_address", "to_address", 100)

# Get 10 last transactions from an address
pyd.get("address", 10)

# Get the current balance of an address
pyd.balance("address", 10)
```
