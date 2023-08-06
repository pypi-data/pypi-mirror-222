import copy
from typing import Any, Dict, List

EntryAnnotation = Dict[str, Any]


class ListOfDict:
    def __init__(self, data, deepcopy: bool = None):
        if deepcopy is None:
            deepcopy = False
        if deepcopy:
            self.data = copy.deepcopy(data)
        else:
            self.data = data
        self._deepcopy = deepcopy

    def first(self, params: dict = None, **kwargs) -> EntryAnnotation:
        """
        Delete the first dictionary in the list that matches the filter criteria.

        Args:
            params: A dictionary containing the filter criteria for the dictionary to be deleted.
            **kwargs: The filter criteria for the dictionary to be deleted.

        Raises:
            ValueError: If both `params` and `**kwargs` are passed as arguments.
            ValueError: If no filter criteria is specified.
        """
        kwargs = self._normalize_params_and_kwargs(params, **kwargs)
        for d in self.data:
            if all(k in d and d[k] == v for k, v in kwargs.items()):
                return d
        raise ValueError("No matching dictionary found")

    def filter(self, params: dict = None, **kwargs) -> "ListOfDict":
        """
        Returns a list of dictionaries that match the filter criteria.

        Args:
            params (dict): A dictionary of filter criteria.
            **kwargs: Additional keyword arguments representing filter criteria.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries that match the filter criteria.
        """
        # TODO: why not returning a ListOfDict?
        kwargs = self._normalize_params_and_kwargs(params, **kwargs)
        result = []
        for d in self.data:
            if all(k in d and d[k] == v for k, v in kwargs.items()):
                result.append(d)
        return ListOfDict(result, deepcopy=self._deepcopy)

    def update(self, filter_query: dict, update_query: dict):
        for d in self.data:
            if all(k in d and d[k] == v for k, v in filter_query.items()):
                d.update(update_query)

    def delete(self, params: dict = None, **kwargs):
        kwargs = self._normalize_params_and_kwargs(params, **kwargs)
        if not kwargs:
            return []
        self.data = [
            d
            for d in self.data
            if not all(k in d and d[k] == v for k, v in kwargs.items())
        ]

    def delete_first(self, params: dict = None, **kwargs):
        """
        Delete the first dictionary in the list that matches the filter criteria.

        Args:
            params: A dictionary containing the filter criteria for the dictionary to be deleted.
            **kwargs: The filter criteria for the dictionary to be deleted.

        Raises:
            ValueError: If both `params` and `**kwargs` are passed as arguments.
            ValueError: If no filter criteria is specified.
        """

        kwargs = self._normalize_params_and_kwargs(params, **kwargs)

        for d in self.data:
            if all(k in d and d[k] == v for k, v in kwargs.items()):
                self.data.remove(d)
                break

    def update_first(self, filter_query: dict, update_query: dict):
        """
        Update the first item matching the filter query with the update query.

        Args:
            filter_query (dict): A dictionary containing key-value pairs that are used to filter the list of dictionaries.
            update_query (dict): A dictionary containing key-value pairs that will be used to update the first matching dictionary.

        Returns:
            None.
        """

        for d in self.data:
            if all(k in d and d[k] == v for k, v in filter_query.items()):
                d.update(update_query)
                return d

    def count(self, params: dict = None, **kwargs):
        kwargs = self._normalize_params_and_kwargs(params, **kwargs)
        if not kwargs:
            return len(self.data)
        return len(self.filter(**kwargs))

    def sum(self, key: str, params: dict = None, **kwargs):
        kwargs = self._normalize_params_and_kwargs(params, **kwargs)
        return sum(
            d[key]
            for d in self.data
            if all(k in d and d[k] == v for k, v in kwargs.items())
        )

    def sort(self, *keys, reverse=False):
        self.data.sort(key=lambda d: tuple(d[k] for k in keys), reverse=reverse)
        return self

    def sorted(self, *keys, reverse=False):
        data = sorted(
            self.data, key=lambda d: tuple(d[k] for k in keys), reverse=reverse
        )
        return ListOfDict(data)

    def group_by(self, *keys):
        result = {}
        for d in self.data:
            group_key = tuple(d[k] for k in keys)
            if group_key not in result:
                result[group_key] = []
            result[group_key].append(d)
        return result

    def merge(self, other):
        return ListOfDict(self.data + other.data)

    def unique(self):
        seen = set()
        result = []
        for d in self.data:
            d_tuple = tuple(sorted(d.items()))
            if d_tuple in seen:
                continue
            seen.add(d_tuple)
            result.append(d)
        return ListOfDict(result)

    def distinct(self, key):
        seen = set()
        results = []
        for e in self:
            if key not in e:
                continue
            ee = e[key]
            if isinstance(ee, list):
                ee = tuple(ee)
            if ee not in seen:
                results.append(ee)
                seen.add(ee)
        return results

    def show(self, fields):
        if not isinstance(fields, list):
            fields = [fields]

        data = []
        for e in self.data:
            entry = {}
            for field in fields:
                if field in e:
                    entry[field] = e[field]
            if entry:
                data.append(entry)
        return ListOfDict(data)

    def count_values(self, key):
        result = {}
        for d in self.data:
            value = d[key]
            if value not in result:
                result[value] = 0
            result[value] += 1
        return result

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        return self.data[index]

    def __iter__(self):
        return iter(self.data)

    def __eq__(self, other):
        if isinstance(other, ListOfDict):
            return self.data == other.data
        return False

    def __repr__(self):
        return f"ListOfDict({repr(self.data)})"

    def __str__(self):
        return str(self.data)

    def _normalize_params_and_kwargs(self, params, **kwargs):
        if params is not None and kwargs:
            raise ValueError("Cannot use both params and kwargs")
        if params is not None:
            kwargs = params
        return kwargs

    def print(self):
        for e in self:
            print(e)
