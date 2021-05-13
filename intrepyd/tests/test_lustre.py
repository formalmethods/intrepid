from intrepyd.lustre2py import translator
from intrepyd.context import Context
import importlib
import time
import unittest
import os
from . import from_fixture_path

class TestLustre(unittest.TestCase):
    def test_it_translates(self):
        module = 'encoding'
        outfile = module + '.py'
        translator.translate(from_fixture_path('lustre/peterson_1.lus'), 'top', outfile, 'real')
        time.sleep(1) # Give some extra time to write encoding.py to a file
        enc = importlib.import_module(module)
        ctx = Context()
        circ = enc.mk_instance(ctx, 'test')
        circ.mk_circuit()
        self.assertTrue('OK' in circ.outputs)
        os.remove(outfile)

if __name__ == "__main__":
    unittest.main()
