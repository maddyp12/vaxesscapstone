#!/bin/bash

filename=$1
folder=$2

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "File $filename not found!"
    exit 1
fi

for file in "$folder"/*.csv; do
    python3 $filename $file
done