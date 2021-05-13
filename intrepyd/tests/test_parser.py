from intrepyd.parser import Parser
import unittest
import tempfile
import io
import os

class TestParser(unittest.TestCase):
    def test_it_parses_inputs(self):
        stream = io.StringIO(
            """
            i1 = input bool
            i2 = input bool
            a1 = and i1 i2
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({'__n1': 1, '__n2': 2, 'a1': 10, 'false': 2, 'i1': 8, 'i2': 9, 'true': 1}, ctx.nets)

    def test_it_parses_latches(self):
        stream = io.StringIO(
            """
            l1 = latch bool
            set_latch_init_next l1 true false
            l2 = latch bool
            set_latch_init_next l2 false true
            o1 = or l1 l2
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({'__n1': 1, '__n2': 2, 'false': 2, 'l1': 8, 'l2': 9, 'o1': 10, 'true': 1}, ctx.nets)

    def test_it_parses_numbers(self):
        stream = io.StringIO(
            """
            n0 = number 0 int8
            n1 = number 1 int8
            a1 = add n0 n1
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({'__n1': 1, '__n2': 2, 'a1': 9, 'false': 2, 'n0': 8, 'n1': 9, 'true': 1}, ctx.nets)

    def test_it_parses_comments(self):
        stream = io.StringIO(
            """
            # This is a comment
            l1 = latch bool
            set_latch_init_next l1 true false
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({'__n1': 1, '__n2': 2, 'false': 2, 'l1': 8, 'true': 1}, ctx.nets)

    def test_it_parses_types(self):
        stream = io.StringIO(
            """
            i1 = input bool
            i2 = input int8
            i3 = input int16
            i4 = input int32
            i5 = input uint8
            i6 = input uint16
            i7 = input uint32
            i8 = input float16
            i9 = input float32
            i10 = input float64
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({
            '__n1': 1,
            '__n2': 2,
            'false': 2,
            'i1': 8,
            'i10': 17,
            'i2': 9,
            'i3': 10,
            'i4': 11,
            'i5': 12,
            'i6': 13,
            'i7': 14,
            'i8': 15,
            'i9': 16,
            'true': 1
        }, ctx.nets)

    def test_it_parses_files(self):
        with tempfile.TemporaryDirectory() as dirname:
            filepath = os.path.join(dirname, 'temp.itd')
            f = open(filepath, 'wt')
            f.write(
                """
                i1 = input bool
                n1 = not i1
                """
            )
            f.close()
            parser = Parser()
            ctx = parser.parse_file(filepath)
            self.assertEqual({'__n1': 1, '__n2': 2, 'false': 2, 'i1': 8, 'n1': 9, 'true': 1}, ctx.nets)

    def test_it_parses_and_creates(self):
        stream = io.StringIO(
            """
            i1 = input bool
            i2 = input bool
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({'__n1': 1, '__n2': 2, 'false': 2, 'i1': 8, 'i2': 9, 'true': 1}, ctx.nets)
        ctx.mk_and(ctx.nets['i1'], ctx.nets['i2'], 'a1')
        self.assertEqual({'__n1': 1, '__n2': 2, 'false': 2, 'i1': 8, 'i2': 9, 'a1': 10, 'true': 1}, ctx.nets)

    def test_it_parses_relations(self):
        stream = io.StringIO(
            """
            n1 = number 0 int8
            i1 = input int8
            e1 = eq n1 i1
            """
        )
        parser = Parser()
        ctx = parser.parse_stream(stream)
        self.assertEqual({'__n1': 1, '__n2': 2, 'e1': 11, 'false': 2, 'i1': 9, 'n1': 8, 'true': 1}, ctx.nets)

if __name__ == '__main__':
    unittest.main()
