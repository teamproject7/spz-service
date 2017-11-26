#!/usr/bin/env bash

set -e
export $(cat dev.env | xargs)
/home/michal/anaconda3/bin/python run.py