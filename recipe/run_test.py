import os
if 'USER' not in os.environ:
    os.environ['USER'] = 'TEST_CONDA_USER'
if 'HOME' not in os.environ:
    os.environ['HOME'] = '/tmp/'

import omas
import unittest

loader = unittest.TestLoader()
suite = loader.discover(
    start_dir=os.path.dirname(omas.__file__),
    pattern='*_core.py'
)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

if not result.wasSuccessful():
    raise SystemExit(1)