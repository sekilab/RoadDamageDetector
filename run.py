#!/usr/bin/env python3
"""Small launcher for the RoadDamageDetector repository.

This project is an older TensorFlow 1.x object-detection codebase and is not a
modern one-click app. The goal of this launcher is to make the setup and usage
clearer and easier to execute from the repository root.

Typical flow:
    1. Create a virtual environment
    2. pip install -r requirements.txt
    3. python run.py check-env
    4. python run.py download-dataset
    5. Follow the TensorFlow Object Detection API training flow
"""

from __future__ import annotations

import argparse
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent

DATASET_URLS = {
    "RoadDamageDataset.tar.gz": "https://s3-ap-northeast-1.amazonaws.com/mycityreport/RoadDamageDataset.tar.gz",
    "trainedModels.tar.gz": "https://s3-ap-northeast-1.amazonaws.com/mycityreport/trainedModels.tar.gz",
}


def print_banner() -> None:
    print("=" * 72)
    print("RoadDamageDetector launcher")
    print("This repo expects TensorFlow 1.x and a classic object-detection workflow.")
    print("=" * 72)


def check_python_version() -> None:
    version = sys.version_info
    print(f"Python version: {version.major}.{version.minor}.{version.micro}")
    if version.major != 3 or version.minor not in (7, 8):
        print("WARNING: Python 3.7 or 3.8 is recommended for TensorFlow 1.x compatibility.")
    else:
        print("Python version looks compatible with TensorFlow 1.x.")


def check_tensorflow() -> None:
    try:
        import tensorflow as tf  # type: ignore

        print(f"TensorFlow found: {tf.__version__}")
        if not tf.__version__.startswith("1."):
            print("WARNING: This repo was written for TensorFlow 1.x. TensorFlow 2.x may not work directly.")
    except Exception:
        print("TensorFlow is not installed yet. Install requirements first:")
        print("  pip install -r requirements.txt")


def check_environment() -> None:
    print_banner()
    check_python_version()
    check_tensorflow()
    print("\nRepository root:", ROOT)
    print("Suggested next step: install requirements and then prepare the dataset.")


def download_dataset() -> None:
    print_banner()
    for filename, url in DATASET_URLS.items():
        target = ROOT / filename
        if target.exists():
            print(f"{filename} already exists: {target}")
            continue

        print(f"Downloading {filename} ...")
        urllib.request.urlretrieve(url, str(target))
        print(f"Saved to: {target}")

    print("\nDownload complete. Extract the archives in the project root if needed.")
    print("Example:")
    print("  tar -zxf RoadDamageDataset.tar.gz")
    print("  tar -zxf trainedModels.tar.gz")


def print_usage_examples() -> None:
    print("Usage examples:")
    print("  python run.py check-env")
    print("  python run.py download-dataset")
    print("  python run.py train")
    print("  python run.py export")
    print("  python run.py notebook")


def print_training_guide() -> None:
    print("\nThis repo is based on the TensorFlow Object Detection API.")
    print("You will usually need the following workflow:")
    print("  1. Install TensorFlow 1.x and project dependencies")
    print("  2. Download and extract the dataset archives")
    print("  3. Prepare Pascal VOC XML annotations and label map")
    print("  4. Generate TFRecord files")
    print("  5. Train using a model config file")
    print("  6. Export the frozen inference graph")
    print("\nExample TF OD API train command:")
    print("  python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1.config")
    print("\nExample export command:")
    print("  python export_inference_graph.py --input_type image_tensor --pipeline_config_path training/ssd_mobilenet_v1.config --trained_checkpoint_prefix training/model.ckpt-<N> --output_directory inference_graph")


def print_notebook_guide() -> None:
    print("Open the tutorial notebook to inspect dataset structure and usage:")
    print("  RoadDamageDatasetTutorial.ipynb")
    print("This is the best reference for this repository's original workflow.")


def run_train() -> None:
    print_banner()
    print_training_guide()


def run_export() -> None:
    print_banner()
    print("This project uses TensorFlow's export step after training.")
    print_training_guide()


def run_notebook() -> None:
    print_banner()
    print_notebook_guide()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="RoadDamageDetector repo launcher")
    parser.add_argument(
        "command",
        nargs="?",
        default="info",
        choices=["info", "check-env", "download-dataset", "train", "export", "notebook"],
        help="Command to run.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.command in ("info", "check-env"):
        check_environment()
    elif args.command == "download-dataset":
        download_dataset()
    elif args.command == "train":
        run_train()
    elif args.command == "export":
        run_export()
    elif args.command == "notebook":
        run_notebook()
    else:
        print_usage_examples()


if __name__ == "__main__":
    main()
