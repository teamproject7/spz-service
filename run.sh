#!/usr/bin/env bash

set -e
export $(cat .env | xargs)
/home/michal/anaconda3/bin/python run.py