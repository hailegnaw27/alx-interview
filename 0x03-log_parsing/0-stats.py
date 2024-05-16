#!/usr/bin/python3
"""Script for computing metrics from stdin input."""

import sys

# Initialize dictionary to store count of each status code
status_codes_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
                     '404': 0, '405': 0, '500': 0}

total_size = 0
count = 0  # keep count of the number of lines processed

try:
    for line in sys.stdin:
        line_list = line.split(" ")

        # Check if the line follows the specified input format
        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # Increment count of status code occurrences
            if status_code in status_codes_dict:
                status_codes_dict[status_code] += 1

            # Update total file size
            total_size += file_size

            # Update line count
            count += 1

        # Print statistics after every 10 lines
        if count == 10:
            count = 0  # Reset line count
            print('Total file size: {}'.format(total_size))

            # Print status code counts in ascending order
            for key, value in sorted(status_codes_dict.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except KeyboardInterrupt:
    pass  # Handle keyboard interruption

finally:
    print('Total file size: {}'.format(total_size))
    # Print final status code counts
    for key, value in sorted(status_codes_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value)))

