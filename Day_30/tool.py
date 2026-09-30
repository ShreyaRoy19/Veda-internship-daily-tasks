import argparse
import sys
import pandas as pd

def load_data(filepath):
    """Loads dataset from CSV file safely."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: The file '{filepath}' was not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading CSV file: {e}", file=sys.stderr)
        sys.exit(1)

def validate_columns(df, columns):
    """Validates if the given columns exist in the dataset dataframe."""
    for col in columns:
        if col and col not in df.columns:
            print(f"Error: Column '{col}' does not exist in the dataset.", file=sys.stderr)
            print(f"Available columns: {list(df.columns)}", file=sys.stderr)
            sys.exit(1)

def main():
    # Set up argument parser for CLI help and options
    parser = argparse.ArgumentParser(
        description="Command-Line Data Analysis Tool using Pandas and Argparse"
    )
    
    # Do not hardcode the dataset filename; accept it as an argument
    parser.add_argument(
        "-f", "--file", 
        required=True, 
        help="Path to the input CSV dataset file"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available analysis commands")

    # 1. Summary Command
    subparsers.add_parser("summary", help="Show basic summary of the dataset (shape, types, missing values)")

    # 2. Stats Command
    stats_parser = subparsers.add_parser("stats", help="Show statistical report")
    stats_parser.add_argument("-c", "--column", help="Specific column for statistics")

    # 3. Filter Command
    filter_parser = subparsers.add_parser("filter", help="Filter rows based on a specific column value")
    filter_parser.add_argument("-c", "--column", required=True, help="Column name to filter on")
    filter_parser.add_argument("-v", "--value", required=True, help="Value to match")

    # 4. Group Command
    group_parser = subparsers.add_parser("group", help="Group data and aggregate")
    group_parser.add_argument("-c", "--column", required=True, help="Column to group by")
    group_parser.add_argument("-agg", "--agg-column", required=True, help="Column to apply aggregation on")
    group_parser.add_argument("--func", default="mean", choices=["mean", "sum", "count", "min", "max"], help="Aggregation function")

    args = parser.parse_args()

    # Load data dynamically
    df = load_data(args.file)

    # Execute commands
    if args.command == "summary":
        print("=== Dataset Summary ===")
        print(f"Total Rows: {df.shape[0]}")
        print(f"Total Columns: {df.shape[1]}")
        print("\nData Types:")
        print(df.dtypes)
        print("\nMissing Values:")
        print(df.isnull().sum())

    elif args.command == "stats":
        if args.column:
            validate_columns(df, [args.column])
            print(f"=== Statistics for '{args.column}' ===")
            print(df[args.column].describe())
        else:
            print("=== Statistical Report for All Numeric Columns ===")
            print(df.describe())

    elif args.command == "filter":
        validate_columns(df, [args.column])
        val = args.value
        # Handle numeric conversion if column is numeric
        if pd.api.types.is_numeric_dtype(df[args.column]):
            try:
                val = float(val) if "." in val else int(val)
            except ValueError:
                pass

        filtered_df = df[df[args.column] == val]
        print(f"=== Filtered Data (Rows: {len(filtered_df)}) ===")
        print(filtered_df.to_string())

    elif args.command == "group":
        validate_columns(df, [args.column, args.agg_column])
        print(f"=== Grouped by '{args.column}' (Aggregating '{args.agg_column}' via {args.func}) ===")
        grouped = df.groupby(args.column)[args.agg_column].agg(args.func).reset_index()
        print(grouped.to_string())

    else:
        parser.print_help()

if __name__ == "__main__":
    main()
