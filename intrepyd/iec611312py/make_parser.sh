#!/bin/bash
# java org.antlr.v4.Tool IEC61131Parser.g4 -visitor -no-listener -Dlanguage=Python2
antlr4 IEC61131Parser.g4 -visitor -no-listener -Dlanguage=Python2
