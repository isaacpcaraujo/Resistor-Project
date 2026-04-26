#!/bin/bash
# Environment setup for HPC
# Modify this file according to your cluster's module system

module load python/3.10
module load cuda/11.8
module load cudnn/8.6.0

# Activate virtual environment
source ~/.venv/bin/activate

# Ensure src/ is in PYTHONPATH
export PYTHONPATH="$PWD:$PYTHONPATH"
