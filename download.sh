#!/bin/bash

# Define the start and end dates
start_date="2020-03-28"
end_date="2021-04-05"

# Convert start and end dates to seconds since epoch
start_seconds=$(date -d "$start_date" +%s)
end_seconds=$(date -d "$end_date" +%s)
# Define the directory to save the downloaded files
download_dir="downloads"

# Create the directory if it doesn't exist
mkdir -p "$download_dir"
# Loop through each day in the date range
current_seconds=$start_seconds
while [ $current_seconds -le $end_seconds ]; do
    # Convert current seconds back to date format
    current_date=$(date -d "@$current_seconds" +%Y-%m-%d)
    
    # Construct the URL
    url="https://www.ins.gov.co/BoletinesCasosCOVID19Colombia/$current_date.xlsx"
    
    # Download the file
    wget "$url" -O "$download_dir/$current_date.xlsx"
    
    # Move to the next day
    current_seconds=$((current_seconds + 86400)) # Increment by one day (86400 seconds)
done

echo "Download completed."
