#! /bin/bash

echo "Cleaning out /tmp/results"
rm -f /tmp/results/*

echo "Disconnecting any initiators"
python3 scripts/perf/nvmf/disconnect_initiators.py

echo "Killing old nvmf_targets"
pkill -9 -f nvmf_tgt
