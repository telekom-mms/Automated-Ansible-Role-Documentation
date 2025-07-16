"""
Defaults module for aar_doc.

This module provides utilities for collecting the default values
of an argument_spec and writing the final defaults file.
"""

from dataclasses import dataclass, field
from os import linesep
from pathlib import Path
from typing import Any, Union

from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.scalarstring import LiteralScalarString, SingleQuotedScalarString

from aar_doc.core import DescriptionTags


def represent_none(self, _):
    """Represents None as 'null' in YAML."""
    return self.represent_scalar("tag:yaml.org,2002:null", "null")


yaml = YAML()
yaml.indent(mapping=2, sequence=4, offset=2)
yaml.representer.add_representer(type(None), represent_none)
yaml.encoding = "utf-8"
yaml.allow_unicode = True


@dataclass
class RoleDefault:
    """
    Class that represents a role default.
    """

    name: str
    value: Any
    description: Union[str, list[str]]
    depth: int


@dataclass
class RoleDefaultsManager:
    """Class for managing all the role defaults of a role.

    Args:
        _overwrite (bool): Whether a default should be overwritten,
        if it's already known. Defaults to False.
    """

    _defaults: dict[str, RoleDefault] = field(default_factory=lambda: {}, init=False)
    _overwrite: bool = False

    @property
    def defaults(self) -> list[RoleDefault]:
        """Get the list of tracked defaults.

        Returns:
            list[RoleDefault]: List of role defaults.
        """
        return list(self._defaults.values())

    def add_default(
        self,
        name: str,
        value: Any,
        description: Union[str, list],
        depth=0,
    ) -> None:
        """Add a default.

        Args:
            name (str): Variable name of the default.
            value (Any): Value of the default.
            description (str, optional): Description of the default.
        """
        if isinstance(value, str):
            value = value.strip()

        if self._overwrite:
            self._defaults[name] = RoleDefault(name, value, description, depth)
        else:
            self._defaults.setdefault(name, RoleDefault(name, value, description, depth))

    def safe_quote_recursive(self, value):
        if isinstance(value, list):
            return [self.safe_quote_recursive(v) for v in value]
        elif isinstance(value, dict):
            for k, v in value.items():
                value[k] = self.safe_quote_recursive(v)
                return value
        elif isinstance(value, str):
            if value in ("yes", "no"):
                return SingleQuotedScalarString(value)
            elif "\n" in value:
                return LiteralScalarString(value)
            elif ":" in value:
                return SingleQuotedScalarString(value)
        return value

    def to_commented_map(self) -> CommentedMap:
        """
        Returns all tracked defaults as a CommentedMap.
        """
        commented_defaults = CommentedMap()
        for role_default in self.defaults:
            value = self.safe_quote_recursive(role_default.value)
            commented_defaults[role_default.name] = value
            description_items = (
                role_default.description if isinstance(role_default.description, list) else [role_default.description]
            )

            for description_item in description_items:
                commented_defaults.yaml_set_comment_before_after_key(
                    key=role_default.name,
                    before=description_item,
                    indent=2 * role_default.depth,
                )

        return commented_defaults


def walk_options(options, overwrite_duplicate_defaults, depth=-1) -> RoleDefaultsManager:
    defaults_manager = RoleDefaultsManager(overwrite_duplicate_defaults)
    depth += 1

    for name, spec in options.items():
        # Handle special case for vars that are intended to have prefix.
        if spec.get("description"):
            tags = DescriptionTags(spec.get("description"))
            if tags.defaults_prefix != "":
                spec["description"] = tags.replace()
                name = tags.defaults_prefix + name

        if spec.get("options"):
            value = walk_options(spec.get("options"), overwrite_duplicate_defaults, depth).to_commented_map()
        elif "default" in spec.keys():
            value = spec.get("default")
        else:
            continue

        defaults_manager.add_default(
            name,
            value,
            spec.get("description"),
            depth,
        )

    return defaults_manager


def generate_commented_defaults(
    argument_spec_data: dict,
    overwrite_duplicate_defaults: bool,
) -> CommentedMap:
    """Generates the initial RoleDefaults"""
    defaults_manager = RoleDefaultsManager(overwrite_duplicate_defaults)
    for entry_point in argument_spec_data:
        options: dict[str, Any] = argument_spec_data.get(entry_point, {}).get("options")
        if not options:
            continue

        for i in walk_options(options, overwrite_duplicate_defaults).defaults:
            defaults_manager.add_default(
                name=i.name,
                value=i.value,
                description=i.description,
                depth=i.depth,
            )

    return defaults_manager.to_commented_map()


def write_defaults(
    output_file_path: Path,
    role_path: Path,
    role_defaults: CommentedMap,
) -> None:
    """
    Writes the generated defaults CommentedMap to the given file.
    """
    if output_file_path.name == "README.md":
        output: Path = role_path / "defaults" / "main.yml"
    elif output_file_path.is_absolute():
        output = output_file_path
    else:
        output = role_path / "defaults" / output_file_path
    output.resolve()

    # Create parent directories if they don't exist yet.
    # Needed if the <role_path>/defaults was not created yet.
    output.parent.mkdir(parents=True, exist_ok=True)

    with open(output, "w", encoding="utf-8") as defaults_file:
        defaults_file.writelines(
            ["---" + linesep, "# Automatically generated by aar-doc" + linesep],
        )
        yaml.dump(role_defaults, defaults_file)
