#!/usr/bin/env bash
set -e

export $(cat dev.env | xargs)

source python3_venv/bin/activate
python run.py