"""Integration tests for supervised and unsupervised experiment paths."""

import numpy as np

from dsm_project.config import load_config
from dsm_project.contracts import TaskKind
from dsm_project.data import load_project_dataset
from dsm_project.evaluation import comparison_table
from dsm_project.experiments import (
    available_models,
    fit_supervised_candidate,
    run_clustering_example,
    run_pca_example,
)


def configured_example():
    config = load_config("configs/example.toml")
    return config, load_project_dataset(config)


def test_supervised_reference_paths_produce_finite_evidence() -> None:
    config, dataset = configured_example()
    regression = fit_supervised_candidate(
        dataset, config, task_name="regression", model_name="linear_regression"
    )
    classification = fit_supervised_candidate(
        dataset,
        config,
        task_name="classification",
        model_name="logistic_regression",
    )

    assert np.isfinite(regression.metric_value)
    assert 0.0 <= classification.metric_value <= 1.0
    assert regression.train_rows + regression.test_rows == len(dataset.observations)


def test_every_declared_classification_family_runs() -> None:
    config, dataset = configured_example()
    table = comparison_table(
        dataset,
        config,
        task_name="classification",
        model_names=available_models(TaskKind.CLASSIFICATION),
    )

    assert set(table["model"]) == set(available_models(TaskKind.CLASSIFICATION))
    assert table["value"].between(0.0, 1.0).all()


def test_unsupervised_paths_do_not_require_targets_for_fitting() -> None:
    config, dataset = configured_example()
    clustering = run_clustering_example(dataset, config)
    representation = run_pca_example(dataset)

    assert len(clustering.labels) == len(dataset.observations)
    assert -1.0 <= clustering.stability_ari <= 1.0
    assert representation.coordinates.shape == (len(dataset.observations), 2)
    assert 0.0 < representation.explained_variance_ratio.sum() <= 1.0
