# Student project case studies

Create the project's executable technical articles here. The reference reports
under `examples/` demonstrate the expected narrative and package boundary; do
not edit them into the submission.

A useful sequence is:

```text
notebooks/
├── 01-data-contract-and-exploration.ipynb
├── 02-supervised-methods.ipynb
├── 03-unsupervised-structure.ipynb
├── 04-model-selection-and-error-analysis.ipynb
└── 05-production-evidence.ipynb
```

Split a report when one clear question becomes several unrelated questions.
Filenames should sort in reading order and describe the analysis rather than a
calendar date.

Every notebook must:

- load configuration and data through `dsm_project`;
- import student algorithms and evaluation behavior from the package;
- identify trusted references explicitly;
- explain the question, data, mathematics, evidence, failures and limitations;
- use purposeful, labeled visualizations;
- run from top to bottom in the **DSM Project** kernel; and
- keep reusable behavior out of notebook-only state.

Follow [`docs/NOTEBOOK_CASE_STUDY_STANDARD.md`](../docs/NOTEBOOK_CASE_STUDY_STANDARD.md).
