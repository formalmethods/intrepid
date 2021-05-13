Module intrepyd.parser
======================
A parser for the Intrepid's language

Classes
-------

`ParseError(message)`
:   Encapsulates a parsing error

    ### Ancestors (in MRO)

    * builtins.Exception
    * builtins.BaseException

    ### Methods

    `message(self)`
    :   Retrieves the error message

`Parser()`
:   A parser for Intrepid's syntax

    ### Methods

    `parse_file(self, filepath)`
    :   Parses the file, and returns the context

    `parse_stream(self, stream)`
    :   Parses the stream, and returns the context