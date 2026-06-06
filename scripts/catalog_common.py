from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml


ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = ROOT / "catalog" / "tools.yml"
SCHEMA_PATH = ROOT / "schema" / "tool.schema.json"
README_PATH = ROOT / "README.md"
CATALOG_JSON_PATH = ROOT / "dist" / "catalog.v2.json"


STATUS_ORDER = {
    "recommended": 0,
    "situational": 1,
    "watch": 2,
    "avoid": 3,
}


class UniqueKeyLoader(yaml.SafeLoader):
    pass


def construct_mapping(loader: UniqueKeyLoader, node: yaml.Node, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ValueError(f"duplicate YAML key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_mapping,
)


def load_catalog() -> dict[str, Any]:
    with CATALOG_PATH.open("r", encoding="utf-8") as handle:
        data = yaml.load(handle, Loader=UniqueKeyLoader)
    if not isinstance(data, dict):
        raise ValueError("catalog/tools.yml must contain a mapping")
    return data


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    return slug or "category"


def sort_tools(tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return sorted(
        tools,
        key=lambda item: (
            STATUS_ORDER.get(str(item.get("recommended_status")), 99),
            str(item.get("name", "")).lower(),
        ),
    )
