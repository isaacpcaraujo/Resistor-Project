# ATLAS/LHC Signal Classification ML Platform

Welcome to the **ATLAS/LHC Signal Classification Platform** (Resistor-Project). This repository contains a modular Python-based platform designed for training, validating, comparing, and interpreting machine learning models applied to the classification of signals originating from hadronic collisions within the ATLAS experiment at the LHC.

## 🚀 Overview

The primary goal of this application is to allow researchers and scientists to configure complex machine learning experiments easily, using declarative JSON configuration files. The system guarantees scientific rigor, strong reproducibility, and scalability.

### Key Features
- **Declarative Experiments:** Configure all parameters (datasets, models, hyperparameters, and evaluation metrics) through simple JSON files.
- **Robust Validation:** Strict JSON schema and data type validation (using Pydantic) to avoid runtime errors and ensure reliable scientific pipelines.
- **End-to-End Pipeline:** Automates data preparation, model training (e.g., XGBoost, CNNs), cross-validation, and metric evaluation.
- **Scalable Architecture:** Clean, modular structure designed for easy expansion, experimentation comparison, and HPC job submissions.

## 📁 Project Architecture

The codebase follows a strict modular structure to maintain a clean separation of concerns:

```text
Resistor-Project/
├── configs/             # Declarative JSON configuration files
├── data/                # Datasets and raw experimental data
├── experiments/         # Saved experiment states and configurations
├── logs/                # Execution logs for debugging and auditing
├── outputs/             # Generated output files, models, and artifacts
├── tests/               # Automated unit and integration tests
├── src/                 # Main source code directory
│   ├── config/          # Pydantic schemas, validators, and config loaders
│   ├── data/            # Data ingestion and datasets management
│   ├── preprocessing/   # Normalization, outlier removal, feature selection
│   ├── models/          # Model architectures and wrappers
│   ├── training/        # Training loops, seeds, and cross-validation
│   ├── evaluation/      # Accuracy, precision, recall, ROC-AUC calculators
│   ├── visualization/   # Diagnostic plots and metric visualizations
│   ├── pipelines/       # Orchestration of the ML lifecycle
│   └── utils/           # General-purpose utility functions
└── main.py              # Application entry point
```

## ⚙️ Configuration (The JSON Contract)

Experiments are driven entirely by JSON configuration files. This eliminates the need to hardcode parameters and allows easy versioning of experiments.

**Example `configs/template.json`:**
```json
{
  "experiment_name": "atlas_signal_classifier",
  "dataset": {
    "path": "data/events.csv",
    "target_column": "label",
    "train_split": 0.8
  },
  "preprocessing": {
    "normalize": true,
    "remove_outliers": false,
    "feature_selection": false
  },
  "model": {
    "type": "xgboost",
    "hyperparameters": {
      "max_depth": 6,
      "learning_rate": 0.1,
      "n_estimators": 200
    }
  },
  "training": {
    "random_seed": 42,
    "cross_validation_folds": 5
  },
  "evaluation": {
    "metrics": [
      "accuracy",
      "precision",
      "recall",
      "f1",
      "roc_auc"
    ]
  }
}
```

## 🛠️ Usage

1. **Setup your Environment:** Ensure you have Python installed, activate your virtual environment (e.g., `.venv`), and install dependencies.
2. **Define an Experiment:** Create a new JSON file inside the `configs/` directory describing your model and dataset.
3. **Run the Pipeline:** Execute the main script, passing the config file as an argument (implementation dependent):
   ```bash
   python main.py --config configs/template.json
   ```
4. **Analyze Results:** Check the `outputs/`, `logs/`, and `experiments/` directories for the generated metrics, visualizations, and saved models.

## 📝 License

*(Refer to the LICENSE file for more information)*
