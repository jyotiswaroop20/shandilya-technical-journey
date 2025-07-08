#!/bin/bash

# ✅ Check: Directory argument दिया गया या नहीं
if [ -z "$1" ]; then
    echo "❌ Error: Please provide a target directory to organize."
    echo "Usage: $0 /path/to/directory"
    exit 1
fi

TARGET_DIR="$1"

# ✅ Directory valid है या नहीं
if [ ! -d "$TARGET_DIR" ]; then
    echo "❌ Error: '$TARGET_DIR' is not a valid directory."
    exit 2
fi

cd "$TARGET_DIR" || exit 3

# 🎯 Target folders
DOC_DIR="Documents"
IMG_DIR="Images"
SCR_DIR="Scripts"
OTH_DIR="Others"
LOG_FILE="organizer.log"

mkdir -p "$DOC_DIR" "$IMG_DIR" "$SCR_DIR" "$OTH_DIR"

# 📒 Logging function
log_move() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') Moved $1 to $2" >> "$LOG_FILE"
}

# 🔁 Move function
move_files() {
    pattern=$1
    target=$2

    shopt -s nullglob
    for file in $pattern; do
        if [ -f "$file" ]; then
            mv "$file" "$target/"
            log_move "$file" "$target"
        fi
    done
    shopt -u nullglob
}

# 📂 Known types
move_files "*.txt" "$DOC_DIR"
move_files "*.pdf" "$DOC_DIR"
move_files "*.jpg" "$IMG_DIR"
move_files "*.png" "$IMG_DIR"
move_files "*.sh"  "$SCR_DIR"

# ⚠️ Unknown types → Others/
shopt -s nullglob
for file in *.*; do
    ext="${file##*.}"
    if [[ "$ext" != "txt" && "$ext" != "pdf" && "$ext" != "jpg" && "$ext" != "png" && "$ext" != "sh" ]]; then
        if [ -f "$file" ]; then
            mv "$file" "$OTH_DIR/"
            log_move "$file" "$OTH_DIR"
        fi
    fi
done
shopt -u nullglob

echo -e "\n✅ File organization complete in '$TARGET_DIR'. Check $LOG_FILE for details."
