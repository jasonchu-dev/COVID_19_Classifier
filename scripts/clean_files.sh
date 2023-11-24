#!/bin/bash

models="../models"
__pycache__="../src/__pycache__"
reports="../reports"

delete_folders() {
    local folder="$1"
    if [ -d "$folder" ]; then
        rm -r "$folder"
        echo "$folder deleted"
    else
        echo "$folder not found"
    fi
}

delete_folders "$models"
delete_folders "$reports"
delete_folders "$__pycache__"