#! /bin/bash

echo "Cleaning out /tmp/results"
rm -f /tmp/results/*

echo "Disconnecting any initiators"
python3 scripts/perf/nvmf/disconnect_initiators.py

echo "Killing old nvmf_targets"
pkill -9 -f nvmf_tgt
sleep 3;

echo "Launching setup_nvmf_target_initators.py"
python3 scripts/perf/nvmf/setup_nvmf_target_initators.py

#echo "Launching HTTP JSON Proxy"
#IP=172.20.8.1
#./scripts/rpc_http_proxy.py ${IP} 8000 user password
