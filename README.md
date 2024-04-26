# Syntax Analyzer

## Overview

This project sets out to take a set of input strings (or a single string) that should be validated against a given
set of **CFG** (Context-Free Grammar) production rules.
The rules were then broken down into a **PPT** (Predictive Parsing Table).

The PPT was used to create a map in Python that allowed for a production rule and symbol (from the input string) to
determine if the current symbol was expected or if another set of rules/symbols needed to be added back into the stack.

The entire process runs over the length of the input string (unless the current input symbol or rule/symbol combo are
not found in the PPT) to validate the entirety of the input string. If a rule/symbol combo is found not to be in the
PPT, the program invalidates the string and outputs this information. Through each iteration, the current stack is
printed out.

## Running the Program

`python main.py`
