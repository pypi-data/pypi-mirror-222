import abc
import os
import pathlib
import re
from pathlib import Path
from typing import Any, Dict, Iterator, List, Tuple, Union

from devtools import debug
from koalak.utils import merge_intervals, str_find_all

STR_OR_PATH = Union[str, Path]
MultiPathAnnotation = Union[None, STR_OR_PATH, List[STR_OR_PATH]]

"""
module to handle iter_path function.
2 basic filters:
- NameFilter: act on the current name of the path (file or dir) without the parent directory
    examples: name startswith, endswith, ...
- PathFilter: act on the full path [TODO]
    examples: extension, size, modify time, ...

"""
# =============== #
# UTILS FUNCTIONS #
# =============== #
DETAILS_KEY_POSITIONS = "positions"


def _normalize_str_or_list_of_str(obj):
    if isinstance(obj, (str, pathlib.Path)):
        return [obj]
    elif obj is None:
        return []
    return obj


# ======= #
# FILTERS #
# ======= #


# Base filters #
# ------------ #
class BasePathFilter(abc.ABC):
    """Base class to filter on the full path"""

    @abc.abstractmethod
    def filter(self, path: Path) -> bool:
        """Main function to filter"""
        pass

    def _get_ext(self, path: Path):
        suffix = path.suffix
        if suffix:
            return suffix[1:]
        return None


