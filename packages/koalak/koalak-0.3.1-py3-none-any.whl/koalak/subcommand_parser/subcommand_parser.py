import argparse
import inspect
import sys
from typing import Any, Dict, Union

import argcomplete
import attrs
from devtools import debug

# import rich
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

# RICH STYLE CONSTS
STYLE_USAGE = "yellow bold"
# table
STYLE_OPTIONS_TABLE_SHOW_LINES = False
STYLE_OPTIONS_TABLE_LEADING = 0
STYLE_OPTIONS_TABLE_PAD_EDGE = False
STYLE_OPTIONS_TABLE_PADDING = (0, 1)
STYLE_OPTIONS_TABLE_BOX = ""
STYLE_OPTIONS_TABLE_ROW_STYLES = None
STYLE_OPTIONS_TABLE_BORDER_STYLE = None

STYLE_ARGUMENTS_NAME = "bold cyan"
STYLE_OPTIONS_TYPE = "yellow bold"

UNGROUPED_NAME = "_ungrouped"
UNGROUPED_TITLE_WHEN_MANY_GROUP = "Other commands"
UNGROUPED_TITLE_WHEN_ONE_GROUP = "Commands"

types_to_text = {
    int: "INTEGER",
    str: "TEXT",
    bool: "",
}


console = Console()


@attrs.define
class Argument:
    dest: str = attrs.field()
    help: str = attrs.field()
    required: bool = attrs.field()
    name = attrs.field()
    is_option: bool = attrs.field()
    type = attrs.field()
    default = attrs.field()
    args_as_list = attrs.field()


@attrs.define
class ArgsGroup:
    title: str = attrs.field()
    description = attrs.field(kw_only=True, default=None)
    elements = attrs.field(kw_only=True, factory=list)

    # elements 3 types: positional args, optional args and subcommand
    def add_element(self, element):
        self.elements.append(element)

    def print(self):
        rich_table = self._get_rich_table()
        for element in self.elements:
            self._add_row(rich_table, element)

        if self.description:
            description = self.description + "\n"
            rich_group = Group(description, rich_table)
        else:
            rich_group = rich_table

        group_panel = Panel(
            rich_group, title=self.title, border_style="dim", title_align="left"
        )
        console.print(group_panel)

    def _add_row(self, table, row):
        if isinstance(row, Argument):
            self._add_row_argument(table, row)
        elif isinstance(row, SubcommandParser):
            self._add_row_subcommands(table, row)
        else:
            raise ValueError(f"unhandled type {type(row)}")

    def _add_row_argument(self, table, argument: Argument):
        # Get name column
        styled_name = Text(argument.name, style=STYLE_ARGUMENTS_NAME)

        # Get type column
        type_str = types_to_text.get(argument.type, "TEXT")
        if argument.args_as_list:
            type_str = f"List[{type_str}]"
        styled_type = Text(type_str, style=STYLE_OPTIONS_TYPE)

        # Get help column
        if argument.help is not None:
            help_str = Text(argument.help)
        else:
            help_str = Text()
        if argument.default is not None:
            help_str += Text(f" [default: {argument.default}]", style="dim")
        help_str.plain = help_str.plain.strip()

        table.add_row(styled_name, styled_type, help_str)

    def _add_row_subcommands(self, table, subcommand: "SubcommandParser"):
        cmd_name = Text(subcommand.name, style=STYLE_ARGUMENTS_NAME)
        table.add_row(cmd_name, subcommand.description)

    def _get_rich_table(self):
        t_styles: Dict[str, Any] = {
            "show_lines": STYLE_OPTIONS_TABLE_SHOW_LINES,
            "leading": STYLE_OPTIONS_TABLE_LEADING,
            "box": STYLE_OPTIONS_TABLE_BOX,
            "border_style": STYLE_OPTIONS_TABLE_BORDER_STYLE,
            "row_styles": STYLE_OPTIONS_TABLE_ROW_STYLES,
            "pad_edge": STYLE_OPTIONS_TABLE_PAD_EDGE,
            "padding": STYLE_OPTIONS_TABLE_PADDING,
        }
        return Table(
            highlight=True,
            show_header=False,
            expand=True,
            **t_styles,
        )


def argparse_argument_to_subcommand_argument(argparse_action):
    dest = argparse_action.dest
    help = argparse_action.help
    if argparse_action.option_strings == []:
        required = True
        name = dest
        is_option = False
    else:
        required = False
        name = " ".join(argparse_action.option_strings)
        is_option = True

    if argparse_action.type is None:
        type = str
    else:
        type = argparse_action.type

    if isinstance(argparse_action, argparse._StoreTrueAction):
        default = False
        type = bool
    elif isinstance(argparse_action, argparse._StoreFalseAction):
        type = bool
        default = True
    else:
        default = argparse_action.default

    if default == "==SUPPRESS==":
        default = None

    if argparse_action.nargs in ["*", "+"]:
        args_as_list = True
    else:
        args_as_list = False
    return Argument(
        dest=dest,
        help=help,
        required=required,
        name=name,
        is_option=is_option,
        type=type,
        default=default,
        args_as_list=args_as_list,
    )


