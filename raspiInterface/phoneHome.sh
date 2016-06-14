#! /bin/bash
iwconfig wlan1 mode Ad-hoc
iwconfig wlan1 essid RasPiFi

ifconfig wlan1 192.168.1.1 netmask 255.255.255.0
