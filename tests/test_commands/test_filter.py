from __future__ import annotations

from io import StringIO

from mypy_baseline import main

from .helpers import LINE1, LINE2, LINE3, NOTEBOOK_LINE1, run


def test_filter():
    stdin = StringIO()
    stdin.write(LINE1)
    stdin.write(LINE2)
    stdin.write(LINE3)
    stdin.seek(0)
    stdout = StringIO()
    code = main(['filter'], stdin, stdout)
    assert code == 3
    stdout.seek(0)
    actual = stdout.read()
    assert LINE1.strip() in actual
    assert LINE2.strip() in actual
    assert LINE3.strip() in actual
    assert '  assignment  ' in actual
    assert '  union-attr  ' in actual
    assert '  unresolved' in actual
    assert 'Your changes introduced' in actual


def test_filter_notebook():
    stdin = StringIO()
    stdin.write(NOTEBOOK_LINE1)

    stdin.seek(0)
    stdout = StringIO()
    code = main(['filter'], stdin, stdout)
    assert code == 1
    stdout.seek(0)
    actual = stdout.read()
    assert NOTEBOOK_LINE1 in actual
    assert '  return-value  ' in actual
    assert '  unresolved' in actual
    assert 'Your changes introduced' in actual


def test_filter__empty_stdin():
    actual = run(['filter'])
    assert actual == ''
