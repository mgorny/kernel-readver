#!/usr/bin/env python
# vim: se fileencoding=utf-8 :
# Tests for kernel-readver.
# (c) 2018 Michał Górny
# Released under the terms of the 2-clause BSD license

import os.path
import subprocess
import sys
import unittest


SCRIPT_DIR = os.path.join(os.path.dirname(__file__), '..', 'kernel-readver')
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')


def kernel_readver(filename):
    cmd = [sys.executable, SCRIPT_DIR, os.path.join(DATA_DIR, filename)]
    s = subprocess.Popen(cmd,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    sout, serr = s.communicate()
    if s.returncode != 0:
        raise subprocess.CalledProcessError(s.returncode, cmd, serr)
    return sout.decode().rstrip('\n')


class CLITests(unittest.TestCase):
    def test_x86_bzImage(self):
        self.assertEqual('4.18.0-pf11-mgorny-amd64+',
                kernel_readver('vmlinuz-4.18.0-pf11-mgorny-amd64+'))


if __name__ == '__main__':
    unittest.main()
