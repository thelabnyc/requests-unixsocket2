#!/usr/bin/env python

from setuptools import setup

setup(
    setup_requires=["pbr"],
    install_requires=[
        # Requests >=2.32.2 blocked by:
        # https://github.com/msabramo/requests-unixsocket/pull/72
        "requests>=1.1,<2.32.2",
        # urllib3 >= 2 is currently blocked by this issue:
        # - https://github.com/msabramo/requests-unixsocket/issues/70
        # - https://github.com/msabramo/requests-unixsocket/pull/69
        "urllib3<2",
    ],
    pbr=True,
)
