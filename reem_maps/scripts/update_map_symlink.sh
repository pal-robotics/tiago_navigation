#! /bin/sh
#
# Update the reem_maps/config symlink to point to the map that is
# currently being used.

set -e

# Check parameters
if [ $# -lt 2 ]; then
  echo "Usage: $0 <symlink path> <map path> [ROS args...]"
  echo "Updates the symlink to point to the given path."
  exit 1
fi

# Ensure target directory exists
if [ ! -d "$2" ]; then
  echo "Error: Target path is not a directory: $2"
  exit 3
fi

# Ensure we are not creating a recursive symlink
# This is important since often reem_maps/config may be used as path.
abspath() {
  (cd "${1%/*}" &>/dev/null && echo "$(pwd)/${1##*/}")
}
if [ "`abspath $1`" = "`abspath $2`" ]; then
  echo "Warning: Same path given for symlink and map directory. Doing nothing."
  exit 0
fi

# Remove the previous symlink, if any.
if [ -e "$1" ]; then
  if [ ! -h "$1" ]; then
    echo "Error: Path is not a symlink: $1"
    exit 2
  fi
  unlink "$1"
fi

# Create the new symlink!
ln -s "$2" "$1"
echo "Done."
