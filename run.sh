#!/usr/bin/env bash
set -e

export $(cat .env | xargs)
python run.py