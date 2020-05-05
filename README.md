# Files comparison
[![Test Coverage](https://api.codeclimate.com/v1/badges/b7bcfe5afa1f76f97e35/test_coverage)](https://codeclimate.com/github/PolyMaG/python-project-lvl2/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/b7bcfe5afa1f76f97e35/maintainability)](https://codeclimate.com/github/PolyMaG/python-project-lvl2/maintainability)
[![Build Status](https://travis-ci.com/PolyMaG/python-project-lvl2.svg?branch=master)](https://travis-ci.com/PolyMaG/python-project-lvl2)

**Files comparison** is a CLI-utility that compares two configuration files.
## Installation
To install the utility use:
```
pip install -i https://test.pypi.org/simple/ polymag-gendiff
```
You may also need to install some extra packages (e.g. PyYaml). For this case use:
```
pip install --no-cache-dir --index-url https://test.pypi.org/simple --extra-index-url https://pypi.org/simple polymag-gendiff
```
## Usage
To run the utility after installing type:
`gendiff first_file second_file`.

Files formats can be either *.json* or *.yml / .yaml*.

The result of comparison can also be displayed in different formats.

To choose format add optional argument `--format`:
- **_json_** for json format
- **_plain_** for plain format
- **_default_** for json-like txt format. This format is used as a default.

E.g. `gendiff --format plain first_file second_file`

You can always call `gendiff -h` for some __help__ information


Some examples are shown below:
##### Installing ang flat _.json_ and _.yaml_ files comparison
[![asciicast](https://asciinema.org/a/XRoBnGZrgcrbVSWF2ELRuufPJ.svg)](https://asciinema.org/a/XRoBnGZrgcrbVSWF2ELRuufPJ)

##### Nested _.json_ and _.yml_ files comparison with _default_ output format
[![asciicast](https://asciinema.org/a/UgqbrmZfm5jE2mClos2RScJXV.svg)](https://asciinema.org/a/UgqbrmZfm5jE2mClos2RScJXV)

##### _Plain_ output format
[![asciicast](https://asciinema.org/a/SOBDNNJoWB9QwobcRjSUbWHFJ.svg)](https://asciinema.org/a/SOBDNNJoWB9QwobcRjSUbWHFJ)

##### _Json_ output format
[![asciicast](https://asciinema.org/a/5dO4ddlAb94YuCjEcQdQcUkYN.svg)](https://asciinema.org/a/5dO4ddlAb94YuCjEcQdQcUkYN)