#!/usr/bin/bash

read -p "enter a number: " m
if [ $((m%2)) -eq 0 ]
then
	echo "Weird"
elif [ $((m%2)) -ne 0 ]
then
       if [[ $m -ge 2 ]] && [[ $m -le 5 ]]
       then
       	       echo "Not Weird"
       elif [[ $m -ge 6 ]] && [[ $m -le 20 ]]
       then
	       echo "Weird"
       elif [[ $m -gt 20 ]]
       then
	       echo "Not Weird"
       fi
fi
