import os
if 'USER' not in os.environ:
    os.environ['USER'] = 'TEST_CONDA_USER'
if 'HOME' not in os.environ:
    os.environ['HOME'] = '/tmp'
import omas
import unittest
unittest.main(omas)
