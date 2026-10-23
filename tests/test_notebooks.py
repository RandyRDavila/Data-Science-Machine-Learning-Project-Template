"""Execute every reference notebook from top to bottom."""

from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

PROJECT_ROOT = Path(__file__).parents[1]
NOTEBOOKS = sorted((PROJECT_ROOT / "examples").glob("**/*.ipynb"))


@pytest.mark.parametrize("notebook_path", NOTEBOOKS, ids=lambda path: path.name)
def test_notebook_has_case_study_structure(notebook_path: Path) -> None:
    notebook = nbformat.read(notebook_path, as_version=4)
    markdown = [cell for cell in notebook.cells if cell.cell_type == "markdown"]
    code = [cell for cell in notebook.cells if cell.cell_type == "code"]
    source = "\n".join(cell.source for cell in code)

    assert len(markdown) >= 3
    assert len(code) >= 2
    assert markdown[0].source.startswith("# ")
    assert "dsm_project" in source


@pytest.mark.parametrize("notebook_path", NOTEBOOKS, ids=lambda path: path.name)
def test_notebook_math_delimiters_are_balanced(notebook_path: Path) -> None:
    notebook = nbformat.read(notebook_path, as_version=4)
    for cell in notebook.cells:
        if cell.cell_type != "markdown":
            continue
        lines = [line.strip() for line in cell.source.splitlines()]
        assert "[" not in lines, "Use $$ rather than a bare [ math delimiter"
        assert "]" not in lines, "Use $$ rather than a bare ] math delimiter"
        assert cell.source.count("$$") % 2 == 0


@pytest.mark.parametrize("notebook_path", NOTEBOOKS, ids=lambda path: path.name)
def test_notebook_executes_from_a_clean_kernel(notebook_path: Path) -> None:
    notebook = nbformat.read(notebook_path, as_version=4)
    client = NotebookClient(
        notebook,
        timeout=180,
        kernel_name="dsm-project",
        resources={"metadata": {"path": str(PROJECT_ROOT)}},
    )

    client.execute()
