# Executable course-topic examples

These notebooks are compact executable reports, not places to hide product
implementations. They import reusable behavior from `src/dsm_project/`, use the
same configured data boundary, and run in CI. Where an example calls a
scikit-learn estimator, it is showing the trusted reference path. Students must
make their own registered implementation appear alongside that reference.

Each example follows the project case-study arc: motivating question, package
data boundary, focused exploration, mathematical model, package experiment,
diagnostics, limitations, and a concrete student extension. Read
[`docs/NOTEBOOK_CASE_STUDY_STANDARD.md`](../docs/NOTEBOOK_CASE_STUDY_STANDARD.md)
before creating project notebooks.

| Example | Course topic | Evidence produced |
| --- | --- | --- |
| `00-data-and-task-contract.ipynb` | Data, provenance, task, and leakage contracts | schema and task audit |
| `supervised/01-linear-regression-and-gradient-descent.ipynb` | Least squares and first-order optimization | regression metric and gradient trace |
| `supervised/02-logistic-regression-and-decisions.ipynb` | Probabilities, log loss, and decisions | classification evidence |
| `supervised/03-svm-margins-and-kernels.ipynb` | Margins and kernel geometry | linear/RBF comparison |
| `supervised/04-neighbors.ipynb` | Local geometry and scaling | neighbor-model evidence |
| `supervised/05-trees-and-ensembles.ipynb` | Recursive partitions, forests, and boosting | family comparison |
| `supervised/06-neural-networks.ipynb` | Composition and nonlinear models | neural candidate evidence |
| `supervised/07-model-selection.ipynb` | Selection as estimation | retained candidate table |
| `unsupervised/01-clustering.ipynb` | Clustering without fitting labels | silhouette and stability |
| `unsupervised/02-dimensionality-reduction.ipynb` | PCA and representation evidence | retained variance and projection |

Before using a notebook with project data, state what one row represents, what
information is available at the prediction or analysis time, and why the
algorithm is compatible with the task. The examples are starting points for
reasoning, not mandatory plots or conclusions.