class BaseNameFilter(abc.ABC):
    """Base filter to act on the name of the file or directory without the full path
    Examle: dir1/dir2/filename  will act only on "dir1" or "dir2" or "filename" separatly
    """

    subclasses = {}

    def __init__(self, keywords, *, insensitive=None):
        """
        Args:
            insensitive(bool): if insensitive is True, the core function will handle it
            meaning that we don't have to lowercase the name in the filter() function
        """
        if insensitive is None:
            insensitive = False

        keywords = _normalize_str_or_list_of_str(keywords)

        self.keywords = keywords
        self.insensitive = insensitive
        self.negative = False

        if self.insensitive:
            self.keywords = [e.lower() for e in self.keywords]

    @abc.abstractmethod
    def filter_with_details(
        self, name: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        """Main function to filter"""
        pass

    def filter(self, name: str) -> bool:
        return self.filter_with_details(name)[0]

    def nofilter(self, name: str) -> bool:
        return self.nofilter_with_details(name)[0]

    def nofilter_with_details(
        self, name: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        found, details = self.filter_with_details(name, details=details)
        found = not found
        return found, details

    def __init_subclass__(cls, **kwargs):
        if cls.name in BaseNameFilter.subclasses:
            raise ValueError(f"Subclass with name {cls.name} already exists")
        BaseNameFilter.subclasses[cls.name] = cls

    def __str__(self):
        args = ""
        if self.insensitive:
            args += "i"
        if self.negative:
            args += "n"
        if args:
            args += ", "
        return f"{self.__class__.__name__}({args}{self.keywords!r})"

        # TODO: implement me!


# Filters on name #
# --------------- #
class StartswithNameFilter(BaseNameFilter):
    """Allow only files with specific extensions"""

    name = "startswith"

    def filter_with_details(
        self, path: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        if details is None:
            return any(path.startswith(e) for e in self.keywords), {}
        else:
            positions = []
            for keyword in self.keywords:
                if path.startswith(keyword):
                    positions.append((0, len(keyword)))
            if positions:
                return True, {DETAILS_KEY_POSITIONS: positions}
            else:
                return False, {}


class EndswithNameFilter(BaseNameFilter):
    name = "endswith"

    def filter_with_details(
        self, path: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        if details is None:
            return any(path.endswith(e) for e in self.keywords), {}
        else:
            positions = []
            for keyword in self.keywords:
                if path.endswith(keyword):
                    positions.append((len(path) - len(keyword), len(path)))
            if positions:
                return True, {DETAILS_KEY_POSITIONS: positions}
            else:
                return False, {}


class DuplicatesNamesFilter(BaseNameFilter):
    """Allow only duplicate filename (without the directory)"""

    name = "duplicates"

    def __init__(self, _dummy_arg=None, *, insensitive=None):
        super().__init__([], insensitive=insensitive)
        self._seen_files = set()

    def filter_with_details(
        self, path: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        if path not in self._seen_files:
            self._seen_files.add(path)
            return False, {}
        return True, {}


class SearchNameFilter(BaseNameFilter):
    """Allow only once each different filename (without the directory)"""

    name = "search"

    def filter_with_details(
        self, path: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        if details is None:
            return all(search in path for search in self.keywords), {}
        else:
            positions = []
            details = {DETAILS_KEY_POSITIONS: positions}
            for keyword in self.keywords:
                new_positions = str_find_all(path, keyword, return_position=True)
                if not new_positions:
                    return False, details
                positions.extend(new_positions)
            return True, details


class RegexNameFilter(BaseNameFilter):
    """Allow only once each different filename (without the directory)"""

    name = "regex"

    def __init__(self, keywords, *, insensitive=None):
        super().__init__(keywords, insensitive=insensitive)
        if self.insensitive:
            flags = re.IGNORECASE
        else:
            flags = 0
        self.keywords = [re.compile(e, flags=flags) for e in self.keywords]

    def filter_with_details(
        self, path: str, details=None
    ) -> Tuple[bool, Dict[str, Any]]:
        if details is None:
            return all(regex.search(path) for regex in self.keywords), {}
        else:
            positions = []
            details = {DETAILS_KEY_POSITIONS: positions}
            for regex in self.keywords:
                new_positions = []
                for match in regex.finditer(path):
                    new_positions.append(match.span())
                if not new_positions:
                    return False, details
                positions.extend(new_positions)
            return True, details


# Filters on paths
# ----------------
class ExtensionsPathFilter(BasePathFilter):
    """Allow only files with specific extensions"""

    def __init__(self, extensions):
        self.extensions = _normalize_str_or_list_of_str(extensions)

    def filter(self, path: Path, details=None) -> bool:
        return self._get_ext(path) in self.extensions


def _iter_paths(
    original_paths: List[STR_OR_PATH],
    *,
    filters_on_name_trim_dirs: List[BaseNameFilter],
    filters_on_name_dirs: List[BaseNameFilter],
    filters_on_name_files: List[BaseNameFilter],
    return_details: bool = None,
) -> Iterator[Path]:
    """Iter through files or directories Return dir, file, ext"""

    def _update_details(details, new_details):
        # Handle positions
        positions_details = details.get(DETAILS_KEY_POSITIONS, [])
        new_positions = new_details.get(DETAILS_KEY_POSITIONS, [])
        positions_details.extend(new_positions)
        details[DETAILS_KEY_POSITIONS] = positions_details

    def _normalize_details(details, rootfile):
        # Normalize positions: update the indexes relative to the full path
        if DETAILS_KEY_POSITIONS in details:
            positions = details[DETAILS_KEY_POSITIONS]
            positions = merge_intervals(positions)
            adding_position = len(str(rootfile)) + 1  # + 1 because of "/" at the end
            positions = [
                (e[0] + adding_position, e[1] + adding_position) for e in positions
            ]
            details[DETAILS_KEY_POSITIONS] = positions

    # Check if we have at least one filter with 'insensitive' == True
    #  to know if we have to lowercase the matched line
    at_least_one_insensitive_filter_name_file = any(
        filter.insensitive for filter in filters_on_name_files
    )
    at_least_one_insensitive_filter_name_dirs = any(
        filter.insensitive for filter in filters_on_name_dirs
    )

    # TODO: add onerror for os.walk
    for original_path in original_paths:
        for root, dirs, files in os.walk(original_path):
            root_as_path = Path(root)

            # Make the same treatment for files and directories
            for name_filters, nodes, at_least_one_insensitive_filter_name_nodes in [
                (
                    filters_on_name_files,
                    files,
                    at_least_one_insensitive_filter_name_file,
                ),
                (filters_on_name_dirs, dirs, at_least_one_insensitive_filter_name_dirs),
            ]:
                for node in nodes:
                    # analyse_node is the node (file or dir) to pass to the filter function
                    # the 'analyse_node' can be changed to lowercase if the filter is insensitive
                    # we use different variable then node to keep the original node
                    analyse_node = node
                    node_details = {}

                    # we pre-compute lowercase only if it's necessary
                    if at_least_one_insensitive_filter_name_nodes:
                        lowercase_node = node.lower()

                    # Keep trace of matching creteria in a boolean to skip the current iteration
                    node_matching_criteria = True

                    for filter_instance in name_filters:
                        # Get the right case to analyse
                        if filter_instance.insensitive:
                            analyse_node = lowercase_node

                        # Get the right function (filter or nofilter)
                        if filter_instance.negative:
                            filter_function = filter_instance.nofilter_with_details
                        else:
                            filter_function = filter_instance.filter_with_details

                        found, new_details = filter_function(
                            analyse_node, details=return_details
                        )

                        if not found:
                            node_matching_criteria = False
                            continue

                        if return_details:
                            _update_details(node_details, new_details)

                    if not node_matching_criteria:
                        continue

                    # Compute the path to yield
                    node_path = root_as_path / node
                    if return_details:
                        _normalize_details(node_details, root_as_path)
                        yield node_path, node_details
                    else:
                        yield node_path

            # TODO: continue trim options (to skip nodes while iterating)
            # Trim dirs
            dirs[:] = [
                d
                for d in dirs
                if all(
                    filter_instance.filter_with_details(d)
                    for filter_instance in filters_on_name_trim_dirs
                )
            ]


def iterpaths(
    rootpaths: MultiPathAnnotation = None,
    details=None,
    **kwargs,
) -> Iterator[Path]:
    """
    Recursively iter through one or more directories with filtering.

    Filters availables:
        search(str or List[str]): search by keywords, if many keywords, all keywords must match
        regex
        duplicates
        startswith
        endswith

    Args:
        rootpaths:
        details: if True, return associated details with each Path (indexes of matches, size, ...)
        kwargs: dictionaries of filters can be in the form of
            <filter_name>: to apply the filter for files and directories
            file_<filter_name>: to apply the filter for files only
            dir_<filter_name>: to apply the filter for dirs only
            i<filter_name>: apply the filter in insensitive mode
            no_<filter_name>: apply the negation of the filter (return only none matching)

    Example:
        iter_path(
            ['dir1', 'dir3],
            search="keyword",
            isearch=['key1', 'key2'],
            dir_regex=r"alpha|beta",
            no_dir_istartswith="_",
        )
    """
    # Local variables
    filters_on_name_dirs: List[BaseNameFilter] = []
    filters_on_name_files: List[BaseNameFilter] = []
    filters_on_name_trim_dirs: List[BaseNameFilter] = []

    for kwarg_name, kwarg_value in kwargs.items():
        if kwarg_value is None:
            continue
        # Possible values
        # --search
        # --isearch
        # --no-search
        # --no-isearch
        # --dir-search
        # --no-dir-isearch  or --dir-no-isearch

        # Handle negation first
        if kwarg_name.startswith("no_"):
            kwarg_name = kwarg_name[len("no_") :]
            negative = True
        else:
            negative = False

        # Handle type
        if kwarg_name.startswith("dir_"):
            filter_name = kwarg_name[len("dir_") :]
            add_to_filters = [filters_on_name_dirs]
        elif kwarg_name.startswith("file_"):
            filter_name = kwarg_name[len("file_") :]
            add_to_filters = [filters_on_name_files]
        elif kwarg_name.startswith("trimdir_"):
            filter_name = kwarg_name[len("trimdir_") :]
            add_to_filters = [filters_on_name_trim_dirs]
        else:
            filter_name = kwarg_name
            add_to_filters = [filters_on_name_dirs, filters_on_name_files]

        # Handle insensitivity
        if filter_name.startswith("i"):
            filter_name = filter_name[1:]
            insensitive = True
        else:
            insensitive = False

        # Add the filters
        filter_cls = BaseNameFilter.subclasses[filter_name]
        for current_filters in add_to_filters:
            filter_instance = filter_cls(kwarg_value, insensitive=insensitive)
            filter_instance.negative = negative
            current_filters.append(filter_instance)

    if rootpaths is None:
        rootpaths = "."
    rootpaths = _normalize_str_or_list_of_str(rootpaths)

    # Core logic
    yield from _iter_paths(
        rootpaths,
        return_details=details,
        filters_on_name_trim_dirs=filters_on_name_trim_dirs,
        filters_on_name_dirs=filters_on_name_dirs,
        filters_on_name_files=filters_on_name_files,
    )


iterpaths.BaseNameFilter = BaseNameFilter
