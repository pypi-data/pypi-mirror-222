from pathlib import Path
from typing import List

from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


def test_iter_paths_arg_endswith(tmp_path):
    # Create some test files and directories
    paths = [
        "f1_",
        "f2_",
        "dir1/",
        "dir1/f1_",
        "dir1/dir1/",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_/f3_",
        "dir3_/f4",
    ]
    expected = [
        "f1_",
        "f2_",
        "dir1/f1_",
        "dir1/dir2_/",
        "dir2_",
        "dir3_",
        "dir3_/f3_",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, endswith="_")))
    assert found_paths == expected


def test_iter_paths_arg_endswith_multiple_string(tmp_path):
    # Create some test files and directories
    paths = [
        "f1_",
        "f2_",
        "f3.",
        "dir1/",
        "dir1/f1_",
        "dir1/dir1/",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_/f3_",
        "dir3_/f4",
        "dir4.",
        "dir5/f1.",
    ]

    expected = [
        "f1_",
        "f2_",
        "f3.",
        "dir1/f1_",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_",
        "dir3_/f3_",
        "dir4.",
        "dir5/f1.",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, endswith=["_", "."])))
    assert found_paths == expected


def test_iter_paths_arg_dir_endswith(tmp_path):
    # Create some test files and directories
    paths = [
        "f1_",
        "f2_",
        "dir1/",
        "dir1/f1_",
        "dir1/dir1/",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_/f3_",
        "dir3_/f4",
    ]
    expected = [
        "f1_",
        "f2_",
        "dir1/f1_",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_",
        "dir3_/f3_",
        "dir3_/f4",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_endswith="_")))
    assert found_paths == expected


def test_iter_paths_arg_file_endswith(tmp_path):
    # Create some test files and directories
    paths = [
        "f1_",
        "f2_",
        "f3",
        "dir1/",
        "dir1/f1_",
        "dir1/f2",
        "dir1/dir1/",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_/f3_",
        "dir3_/f4",
    ]
    expected = [
        "f1_",
        "f2_",
        "dir1/",
        "dir1/f1_",
        "dir1/dir1/",
        "dir1/dir2_/",
        "dir2_/",
        "dir3_",
        "dir3_/f3_",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_endswith="_")))
    assert found_paths == expected
