import os
import ast

import pytest
from flake8.options.manager import OptionManager

from flake8_fine_pytest.checker import FinePytestChecker


def parse_options(allowed_test_directories, allowed_test_arguments_count, allowed_assert_count):
    options = OptionManager()

    options.allowed_test_directories = allowed_test_directories
    options.allowed_test_arguments_count = allowed_test_arguments_count
    options.allowed_assert_count = allowed_assert_count

    FinePytestChecker.parse_options(options)


@pytest.fixture
def run_validator_for_test_files():
    def _run(filename, allowed_test_directories=None, allowed_test_arguments_count=None, allowed_assert_count=None):
        test_file_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            'test_files',
            filename,
        )

        with open(test_file_path, 'r') as file_handler:
            raw_content = file_handler.read()

        tree = ast.parse(raw_content)
        checker = FinePytestChecker(tree=tree, filename=test_file_path)

        parse_options(allowed_test_directories, allowed_test_arguments_count, allowed_assert_count)

        return list(checker.run())

    return _run
