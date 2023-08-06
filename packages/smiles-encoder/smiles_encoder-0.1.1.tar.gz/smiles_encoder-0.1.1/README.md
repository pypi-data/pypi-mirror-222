# smiles-encoder: One-hot encoding for simple molecular-input line-entry system (SMILES) strings

[![GitHub version](https://badge.fury.io/gh/tjkessler%2Fsmiles-encoder.svg)](https://badge.fury.io/gh/tjkessler%2Fsmiles-encoder)
[![PyPI version](https://badge.fury.io/py/smiles-encoder.svg)](https://badge.fury.io/py/smiles-encoder)
[![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/tjkessler/smiles-encoder/master/LICENSE.txt)

smiles-encoder is a Python package used to generate one-hot vectors representing SMILES strings (each string element is a one-hot vector).

## Installation

Installation via pip:

```
$ pip install smiles-encoder
```

Installation via cloned repository:

```
$ git clone https://github.com/tjkessler/smiles-encoder
$ cd smiles-encoder
$ python setup.py install
```

smiles-encoder does not require any dependencies.

## Basic Usage

First, assemble a list of SMILES strings:

```python
smiles_strings = [
    'O=Cc1ccc(O)c(OC)c1',  # Vanillin
    'CC(=O)NCCC1=CNc2c1cc(OC)cc2',  # Melatonin
    'C1CCCCC1',  # Cyclohexane
    'C1=CC=CC=C1'  # Benzene
]
```

Import the SmilesEncoder object, and pass it the list of SMILES strings during initialization to construct the element dictionary:

```python
from smiles_encoder import SmilesEncoder

encoder = SmilesEncoder(smiles_strings)
```

Use the encoder to encode SMILES strings:

```python
encoded_smiles = encoder.encode_many(smiles_strings)

# OR

encoded_smiles = [encoder.encode(s) for s in smiles_strings]
```

Use the encoder to decode encoded SMILES strings:

```python
decoded_smiles = encoder.decode_many(encoded_smiles)

# OR

decoded_smiles = [encoder.decode(e) for e in encoded_smiles]
```

## Contributing, Reporting Issues and Other Support

To contribute to smiles-encoder, make a pull request. Contributions should include extensive documentation.

To report problems with the software or feature requests, file an issue. When reporting problems, include information such as error messages, your OS/environment and Python version.

For additional support/questions, contact Travis Kessler (travis.j.kessler@gmail.com).
