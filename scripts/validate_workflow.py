"""Validate Kaeru package/project structure; not product QA or a security audit.

Python 3.9+, standard library only. Does not modify the inspected directory.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.parse import unquote


TEMPLATE_DIRS = (
    "Agents", "Design", "Plan", "Memory", "Rules", "Research", "Revision", "Dist"
)
TEMPLATE_FILES = (
    "AGENTS.md",
    "Agents/project_manager.md", "Agents/design.md", "Agents/architect.md",
    "Agents/engineer.md", "Agents/database.md", "Agents/qa.md", "Agents/tech_lead.md",
    "Design/Design.md", "Design/frontend.md", "Design/backend.md", "Design/database.md",
    "Plan/Todo.md", "Plan/Phases/Phases(N).md",
    "Memory/Memory.md", "Memory/CodeMap.md", "Rules/Rules.md", "Rules/user.md",
    "Research/Research.md", "Revision/Revision(N).md", "Dist/README.md",
)
PACKAGE_FILES = ("README.md", "SKILL.md", "scripts/validate_workflow.py")
LINK = re.compile(r"\[[^\]\n]*\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)")
INLINE = re.compile(r"`([^`\n]+)`")


def inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def validate(root: Path, mode: str) -> dict:
    root = root.resolve()
    errors: list[str] = []
    warnings: list[str] = []
    required = TEMPLATE_FILES + (PACKAGE_FILES if mode == "package" else ())
    for name in required:
        candidate = root / name
        # Project initialization may consume/rename the numbered template files.
        if mode == "project" and "(N)" in name and not candidate.exists():
            continue
        if not candidate.is_file():
            errors.append("Missing required file: " + name)
        elif not inside(candidate.resolve(), root):
            errors.append("Required resource resolves outside root: " + name)

    root_names = {item.name for item in root.iterdir()} if root.is_dir() else set()
    if "AGENTS.md" not in root_names:
        errors.append("Entry point must be named exactly AGENTS.md")
    if "Agents.md" in root_names:
        errors.append("Stale mixed-case entry point: Agents.md")

    if mode == "package" and (root / "SKILL.md").is_file():
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", skill, re.S)
        if frontmatter is None:
            errors.append("SKILL.md needs YAML frontmatter")
        else:
            # Validate this package's simple scalar fields, not arbitrary YAML.
            fields = dict(re.findall(r"^([a-z-]+):[ \t]*(.+)$", frontmatter[1], re.M))
            name = fields.get("name", "").strip()
            description = fields.get("description", "").strip()
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
                errors.append("Invalid skill name")
            if name != "workflow-kaeru":
                errors.append("Unexpected skill name: " + name)
            if not 1 <= len(description) <= 1024:
                errors.append("Skill description length must be 1..1024")
            if name and root.name != name:
                warnings.append("For standalone installation, use directory " + name)
        if len(skill.splitlines()) >= 500:
            warnings.append("Keep SKILL.md below 500 lines for progressive disclosure")

    documents = set()
    for name in ("AGENTS.md", "README.md", "SKILL.md"):
        if mode == "project" and name != "AGENTS.md":
            continue
        if (root / name).is_file():
            documents.add(root / name)
    for directory in TEMPLATE_DIRS:
        path = root / directory
        if path.is_dir():
            documents.update(path.rglob("*.md"))

    links_checked = 0
    tables_checked = 0
    for document in sorted(documents):
        label = document.relative_to(root).as_posix()
        if not inside(document.resolve(), root):
            errors.append(label + ": resource resolves outside root")
            continue
        text = document.read_text(encoding="utf-8")
        if "Agents.md" in text:
            errors.append(label + ": stale reference to Agents.md")
        in_fence = False
        table_width = None
        for number, line in enumerate(text.splitlines(), 1):
            if line.lstrip().startswith(("```", "~~~")):
                in_fence = not in_fence
                table_width = None
                continue
            if in_fence:
                continue
            if line.startswith("|") and line.rstrip().endswith("|"):
                width = len(re.split(r"(?<!\\)\|", line.strip())) - 2
                if table_width is None:
                    tables_checked += 1
                elif width != table_width:
                    errors.append(f"{label}:{number}: inconsistent table columns")
                table_width = width
            else:
                table_width = None

        for match in LINK.finditer(text):
            target = match[1].strip("<>")
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            target = unquote(target.split("#", 1)[0])
            links_checked += 1
            resolved = (document.parent / target).resolve()
            if not inside(resolved, root) or not resolved.exists():
                errors.append(label + ": broken/outside local link: " + target)

        for reference in INLINE.findall(text):
            if reference.endswith(".md") and any(
                reference.startswith(directory + "/") for directory in TEMPLATE_DIRS
            ):
                # References in project documents use project-root-relative paths.
                if mode == "project" and "(N)" in reference:
                    continue
                if not (root / reference).is_file():
                    errors.append(label + ": missing root-relative document: " + reference)

    return {
        "root": str(root), "mode": mode, "ok": not errors,
        "documents_checked": len(documents), "local_links_checked": links_checked,
        "tables_checked": tables_checked,
        "errors": sorted(set(errors)), "warnings": sorted(set(warnings)),
        "limits": "Structural checks only; not product QA, security review, or full Agent Skills conformance.",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--mode", choices=("package", "project"), default="package")
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error("Root must be an existing directory")
    result = validate(args.root, args.mode)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
