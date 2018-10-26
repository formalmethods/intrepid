#!/bin/bash
antlr4 IEC61131Parser.g4 -visitor -no-listener -Dlanguage=Python2
