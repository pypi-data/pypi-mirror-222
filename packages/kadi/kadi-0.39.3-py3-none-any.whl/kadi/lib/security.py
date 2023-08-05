# Copyright 2022 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import hashlib
import os
import string
from secrets import SystemRandom
from time import time

import jwt
from flask import current_app


def random_alnum(num_chars=16):
    """Generate a secure random alphanumeric string.

    :param num_chars: (optional) The number of chars to generate.
    :return: The generated string.
    """
    alphanum = string.ascii_letters + string.digits
    return "".join(SystemRandom().choice(alphanum) for _ in range(num_chars))


def random_bytes(num_bytes=24, hexadecimal=True):
    """Generate a secure random byte sequence.

    :param length: (optional) The number of bytes to generate.
    :param hexadecimal: (optional) Whether to return the bytes in a hexadecimal string
        representation.
    :return: The generated byte sequence or hexadecimal string.
    """
    byte_sequence = os.urandom(num_bytes)

    if hexadecimal:
        return byte_sequence.hex()

    return byte_sequence


def hash_value(value, alg="sha256", hexadecimal=True):
    """Create a secure hash of a value.

    :param value: The value to hash, either a bytes-like object or a string.
    :param alg: (optional) The hash algorithm to use, according to the algorithms
        available in Python's "hashlib" module.
    :param hexadecimal: (optional) Whether to return the hash in a hexadecimal string
        representation.
    :return: The calculated hash as a byte sequence or hexadecimal string or ``None`` if
        the given algorithm is not available.
    """
    try:
        memoryview(value)
    except TypeError:
        value = value.encode()

    if alg not in hashlib.algorithms_available:
        return None

    hashed_value = getattr(hashlib, alg)(value)

    if hexadecimal:
        return hashed_value.hexdigest()

    return hashed_value.digest()


def encode_jwt(payload, expires_in=None):
    """Encode a given payload inside a JSON web token.

    :param payload: The payload to encode as dictionary, which needs to be JSON
        serializable.
    :param expires_in: (optional) The time in seconds that the token should expire in.
    :return: The encoded token as string.
    """
    if expires_in is not None:
        payload["exp"] = int(time()) + expires_in

    return jwt.encode(payload, current_app.secret_key, algorithm="HS256")


def decode_jwt(token):
    """Decode a given JSON web token.

    :param token: The token to decode as string.
    :return: The decoded payload dictionary or ``None`` if the token is invalid or
        expired.
    """
    try:
        return jwt.decode(token, current_app.secret_key, algorithms=["HS256"])
    except jwt.InvalidTokenError:
        return None
