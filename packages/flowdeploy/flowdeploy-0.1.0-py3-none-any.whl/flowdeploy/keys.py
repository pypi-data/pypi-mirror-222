import os
from loguru import logger


def get_key():
    """Retrieves the Toolchest API key, if it is set."""

    try:
        key = os.environ["TOOLCHEST_KEY"]
    except KeyError as e:
        logger.error("Key not found. Please set environment variable TOOLCHEST_KEY to your Toolchest API key.")
        logger.error("Function call:")
        logger.error("    flowdeploy.set_key(YOUR_KEY_HERE)")
        return e
    return key


def set_key(key):
    """Sets the Toolchest auth key (env var TOOLCHEST_KEY) to the given value.

    :param key: key value (str) or path to file containing key. If given a filename,
        the file must consist of only the key itself.

    Usage::

        >>> import flowdeploy
        >>> flowdeploy.set_key(YOUR_KEY_HERE)

    """

    if os.path.isfile(key):
        with open(key, "r") as f:
            os.environ["TOOLCHEST_KEY"] = f.read().strip()
    else:
        os.environ["TOOLCHEST_KEY"] = key
