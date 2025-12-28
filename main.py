import argparse
import os
import sys

# Robust Path Fix: Add project root to sys.path
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from pipelines import optimize_bootstrap, optimize_mipro, distill

def main():
    parser = argparse.ArgumentParser(description="AURA CLI")
    subparsers = parser.add_subparsers(dest="command")
    
    # Optimization
    opt_parser = subparsers.add_parser("optimize")
    opt_parser.add_argument("--method", choices=["bootstrap", "mipro"], required=True)
    opt_parser.add_argument("--api-key", required=True)
    
    # Distillation
    dist_parser = subparsers.add_parser("distill")
    dist_parser.add_argument("--api-key", required=True)
    
    args = parser.parse_args()
    
    if args.command == "optimize":
        if args.method == "bootstrap":
            optimize_bootstrap.run(args.api_key)
        elif args.method == "mipro":
            optimize_mipro.run(args.api_key)
            
    elif args.command == "distill":
        distill.run(args.api_key, None) # None for teacher path default behavior
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
