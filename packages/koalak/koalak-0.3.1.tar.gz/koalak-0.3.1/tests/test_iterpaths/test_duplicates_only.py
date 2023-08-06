from pathlib import Path
from typing import List

from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


def test_iter_paths_arg_duplicates(tmp_path):
    # Create some test files and directories
    paths = [
        "f1",
        "f2",
        "x",
        "dir1/f1",  # should be skipped
        "dir1/dir1/",  # should be skipped
        "dir1/x/",  # should be returned since folders and files are different
    ]
    expected = [
        "dir1/f1",
        "dir1/dir1",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, duplicates=True)))
    assert found_paths == expected


def test_iter_paths_arg_dir_duplicates(tmp_path):
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
        "dir1/f1/",
        "dir1/dir1/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_duplicates=True)))
    assert found_paths == expected


def test_iter_paths_arg_file_duplicates(tmp_path):
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
        "dir1/f1",
        "dir1/",
        "dir1/dir1/",
        "dir1/x/",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_duplicates=True)))
    assert found_paths == expected
