#!/usr/bin/env python3
import argparse
import subprocess
import os
from src.jobs.slurm_generator import generate_sbatch

def main():
    parser = argparse.ArgumentParser(description="Ringer ML Orchestrator - Job Submitter")
    parser.add_argument("config", help="Path to experiment JSON config")
    parser.add_argument("--dry-run", action="store_true", help="Generate sbatch but do not submit")
    args = parser.parse_args()

    if not os.path.exists(args.config):
        print(f"Error: Config file '{args.config}' not found.")
        return

    print(f"Reading configuration from {args.config}...")
    sbatch_file = generate_sbatch(args.config)

    if args.dry_run:
        print("Dry run enabled. Skipping submission.")
        print(f"To submit manually, run: sbatch {sbatch_file}")
    else:
        print("Submitting job to Slurm...")
        try:
            result = subprocess.run(["sbatch", sbatch_file], check=True, capture_output=True, text=True)
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error submitting job: {e.stderr}")
        except FileNotFoundError:
            print("Error: 'sbatch' command not found. Are you on an HPC cluster?")
            print("If testing locally, use --dry-run or run python src/core/trainer.py directly.")

if __name__ == "__main__":
    main()
