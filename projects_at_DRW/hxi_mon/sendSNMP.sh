#!/bin/bash

MAC='00:18:31:91:83:82'
IP='192.168.1.110'

loop=1
#while [ $loop -eq 1 ]; do
	RSSI=100
	TEMP=31
	VOL=$((6500 + RANDOM % 500))
	CURR=$((1600 + RANDOM % 30))
	MMW=$((RANDOM % 2))
	NET=$((RANDOM % 2))
	data="$MAC $RSSI $TEMP $VOL $CURR $MMW $NET"
	echo "$data"
#	snmptrap -v1 -c K3nP@c#1 192.95.66.74 1.2 '' '' '' 3 1 s "$data"
#	sleep 1
#done

