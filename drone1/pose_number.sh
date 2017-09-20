#!/bin/bash

if [[ "$1" == "TAKE_OFF" ]]; then
  ./set_pose.sh 0.92 3.92 0 0
elif [[ "$1" == "POLES" ]]; then
  ./set_pose.sh 5.12 4.80 0 0
elif [[ "$1" == "VEGETATION" ]]; then
  ./set_pose.sh 10.91 9.97 0 0
elif [[ "$1" == "FANS" ]]; then
  ./set_pose.sh 10.91 9.97 0 0
elif [[ "$1" == "QR" ]]; then
  ./set_pose.sh 13.64 5.45 0 0
fi
