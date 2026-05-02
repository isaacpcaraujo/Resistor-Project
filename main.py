import argparse
import sys
from pydantic import ValidationError
from src.config.loader import load_config

def main():
    parser = argparse.ArgumentParser(description="Main script to run machine learning experiments.")
    parser.add_argument("config_file", type=str, help="Path to the JSON configuration file (e.g., configs/cnn1d_experiment.json)")
    
    args = parser.parse_args()
    
    print(f"Loading configuration from: {args.config_file}...")
    try:
        config = load_config(args.config_file)
        print("\nConfiguration loaded and validated successfully!")
        print("="*50)
        print(f"Experiment: {config.experiment_name}")
        print(f"Model: {config.model.type}")
        print(f"Dataset: {config.dataset.path} (target: {config.dataset.target_column})")
        print("="*50)
        
        # Instantiate and build the model using the Factory pattern
        from src.models.factory import ModelFactory
        model = ModelFactory.create(config)
        print("\nModel instantiated and ready for use!")
        
        # Future: data would be loaded and split here:
        # X_train, y_train, ... = data_pipeline.load_and_split(config)
        # model.train(X_train, y_train)
        # model.evaluate(X_test, y_test)
        
    except FileNotFoundError as e:
        print(f"\nError: {e}", file=sys.stderr)
        sys.exit(1)
    except ValidationError as e:
        print(f"\nConfiguration validation error:", file=sys.stderr)
        print(e, file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"\nUnexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
