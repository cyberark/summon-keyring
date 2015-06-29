# summon-keyring

Cross-platform provider for [Summon](https://github.com/conjurinc/summon) that talks to keyrings.

Wraps the Python [keyring library](https://pypi.python.org/pypi/keyring) to allow summon to fetch credentials from:

* OSX Keychain
* Linux Secret Service
* Windows Credential Vault
* gnome-keyring
* kwallet

This provider requires that you have Python and pip installed.

By default, this provider fetches secrets from the service "summon". Change this by setting the `SUMMON_KEYRING_SERVICE` environment variable.

## Example

Let's use the OSX keychain to store a secret and fetch it with summon.

First, we add the secret:

```sh-session
$ security add-generic-password -s "summon" -a "secret/path" -w "secretvalue"
```

You can also do this through the Keychain Access utility.  The "Keychain Item
Name" field should be "summon", the "Account Name" should be the secret path,
and the "Password" field should contain the secret value.

Now we can fetch it with summon by using this provider.

```sh-session
$ summon -p keyring.py --yaml 'MYSECRET: !var secret/path' printenv MYSECRET
secretvalue
```

Using summon, you can easily switch between this keyring provider for development and use and more appropriate provider, like [Conjur](http://conjur.net/), in production.

## Install

You will need to [install summon](http://conjurinc.github.io/summon/) to
use this provider.

You also need to install the Python [keyring](https://pypi.python.org/pypi/keyring) library.

```sh-session
$ pip install keyring
```

You can install by simply cloning the repo and creating a symlink in the
`/usr/libexec/summon` directory.

You may need to run the following commands as a super user.

```sh-session
$ git clone git@github.com:conjurinc/summon-keyring.git
$ cd summon-keyring
$ mkdir -p /usr/libexec/summon
$ ln -s "$PWD/keyring.py" /usr/libexec/summon/keyring.py

