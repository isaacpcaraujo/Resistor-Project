#!/bin/bash
#SBATCH --job-name=ringer_v2_training
#SBATCH --output=logs/ringer_v2_training_%j.out
#SBATCH --error=logs/ringer_v2_training_%j.err
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:1
#SBATCH --time=24:00:00
#SBATCH --mem=64G

# Load environment
source config/env_setup.sh

# Run training
echo "Starting training for experiment: ringer_v2_training"
python src/core/trainer.py --config config/template.json
echo "Training finished!"

# Run analysis
echo "Starting analysis..."
python src/analysis/metrics.py --config config/template.json
echo "Analysis finished!"
