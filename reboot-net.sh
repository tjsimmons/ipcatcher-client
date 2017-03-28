#!/bin/bash

ping -c 5 google.com

retval=$?

echo $retval

if [ $retval -eq 0 ]; then
    echo 0 > offline_count.txt
else
    offline=`cat offline_count.txt`
    new_offline=$((offline + 1))

    echo $new_offline > offline_count.txt

    if [ $new_offline -gt 5 ]; then
	touch rebooted.txt
        reboot
    fi
fi