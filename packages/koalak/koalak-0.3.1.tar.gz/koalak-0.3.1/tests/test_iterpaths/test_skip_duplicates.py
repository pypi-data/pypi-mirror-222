from pathlib import Path
from typing import List

import pytest
from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


def test_iter_paths_arg_no_duplicates(tmp_path):
    # Create some test files and directories
    paths = [
        "f1",
        "f2",
        "x",
        "dir1/f1",  # should be skipped
        "dir1/dir1/",  # should be skipped
        "dir1/x/",  # should be returned since
    ]
    expected = [
        "f1",
        "f2",
        "x",
        "dir1/",
        "dir1/x/",  # should be returned since
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, no_duplicates=True)))
    assert found_paths == expected


def test_iter_paths_arg_no_dir_duplicates(tmp_path):
    # Create some test files and directories
    paths = [
        "f1",
        "f2",
        "x",
        "dir1/f1",
        "dir1/dir1/",
        "dir1/x/",
    ]
    expected = [
        "f1",
        "f2",
        "x",
        "dir1/",
        "dir1/f1/",  # returned because we skip only dir duplicates
        "dir1/x/",  # should be returned since
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, no_dir_duplicates=True)))
    assert found_paths == expected


def test_iter_paths_arg_no_file_duplicates(tmp_path):
    # Create some test files and directories
    paths = [
        "f1",
        "f2",
        "x",
        "dir1/f1",  # removed
        "dir1/dir1/",
        "dir1/x/",
    ]
    expected = [
        "f1",
        "f2",
        "x",
        "dir1/",
        "dir1/dir1",
        "dir1/x/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, no_file_duplicates=True)))
    assert found_paths == expected


@pytest.mark.skip
def test_iter_paths_arg_trimdir_no_duplicates(tmp_path):
    # Create some test files and directories
    paths = [
        "f1",
        "f2",
        "x",
        "dir1/" "dir1/f1",
        "dir2/",
        "dir2/dir1",  # dir1 already found so dont iter through it but return it
        "dir1/dir1/f2",
    ]
    expected = [
        "f1",
        "f2",
        "x",
        "dir1/",
        "dir1/f1",
        "dir2/",
        "dir2/dir1/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, trimdir_skip_duplicates=True)))
    assert found_paths == expected
