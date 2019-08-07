#! /bin/bash

echo "Cleaning out /tmp/results"
rm -f /tmp/results/*

echo "Killing old nvmf_targets"
pkill -9 -f nvmf_tgt
sleep 3;

echo "Launching run_nvmf.py"
python3 scripts/perf/nvmf/run_nvmf.py
