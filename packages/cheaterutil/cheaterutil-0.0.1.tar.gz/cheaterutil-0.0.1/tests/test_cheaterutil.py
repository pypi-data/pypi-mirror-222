#!/usr/bin/env python

"""Tests for `cheaterutil` package."""

import pytest

from click.testing import CliRunner

from cheaterutil import cbutil
from cheaterutil import cli
from colorama import Style, Fore

logger = cbutil.Logger("Test", Fore.CYAN, Style.BRIGHT)

def test_content():

    logger.log("This is an message")
    logger.log_color( message="This is an message", color=Fore.BLUE)
    logger.log_color_style(message="This is an message", color=Fore.BLUE, style=Style.DIM)


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 'cheaterutil.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output


test_content()