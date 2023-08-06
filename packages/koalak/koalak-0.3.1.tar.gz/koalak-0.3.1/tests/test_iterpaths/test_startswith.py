from pathlib import Path
from typing import List

import pytest
from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


def test_iter_paths_arg_startswith(tmp_path):
    # Create some test files and directories
    paths = [
        "_f1",
        "_f2",
        "dir1/",
        "dir1/_f1",
        "dir1/dir1/",
        "dir1/_dir2/",  # Return this, eve, of dir1 do not startswith '_'
        "_dir2/",
        "_dir3/_f3",
        "_dir3/f4",
    ]
    expected = [
        "_f1",
        "_f2",
        "dir1/_f1",
        "dir1/_dir2/",
        "_dir2",
        "_dir3",
        "_dir3/_f3",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, startswith="_")))
    assert found_paths == expected


def test_iter_paths_arg_startswith_multiple_string(tmp_path):
    # Create some test files and directories
    paths = [
        "_f1",
        "_f2",
        "dir1/",
        "_dir2/",
        "_dir3/_f3",
        "_dir3/f4",
        ".f5",
        "dir4/.f6",
    ]

    expected = [
        "_f1",
        "_f2",
        "_dir2",
        "_dir3",
        "_dir3/_f3",
        ".f5",
        "dir4/.f6",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, startswith=["_", "."])))

    assert found_paths == expected


def test_iter_paths_arg_dir_startswith(tmp_path):
    # Create some test files and directories
    paths = [
        "_f1",
        "_f2",
        "dir1/",
        "dir1/_f1",
        "dir1/dir1/",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3/_f3",
        "_dir3/f4",
    ]
    expected = [
        "_f1",
        "_f2",
        "dir1/_f1",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3",
        "_dir3/_f3",
        "_dir3/f4",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_startswith="_")))

    assert found_paths == expected


def test_iter_paths_arg_dir_startswith_multiple_string(tmp_path):
    # Create some test files and directories
    paths = [
        "_f1",
        "_f2",
        "f3.",
        "dir1/",
        "dir1/_f1",
        "dir1/dir1/",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3/_f3",
        "_dir3/f4",
        "dir4.",
    ]
    expected = [
        "_f1",
        "_f2",
        "f3.",
        "dir1/_f1",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3",
        "_dir3/_f3",
        "_dir3/f4",
        "dir4.",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, dir_startswith=["_", "."])))

    assert found_paths == expected


def test_iter_paths_arg_file_startswith(tmp_path):
    # Create some test files and directories
    paths = [
        "_f1",
        "_f2",
        "f3",
        "dir1/",
        "dir1/_f1",
        "dir1/f2",
        "dir1/dir1/",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3/_f3",
        "_dir3/f4",
    ]
    expected = [
        "_f1",
        "_f2",
        "dir1/",
        "dir1/_f1",
        "dir1/dir1/",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3",
        "_dir3/_f3",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_startswith="_")))
    assert found_paths == expected


def test_iter_paths_arg_file_startswith_multiple(tmp_path):
    # Create some test files and directories
    paths = [
        "_f1",
        "_f2",
        "f3",
        ".f4",
        "dir1/",
        "dir1/_f1",
        "dir1/f2",
        "dir1/dir1/",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3/_f3",
        "_dir3/f4",
    ]
    expected = [
        "_f1",
        "_f2",
        ".f4",
        "dir1/",
        "dir1/_f1",
        "dir1/dir1/",
        "dir1/_dir2/",
        "_dir2/",
        "_dir3",
        "_dir3/_f3",
    ]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, file_startswith=["_", "."])))
    assert found_paths == expected


@pytest.mark.skip
def test_iter_paths_arg_trimdir_startswith(tmp_path):
    # Create some test files and directories
    paths = ["f1", "_f2", "_dir1/", "_dir1/f3", "dir2/", "dir2/f1"]  # don't return it
    expected = ["f1", "_f2", "_dir1/", "dir2/", "dir2/f1"]
    expected = sorted([Path(tmp_path / e) for e in expected])
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = sorted(list(iterpaths(tmp_path, trimdir_startswith="_")))
    assert found_paths == expected
