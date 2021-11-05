import unittest
from intrepyd.formula2py.parser import parse_string

class TestFormulaParser(unittest.TestCase):
    """
    Tests for the formula parser
    """
    def test_it_parses_correct_formulas(self):
        """
        Basic parsing
        """
        self.assertDictEqual({'AND': ['a', 'b']}, parse_string('a and b'))
        self.assertDictEqual({'OR': ['a', 'b']}, parse_string('a or b'))
        self.assertDictEqual({'NOT': 'a'}, parse_string('not a'))
        self.assertDictEqual({'PRE': 'a'}, parse_string('pre a'))
        self.assertEqual('a', parse_string('a'))
        self.assertEqual('a', parse_string('(a)'))
        self.assertDictEqual({'AND': ['a', 'b']}, parse_string('(a and b)'))
        self.assertDictEqual(
            {'AND':
                ['a',
                    {'OR':
                        [{'PRE': 'b'},
                         {'NOT': 'c'}
                        ]
                    }
                ]
            },
            parse_string('a and (pre b or not c)'))
        self.assertDictEqual(
            {'PRE': {'PRE': 'b'}},
            parse_string('pre pre b'))

if __name__ == '__main__':
    unittest.main()
