#!/bin/bash

if [[ "$1" == "TAKE_OFF" ]]; then
  ./set_pose.sh 0.92 3.92 0 0
elif [[ "$1" == "POLES" ]]; then
  ./set_pose.sh 5.12 6.7 0 0
elif [[ "$1" == "VEGETATION" ]]; then
  ./set_pose.sh 10.91 10.47 0 0
elif [[ "$1" == "QR" ]]; then
  ./set_pose.sh 12.79 5.3 0 0
fi
