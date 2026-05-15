"""One-off script: add quantum_circuit_drawer imports and replace .draw('mpl') / .draw(\"mpl\")."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

IMPORT_LINES = [
    "# %matplotlib widget\n",
    "from quantum_circuit_drawer import DrawConfig, OutputOptions, draw_quantum_circuit\n",
    "from quantum_circuit_drawer import draw_quantum_circuit as _draw_qc\n",
    "\n",
    "draw_quantum_circuit = lambda x: _draw_qc(x, config=DrawConfig(output=OutputOptions(show=False)))\n",
]

DRAW_SUFFIX_RE = re.compile(r"\.draw\((['\"])mpl\1\)")

DISPLAY_DRAW_RE = re.compile(
    r"^(\s*)display\((.+)\.draw\((['\"])mpl\3\)\)\s*(#.*)?\s*$"
)

STANDALONE_DRAW_RE = re.compile(
    r"^(\s*)(.+)\.draw\((['\"])mpl\3\)\s*(#.*)?\s*$"
)


def _has_drawer_imports(source: list[str]) -> bool:
    text = "".join(source)
    return (
        "quantum_circuit_drawer" in text
        and "DrawConfig" in text
        and "_draw_qc" in text
    )


def _first_import_cell_idx(cells: list[dict]) -> int | None:
    for i, cell in enumerate(cells):
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        if isinstance(src, str):
            src = [src]
        for line in src:
            s = line.strip()
            if s.startswith("import ") or s.startswith("from "):
                return i
    return None


def _insert_import_block(cells: list[dict]) -> None:
    idx = _first_import_cell_idx(cells)
    if idx is None:
        return
    cell = cells[idx]
    src = cell.get("source", [])
    if isinstance(src, str):
        src = [src]
    if _has_drawer_imports(src):
        return
    insert_at = 0
    while insert_at < len(src) and src[insert_at].lstrip().startswith("%"):
        insert_at += 1
    spacer = ["\n"] if insert_at < len(src) else []
    cell["source"] = src[:insert_at] + IMPORT_LINES + spacer + src[insert_at:]


def _notebook_has_full_drawer_imports(cells: list[dict]) -> bool:
    for cell in cells:
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        if isinstance(src, str):
            src = [src]
        if _has_drawer_imports(src):
            return True
    return False


def _drop_redundant_drawconfig_lines(source: list[str]) -> list[str]:
    return [
        line
        for line in source
        if line.strip() != "from quantum_circuit_drawer import DrawConfig"
    ]


def _transform_source_cell(source: list[str], drop_drawconfig_only: bool) -> list[str]:
    if isinstance(source, str):
        source = [source]
    out: list[str] = []
    i = 0
    while i < len(source):
        line = source[i]
        stripped = line.strip()

        if (
            i + 1 < len(source)
            and DRAW_SUFFIX_RE.search(line)
            and stripped.startswith("#")
            and "draw_quantum_circuit(" in source[i + 1]
            and not source[i + 1].strip().startswith("#")
        ):
            out.append(line)
            out.append(source[i + 1])
            i += 2
            continue

        if DRAW_SUFFIX_RE.search(line) and not stripped.startswith("#"):
            if i + 1 < len(source) and "draw_quantum_circuit(" in source[i + 1]:
                nxt = source[i + 1]
                if not nxt.strip().startswith("#"):
                    out.append(line)
                    out.append(nxt)
                    i += 2
                    continue

            m_disp = DISPLAY_DRAW_RE.match(line)
            if m_disp:
                indent, inner = m_disp.group(1), m_disp.group(2).strip()
                orig = line.rstrip("\n")
                out.append(f"{indent}# {orig}\n")
                out.append(f"{indent}draw_quantum_circuit({inner})\n")
                i += 1
                continue

            m_stand = STANDALONE_DRAW_RE.match(line)
            if m_stand:
                indent, expr = m_stand.group(1), m_stand.group(2).strip()
                orig = line.rstrip("\n")
                out.append(f"{indent}# {orig}\n")
                out.append(f"{indent}draw_quantum_circuit({expr})\n")
                i += 1
                continue

        out.append(line)
        i += 1

    if drop_drawconfig_only:
        out = _drop_redundant_drawconfig_lines(out)
    return out


def process_notebook(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    cells = data.get("cells", [])
    _insert_import_block(cells)
    drop_dc = _notebook_has_full_drawer_imports(cells)
    for cell in cells:
        if cell.get("cell_type") != "code":
            continue
        src = cell.get("source", [])
        if isinstance(src, str):
            src = [src]
        cell["source"] = _transform_source_cell(src, drop_dc)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    for p in sorted(ROOT.glob("**/*.ipynb")):
        if p.name.startswith("_") or ".ipynb_checkpoints" in str(p):
            continue
        process_notebook(p)
        print("patched", p.relative_to(ROOT))


if __name__ == "__main__":
    main()
