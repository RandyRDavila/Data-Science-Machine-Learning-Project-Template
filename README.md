# Data Science and Machine Learning Project Template

This repository is the starting point for final projects in Rice University
CMOR 438 / INDE 577. It demonstrates how a machine-learning investigation
becomes a tested, reproducible, and operated software product.

Students write their project **on top of this working production shell**. They
supply the domain and data, implement the course algorithms, register those
implementations behind stable interfaces, design the evaluation, and evolve
the API and user experience. The included wine-chemistry path proves that the
untouched system works from data ingestion through a served prediction; it is
not a suggested project topic or a substitute for student implementation.

Scikit-learn models in `src/dsm_project/experiments/` are deliberately marked
as **reference models**. They provide trusted comparisons and keep the shell
executable while student code is under development. Calling one does not
satisfy an algorithm-implementation requirement.

## Start here

1. Read [`START_HERE.md`](START_HERE.md).
2. Create a repository with GitHub's **Use this template** button.
3. Complete [`docs/PRODUCT_CONTRACT.md`](docs/PRODUCT_CONTRACT.md) before
   fitting models.
4. Put local data under `data/local/`, which Git ignores.
5. Configure the data boundary in `configs/student.toml`.
6. Follow [`STUDENT_IMPLEMENTATION_GUIDE.md`](STUDENT_IMPLEMENTATION_GUIDE.md)
   and implement reusable behavior under `src/dsm_project/`.
7. Use notebooks under `examples/` as executable reports, not as the product.
8. Require tests and review before merging changes.

## System path

```text
documented student data
    -> adapter and validation
    -> durable local or remote data boundary
    -> declared supervised and unsupervised tasks
    -> reproducible experiments
    -> versioned model artifact
    -> API and analytical client
    -> logs, metrics, monitoring, and revision evidence
```

## Repository map

| Location | Responsibility |
| --- | --- |
| `examples/` | Short, executable demonstrations aligned with course topics |
| `src/dsm_project/data/` | Data adapters, validation, provenance, and task declarations |
| `src/dsm_project/algorithms/student/` | Student-owned algorithm implementations |
| `src/dsm_project/algorithms/registry.py` | Explicit connection between student code and the product |
| `src/dsm_project/experiments/` | Repeatable training and clearly labeled trusted-reference comparisons |
| `src/dsm_project/evaluation/` | Metrics and evidence appropriate to each task |
| `src/dsm_project/artifacts/` | Save/load contracts and model metadata |
| `src/dsm_project/service/` | Prediction API and health interfaces |
| `src/dsm_project/monitoring/` | Structured operational evidence |
| `tests/` | Unit, integration, contract, notebook, and system verification |
| `docs/` | Product, data, model, team, operations, and decision records |

## Commands

```bash
uv sync --locked
uv run python scripts/setup_project.py
uv run dsm-project verify
uv run pytest -q
uv run ruff check src tests scripts
```

The setup command installs the named **DSM Project** notebook kernel. VS Code
is the intended notebook interface; the command does not launch JupyterLab.

## Boundaries

- Do not commit private, restricted, licensed, or large raw data.
- Do not commit credentials or `.env` files.
- Do not force an algorithm onto an incompatible task merely to check a box.
- Do not put reusable training, API, or monitoring behavior only in notebooks.
- Do not report final-test results until the model-selection procedure is frozen.

See [`PROJECT_CHECKLIST.md`](PROJECT_CHECKLIST.md) for the required student
work and [`MILESTONES.md`](MILESTONES.md) for a recommended sequence.
