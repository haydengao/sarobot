#! /bin/bash

#echo "CPU name: `cat /proc/cpuinfo |grep "model name" |awk -F ":" '{print $2}'`"

echo "system load average: `uptime |awk -F ":" '{print $5}'`"
echo "DISK status:" `df -h|sed '1d;/ /!N;s/\n//;s/ \+/ /;' |grep -v "tmpfs" |grep -v "udev" |awk '{print $6,"\t",$2,"\t",$3,"\t",$4,"\t",$5}' |awk '!a[$0]++'`

echo "mem status: `free -m | head -2 |tail -1 |awk '{print $2}'` `free -m | head -2 |tail -1 |awk '{print $3}'` `free -m | head -2 |tail -1 |awk '{print $4}'`"
