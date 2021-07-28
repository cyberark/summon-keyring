# summon-keyring

Cross-platform provider for [Summon](https://github.com/cyberark/summon) that talks to keyrings.

Wraps the Python [keyring library](https://pypi.python.org/pypi/keyring) to allow summon to fetch credentials from:

* OSX Keychain
* Linux Secret Service
* Windows Credential Vault
* gnome-keyring
* kwallet

## Requirements

To use this provider, you will need to install:
- [Summon](https://cyberark.github.io/summon/)
- Python and `pip`
- The Python [keyring](https://pypi.python.org/pypi/keyring) library.
  - Note: v21+ of this library requires Python 3.6+.

To install the Python `keyring` library, run:
```sh-session
$ pip install keyring
```

## Installation

Install the keyring provider by  cloning the repo and creating a symlink in the
`/usr/local/lib/summon` directory.

You may need to run the following commands as a super user.

```
$ git clone git@github.com:cyberark/summon-keyring.git
$ cd summon-keyring
$ mkdir -p /usr/local/lib/summon
$ ln -s "$PWD/ring.py" /usr/local/lib/summon/keyring.py
```

**Note**: If you copy the `ring.py` file to `/usr/local/lib/summon/` instead
of symbolically linking it, you may see an error like:
```
Traceback (most recent call last):
  File "/usr/local/lib/summon/ring.py", line 22, in <module>
    value = keyring.get_password(
AttributeError: module 'keyring' has no attribute 'get_password'
```
This can be resolved by creating a symbolic link instead.

## Usage instructions

To use this provider, invoke Summon as usual. If you have multiple providers
installed, be sure to provide the path to the keyring provider using the
`--provider` flag:
```
summon --provider keyring.py \
  --yaml 'MY_ENV_VAR: !var secret/path' \
  my_command
```

By default, this provider fetches secrets from the service `summon`. To
retrieve secrets from another service, set the `SUMMON_KEYRING_SERVICE`
environment variable.

### Example

Let's use the OSX keychain to store a secret and fetch it with summon.

First, we add the secret:

```
$ security add-generic-password -s "summon" -a "secret/path" -w "secretvalue"
```

**Note**: You can also add a secret to the OSX keychain through the Keychain
Access utility.  The "Keychain Item Name" field should be `summon`, the
"Account Name" should be the secret path, and the "Password" field should
contain the secret value. If you are using other secret stores, you can also
use the `keyring` command utility installed with the `keyring` Python package
to set the secret:
```
$ keyring set summon secret/path # enter "secretvalue" when prompted
```

Once the secret has been added, we can fetch it with summon by using this provider.

```sh-session
$ summon --provider keyring.py \
  --yaml 'MYSECRET: !var secret/path' \
  printenv MYSECRET

secretvalue
```

Using summon, you can easily switch between this keyring provider for development and use and more appropriate provider, like [Conjur](http://conjur.net/), in production.

## Contributing

We welcome contributions of all kinds to this repository. For instructions on how to get started and descriptions
of our development workflows, please see our [contributing guide](CONTRIBUTING.md).

## License

Copyright (c) 2020 CyberArk Software Ltd. All rights reserved.

Licensed under the MIT License (MIT).

For the full license text see [`LICENSE`](LICENSE).