class SubcommandParser:
    def __init__(
        self,
        prog=None,
        *,
        parent=None,
        parser=None,
        autocomplete: bool = None,
        # Help
        prolog=None,
        description=None,
        epilog=None,
    ):
        """

        Args:
            prog: name of the program
            parent: parent parser
            parser: argparse.ArgParser to use
            description: description of the program
            autocomplete: E,able autocomplete

        Advantages over argparse:
            - use add_subcommand instead of using add_parsers then add_subparser
            - run command that will run directly the program
            - better help with groups/colors
            - ease of use autocomplete
        """

        from rich.traceback import install

        install(show_locals=True)
        # FIXME: if parser is given don't take prolog/epilog
        if prog is None:
            prog = sys.argv[0]

        if autocomplete is None:
            autocomplete = False

        self.parent = parent
        self.name = prog or sys.argv[0]
        self.subcommands: Dict[str, SubcommandParser] = {}
        self.function = None  # function to run
        self._argparse_subparsers = None

        # Help related attributes
        self.groups: Dict[str, ArgsGroup] = {}
        self._i_group_name = 0
        self._group_commands_arguments = self.add_group(title="Commands Arguments")
        self._group_positional_arguments = self.add_group(title="Positional Arguments")
        self._group_optional_arguments = self.add_group(title="Optional Arguments")

        self.description = description
        self.prolog = prolog
        self.epilog = epilog
        self.hide = False
        self.autocomplete = autocomplete
        # FIXME: _group_namespace usage
        self._group_namespace = (
            set()
        )  # track groupnamespace for subcommands and help_subcommands

        if self.parent is None:
            self.fullname = self.name
        else:
            self.fullname = f"{self.parent.fullname}.{self.name}"

        if parser is None:
            parser = argparse.ArgumentParser(
                prog=prog, description=description, epilog=epilog
            )

        self._argparse_parser = parser
        self._subcommand_depth = 1

        self._argparse_parser.print_help = self.print_help

    def add_argument(
        self, *args, group: Union[str, ArgsGroup] = None, hide=None, **kwargs
    ):
        """Same as add_argument with hide in"""
        if hide is None:
            hide = False

        argparse_arg = self._argparse_parser.add_argument(*args, **kwargs)

        if not hide:
            arg = argparse_argument_to_subcommand_argument(argparse_arg)
            if isinstance(group, str):
                group = self.groups[group]
            elif group is None:
                if arg.is_option:
                    group = self._group_optional_arguments
                else:
                    group = self._group_positional_arguments

            group.add_element(arg)

    def add_group(self, name=None, *, title: str = None, description: str = None):
        if name is None:
            name = f"_random_group_koalak_{self._i_group_name}"
            self._i_group_name += 1

        if name in self.groups:
            raise KeyError(f"Group {name} already exists")

        if title is None:
            title = name

        if description is None:
            description = ""

        group = ArgsGroup(title=title, description=description)
        self.groups[name] = group
        return group

    def add_subcommand(self, command_name, description=None, group=None, hide=None):
        if hide is None:
            hide = False

        if command_name in self.subcommands:
            raise KeyError(f"command {command_name!r} already exists")

        # TODO: check that help_command is not existing in the same grp
        #  refactor this! we should check all namespace not only the one for grp
        # TODO: test me

        if self._argparse_subparsers is None:
            self._argparse_subparsers = self._argparse_parser.add_subparsers(
                dest=self._get_subcommand_dest_name()
            )

        subcommand_parser = self._argparse_subparsers.add_parser(command_name)

        subcommand_command = SubcommandParser(
            command_name,
            parser=subcommand_parser,
            parent=self,
            description=description,
        )
        # Add it to group

        subcommand_command._subcommand_depth += self._subcommand_depth

        if not hide:
            if isinstance(group, str):
                group = self.groups[group]
            elif group is None:
                group = self._group_commands_arguments
            group.add_element(subcommand_command)
        # Add it to subcommands
        self.subcommands[command_name] = subcommand_command
        return subcommand_command

    def add_help_subcommand(self, command_name, description=None, group=None):
        """Only add this command in the help

        Explanation:
            this could be useful if you have a lot of commands that are hidden
            and you want to add one help description to group all these commands
        """
        # FIXME
        if group is None:
            group = UNGROUPED_NAME

        if command_name in self.subcommands:
            raise KeyError(f"command {command_name!r} already exists")

        if command_name in self._group_namespace:
            raise KeyError(
                f"command {command_name!r} already exists in help_subcommands"
            )

        self.groups[group]["commands"][command_name] = {"description": description}
        self._group_namespace.add(command_name)

    def __getitem__(self, item: str):
        return self.subcommands[item]

    def __str__(self):
        return f"<SubcommandParser({self.fullname!r})>"

    def __repr__(self):
        return self.__str__()

    def parse_args(self, args=None, namespace=None):
        self.check_errors()

        if self.autocomplete:
            argcomplete.autocomplete(self._argparse_parser)

        return self._argparse_parser.parse_args(args, namespace=namespace)

    def run(self, args=None):
        """Run the main program"""

        # Parse arguments
        parsed_args = self.parse_args(args)
        # TODO: hook main: self._run_main(parsed_args)  # hook to _run_main

        # Check if there is any subcommand
        if not self.subcommands:
            if self.function:
                self.function(parsed_args)
                return
            else:
                self.print_help()
                sys.exit(1)

        # get called subcommand
        depth = 1
        subcommand = self
        while True:
            try:
                cmd_name = self._get_subcommand_name(parsed_args, depth=depth)

                if cmd_name is None:
                    self.print_help()
                    sys.exit(1)
                subcommand = subcommand[cmd_name]
                depth += 1
            except AttributeError:
                break

        # If function is None, automatically it (doesn't have subparsers
        #  because we already checked errors on parse_args
        if subcommand.function is None:
            self.print_help()
            sys.exit(0)

        subcommand.function(parsed_args)

    def _get_rich_table(self):
        t_styles: Dict[str, Any] = {
            "show_lines": STYLE_OPTIONS_TABLE_SHOW_LINES,
            "leading": STYLE_OPTIONS_TABLE_LEADING,
            "box": STYLE_OPTIONS_TABLE_BOX,
            "border_style": STYLE_OPTIONS_TABLE_BORDER_STYLE,
            "row_styles": STYLE_OPTIONS_TABLE_ROW_STYLES,
            "pad_edge": STYLE_OPTIONS_TABLE_PAD_EDGE,
            "padding": STYLE_OPTIONS_TABLE_PADDING,
        }
        return Table(
            highlight=True,
            show_header=False,
            expand=True,
            **t_styles,
        )

    def print_help(self, file=None):
        """Print the help menu with better coloring"""
        # print the following
        # - prolog
        # - usage
        # - description
        # - Groups of arguments (subcommand,s positional args, optional args)

        # FIXME: test/me

        # header prog name and description
        prog = self.name

        # Print prolog
        # ------------
        if self.prolog:
            console.print(self.prolog)

        # Print usage
        # -----------
        console.print(f"[{STYLE_USAGE}]Usage:[/{STYLE_USAGE}] {prog} [-h] <subcommand>")
        console.print()
        # Print description
        # -----------------
        if self.description:
            console.print(f"{self.description}")
            console.print()

        # Print all groups
        # ----------------
        for group in self.groups.values():
            if not group.elements:
                continue
            group.print()

        # Print epilog
        # ------------
        if self.epilog:
            console.print(self.epilog)

    def __call__(self, function):
        self._add_function(function)
        return function

    def _add_function(self, function):
        parameters = inspect.signature(function).parameters
        if len(parameters) != 1:
            raise ValueError(
                f"The added function {function} must have one unique parameter not {len(parameters)} parameters"
            )
        self.function = function

    def iter_allcommands(self):
        """Iter all commands, self included"""
        yield self
        for parser in self.subcommands.values():
            yield from parser.iter_allcommands()

    def check_errors(self):
        """Check if subcommands are correctly built
        This method is called before parse_args/run
        """
        for command in self.iter_allcommands():
            # If function exists it must be callable
            if command.function is not None and not callable(command.function):
                raise TypeError(f"{command.fullname}.function must be callable")

            # Todo: check that function has only one argument

            # If the command don't have any subcommand, it must have a function
            if not command.subcommands and command.function is None:
                raise ValueError(
                    f"Subcommand {command} don't have linked function or should have subpcommands"
                )

    # Private methods #
    # =============== #
    def _get_subcommand_dest_name(self, depth: int = None):
        if depth is None:
            depth = self._subcommand_depth
        if depth == 1:
            return "subcommand"
        else:
            return f"subcommand_{depth}"

    def _get_subcommand_name(self, parsed_args, depth: int = None):
        argparse_cmd_name = self._get_subcommand_dest_name(depth)
        return getattr(parsed_args, argparse_cmd_name)

    def _print_and_exist(self, msg, status=1):
        print(msg)
        sys.exit(status)
