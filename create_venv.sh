# This script simply creates virtual environment using
# your default Python interpreter in a folder called `.venv`.
# NOTE: This is designed for Windows.

# To run this script: ensure you are in the base level of
# this repository, then run the command `./create_venv.sh`
# in a UNIX-compatible terminal such as Git Bash
mkdir .venv
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.in
