#
# File:    ./tests/unit/test_version.py
# Author:  Jiří Kučera <sanczes AT gmail.com>
# Date:    2022-11-15 10:39:08 +0100
# Project: vutils-parsing: Grammars, automata, and parsing library
#
# SPDX-License-Identifier: MIT
#
"""Test `vutils.parsing.version` module."""

from vutils.testing.testcase import TestCase

from vutils.parsing.version import __version__


class VersionTestCase(TestCase):
    """Test case for version."""

    __slots__ = ()

    def test_version(self):
        """Test if version is defined properly."""
        self.assertIsInstance(__version__, str)
