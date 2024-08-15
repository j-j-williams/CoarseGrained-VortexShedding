#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <base_directory> <prefix>"
    exit 1
fi

# Base directory containing the folders of files
base_directory="$1"

# Prefix to use for renaming files
prefix="$2"

# Full directory path including the prefix
directory="${base_directory}${prefix}/"

# Change to the directory where the files are located
cd "$directory" || exit

# Loop over files from prefix_500.npy to prefix_0.npy
for i in {500..0}; do
    old_file="${prefix}_${i}.npy"
    new_file="${prefix}_$((i + 500)).npy"
    
    # Rename the file
    if [ -f "$old_file" ]; then
        mv "$old_file" "$new_file"
        echo "Renamed $old_file to $new_file"
    else
        echo "File $old_file not found, skipping..."
    fi
done