import time
from typing import (
    Dict,
    List,
    Optional
)
from dataclasses import (
    field,
    dataclass
)
from collections import deque

import settings
from constants import ProvidedCFGConfig

logger = settings.getLogger(__name__)


@dataclass
class SyntaxAnalyzer:
    """
    Syntax Analyzer class that can parse a given input
    string and determine if it is a valid expression based on
    the defined grammar.
    """
    index: int          = 0
    stack: deque        = None
    input_strings: List = field(default_factory=lambda: ProvidedCFGConfig.input_strings)

    rules: List         = field(default_factory=lambda: ProvidedCFGConfig.rules)
    parsing_table: Dict = field(default_factory=lambda: ProvidedCFGConfig.parsing_table)

    total_analyze_runtime: float = 0.0

    def __post_init__(self):
        if not self.stack:
            self.stack = deque(['$', self.rules[0]])

    def __reset(self):
        """
        Reset the index and stack.
        """
        logger.debug('Resetting index and stack.')

        self.index = 0
        self.stack = deque(['$', self.rules[0]])

    def __log_stack(self):
        logger.debug('Stack: %s', self.stack)
        print(f'Stack: {list(self.stack)}')

    def __update_runtime(self, _start: float):
        runtime = time.time() - _start

        logger.debug('Runtime: %s seconds', f'{runtime:.10f}')
        print(f'Input String Runtime: {runtime:.10f} seconds')

        self.total_analyze_runtime += runtime

    def parse(self, input_string: str) -> bool:
        """
        Parse the input string based on the defined grammar.
        """
        logger.debug('Input: %s', input_string)
        print(f'\nInput: {input_string}')

        while self.stack:
            _start = time.time()

            current_stack_symbol = self.stack[-1]
            current_input_symbol = input_string[self.index]

            if current_stack_symbol == current_input_symbol:
                self.stack.pop()
                self.index += 1

                if current_input_symbol == '$':
                    self.__update_runtime(_start=_start)
                    return True

            elif rule := self.parsing_table.get((current_stack_symbol, current_input_symbol)):
                self.stack.pop()

                if rule != 'ep.':
                    for symbol in reversed(rule):
                        self.stack.append(symbol)

            else:
                self.__update_runtime(_start=_start)
                return False

            self.__log_stack()

    def run(self, input_strings: Optional[List] = None):
        """
        Run the syntax analyzer using the provided input strings
        or the default ones.
        """
        self.total_analyze_runtime = 0.0

        # NOTE: This is a little redundant as one can just initialize
        # the class with a different set of input strings
        if input_strings:
            self.input_strings = input_strings

        for input_string in self.input_strings:
            result = self.parse(input_string)
            self.__reset()

            if result:
                logger.debug('Output: %s is accepted/valid.', input_string)
                print(f'Output: {input_string} is accepted/valid.')
            else:
                logger.debug('Output: %s is not accepted/invalid.', input_string)
                print(f'Output: {input_string} is not accepted/invalid.')

        logger.debug('Total analysis runtime: %s seconds', f'{self.total_analyze_runtime:.10f}')
        print(f'\nTotal Analysis Runtime: {self.total_analyze_runtime:.10f} milliseconds')
