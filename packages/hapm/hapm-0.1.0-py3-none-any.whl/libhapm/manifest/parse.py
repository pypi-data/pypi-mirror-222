"""HAPM manifest parsing utils"""

from re import match
from typing import Dict, List, Optional, Tuple

from libhapm.package import PackageDescription


def parse_entry(entry: str) -> Tuple[Optional[str], Optional[str]]:
    """Parses the manifest entry to the address and version"""
    parts = match(r"(.[^@]*)(@(.*))?", entry)
    if parts is None:
        return (None, None)
    return (parts.group(1), parts.group(3))


def parse_category(manifest: Dict[str, List[str]], key: str) -> List[PackageDescription]:
    """Parses the manifest, turning it into a list of packages"""
    if key not in manifest:
        raise TypeError(f"Key {key} is not found in repo")
    items: List[PackageDescription] = []
    for entry in manifest[key]:
        (full_name, version) = parse_entry(entry)
        if full_name is None:
            raise TypeError(f"Wrong entity: {entry}")
        if version is None:
            raise TypeError(f"Version is missing: {entry}")
        items.append({
            "full_name": full_name,
            "version": version,
            "kind": key
        })
    return items
