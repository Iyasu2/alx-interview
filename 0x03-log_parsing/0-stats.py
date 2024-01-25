#!/usr/bin/python3
import sys

# Define the status codes to track
STATUS_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

# Initialize the metrics variables
total_file_size = 0
status_code_counts = {code: 0 for code in STATUS_CODES}

try:
    line_count = 0
    for line in sys.stdin:
        line = line.strip()
        parts = line.split()

        # Skip lines with incorrect format
        if len(parts) != 7 or parts[3] != "GET":
            continue

        try:
            status_code = int(parts[5])
            file_size = int(parts[6])
        except ValueError:
            continue

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1

        line_count += 1
        if line_count % 10 == 0:
            # Print statistics
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts):
                count = status_code_counts[code]
                if count > 0:
                    print(f"{code}: {count}")
            print()

except KeyboardInterrupt:
    # Print final statistics on keyboard interruption
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")
