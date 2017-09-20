#!/bin/bash
if [[ "$1" == "TAKE_OFF" ]]; then
  ./set_pose.sh 0.92 3.92 0 0
elif [[ "$1" == "POLES" ]]; then
  ./set_pose.sh 5.12 4.80 0 0
elif [[ "$1" == "VEGETATION" ]]; then
  ./set_pose.sh 0 0 0.5 0
elif [[ "$1" == "FANS" ]]; then
  ./set_pose.sh 0 0 0.5 0
elif [[ "$1" == "QR" ]]; then
  ./set_pose.sh 0 0 0.5 0
fi
