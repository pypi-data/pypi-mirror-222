from pathlib import Path
from typing import List

from devtools import debug
from koalak.iterpaths import iterpaths

from .utils_test_iterpath import create_paths


def test_iter_paths_no_args_with_files_only_simple(tmp_path):
    # Create some test files and directories
    paths = ["file1.txt", "file2.txt"]
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = list(iterpaths(tmp_path))
    assert len(found_paths) == 2
    assert found_paths[0] == tmp_path / paths[0]
    assert found_paths[1] == tmp_path / paths[1]


def test_iter_paths_no_args_with_dirs_only_simple(tmp_path):
    # Create some test files and directories
    paths = ["dir1/", "dir2/"]
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = list(iterpaths(tmp_path))
    assert len(found_paths) == 2
    assert found_paths[0] == tmp_path / paths[0]
    assert found_paths[1] == tmp_path / paths[1]


def test_iter_paths_no_args_with_dirs_and_files_simple(tmp_path):
    # Create some test files and directories
    paths = ["f1", "f2", "f3.txt", "dir1/", "dir2/"]
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = list(iterpaths(tmp_path))
    assert len(found_paths) == 5
    for path in paths:
        assert tmp_path / path in found_paths


def test_iter_paths_no_args_with_dirs_and_files_recursive(tmp_path):
    # Create some test files and directories
    paths = ["f1", "f2", "f3.txt", "dir1/", "dir2/", "dir3/a", "dir3/b"]
    create_paths(tmp_path, paths)

    # Call iter_paths and check the results
    found_paths = list(iterpaths(tmp_path))
    assert len(found_paths) == 8
    for path in paths:
        assert tmp_path / path in found_paths
    assert tmp_path / "dir3" in found_paths
