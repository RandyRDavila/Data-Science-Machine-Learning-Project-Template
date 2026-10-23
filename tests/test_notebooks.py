"""Execute every reference notebook from top to bottom."""

from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

PROJECT_ROOT = Path(__file__).parents[1]
NOTEBOOKS = sorted((PROJECT_ROOT / "examples").glob("**/*.ipynb"))


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
