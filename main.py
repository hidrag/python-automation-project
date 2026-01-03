import csv
import logging
import argparse
import os
import sys

from config import DEFAULT_INPUT_FILE, DEFAULT_OUTPUT_FILE, LOG_FILE
from validator import validate_user
from processor import process_user
from reporter import generate_summary

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Python Automation Tool for CSV Data Processing"
    )
    parser.add_argument(
        "--input",
        help="Path to input CSV file",
        default=DEFAULT_INPUT_FILE
    )
    parser.add_argument(
        "--output",
        help="Path to output CSV file",
        default=DEFAULT_OUTPUT_FILE
    )
    return parser.parse_args()


def read_users(file_path):
    with open(file_path, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_users(users, file_path):
    with open(file_path, "w", newline="", encoding="utf-8") as f:
        fieldnames = users[0].keys()
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(users)


def main():
    args = parse_arguments()

    if not os.path.isfile(args.input):
        print(f"Error: Input CSV file not found → {args.input}")
        sys.exit(1)

    logging.info("Automation started")
    logging.info(f"Input file: {args.input}")
    logging.info(f"Output file: {args.output}")

    raw_users = read_users(args.input)
    valid_users = []

    for user in raw_users:
        errors = validate_user(user)
        if errors:
            logging.error(f"Invalid record {user}: {errors}")
            continue

        processed_user = process_user(user)
        valid_users.append(processed_user)

    if not valid_users:
        print("No valid records found. Output file not generated.")
        sys.exit(0)

    write_users(valid_users, args.output)

    summary = generate_summary(valid_users)
    logging.info(f"Summary: {summary}")

    print("Processing completed successfully.")
    print("Summary:", summary)


if __name__ == "__main__":
    main()
