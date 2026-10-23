"""Structural safeguards that keep the template student-ready."""

from pathlib import Path

import nbformat

ROOT = Path(__file__).parents[1]


def test_required_student_guidance_and_product_boundaries_exist() -> None:
    required = (
        "START_HERE.md",
        "STUDENT_IMPLEMENTATION_GUIDE.md",
        "PROJECT_CHECKLIST.md",
        "MILESTONES.md",
        "docs/PRODUCT_CONTRACT.md",
        "docs/DATASET_CARD.md",
        "docs/MODEL_CARD.md",
        "docs/OPERATIONS.md",
        "docs/NOTEBOOK_CASE_STUDY_STANDARD.md",
        "docs/PUBLIC_DATA_SOURCES.md",
        "configs/student.toml.example",
        "notebooks/README.md",
        "Dockerfile",
        "compose.yaml",
        "src/dsm_project/algorithms/student/README.md",
    )
    for relative_path in required:
        assert (ROOT / relative_path).is_file(), relative_path


def test_examples_request_the_named_project_kernel() -> None:
    notebooks = sorted((ROOT / "examples").glob("**/*.ipynb"))
    assert len(notebooks) >= 10
    for path in notebooks:
        notebook = nbformat.read(path, as_version=4)
        assert notebook.metadata.kernelspec.name == "dsm-project"


def test_sensitive_and_generated_paths_are_ignored() -> None:
    ignore = (ROOT / ".gitignore").read_text()
    for pattern in (".env", ".venv/", "data/local/*", "artifacts/*"):
        assert pattern in ignore
