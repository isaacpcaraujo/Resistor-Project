import json
import os

def generate_sbatch(config_path, output_path="job.sbatch"):
    with open(config_path, 'r') as f:
        config = json.load(f)

    hpc = config.get("hpc", {})
    job_name = config.get("experiment_name", "ringer_job")
    
    sbatch_content = f"""#!/bin/bash
#SBATCH --job-name={job_name}
#SBATCH --output=logs/{job_name}_%j.out
#SBATCH --error=logs/{job_name}_%j.err
#SBATCH --partition={hpc.get('queue', 'gpu')}
#SBATCH --nodes={hpc.get('nodes', 1)}
#SBATCH --ntasks-per-node=1
#SBATCH --gres=gpu:{hpc.get('gpus_per_node', 1)}
#SBATCH --time={hpc.get('time', '24:00:00')}
#SBATCH --mem={hpc.get('memory', '64G')}

# Load environment
source config/env_setup.sh

# Run training
echo "Starting training for experiment: {job_name}"
python src/core/trainer.py --config {config_path}
echo "Training finished!"

# Run analysis
echo "Starting analysis..."
python src/analysis/metrics.py --config {config_path}
echo "Analysis finished!"
"""

    os.makedirs("logs", exist_ok=True)
    with open(output_path, "w") as f:
        f.write(sbatch_content)
    
    print(f"Generated Slurm script: {output_path}")
    return output_path

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Generate Slurm sbatch file from config")
    parser.add_argument("config", help="Path to experiment JSON config")
    parser.add_argument("--out", default="job.sbatch", help="Output sbatch file path")
    args = parser.parse_args()
    generate_sbatch(args.config, args.out)
