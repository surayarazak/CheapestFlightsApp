import json
import os
import glob
from find_cheapest_price import find_cheapest_price

def run_test_case(input_file_path):
    try:
        with open(input_file_path, 'r') as f:
            data = json.load(f)

        n = data.get('n')
        flights = data.get('flights')
        src = data.get('src')
        dst = data.get('dst')
        k = data.get('k')

        if None in [n, flights, src, dst, k]:
            print(f"Error: Missing parameters in {input_file_path}", file=os.sys.stderr)
            return

        result = find_cheapest_price(n, flights, src, dst, k)

        print(f"--- Test Case: {os.path.basename(input_file_path)} ---")
        print(f"Input: n={n}, flights={flights}, src={src}, dst={dst}, k={k}")
        print(f"Output: {result}")
        print("-" * 30)

    except FileNotFoundError:
        print(f"Error: Input file '{input_file_path}' not found.", file=os.sys.stderr)
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{input_file_path}'. Please check file format.", file=os.sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred for {input_file_path}: {e}", file=os.sys.stderr)

def main():
    script_dir = os.path.dirname(__file__)

    # Find all JSON files that start with 'input_example' or 'input_test_case'
    # Adjust the pattern as needed for your file names
    input_files_pattern = os.path.join(script_dir, 'input_example*.json')
    input_file_paths = sorted(glob.glob(input_files_pattern))

    if not input_file_paths:
        print(f"No input files found matching pattern '{input_files_pattern}'. Please check your file names.")
        return

    for file_path in input_file_paths:
        run_test_case(file_path)

if __name__ == "__main__":
    main()