#!/bin/bash

antlr IEC61131Parser.g4 -visitor -no-listener -Dlanguage=Python3
