#!/usr/bin/env python

from setuptools import setup

setup(
    name='pretix-icepay',
    version="0.0.1",
    description="Pretix extension for the Icepay payment provider.",
    author='chotee',
    author_email='chotee@openended.eu',
    packages=['pretix_icepay'],
    install_requires=['icepay_python'],
    url="https://github.com/chotee/pretix-icepay",
    entry_points="""
[pretix.plugin]
pretix_icepay=pretix_icepay:PretixPluginMeta
"""
)