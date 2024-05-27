# Artifact
SCMA - Secure Centralized Management System – Management Platform for Home Network Devices

## Features

- Inventory Module - Automatic discover devices in a home networks. Customize alerting and system resource monitoring. 
- Security Module - Categorizing the devices according to risk level
- Cloud Module -  Data accesssible from anywhere and anytime via utlizing Microsoft Azure API.

## Installation

- Install Ubuntu 22.04 LTS available on https://ubuntu.com/download/desktop/thank-you?version=22.04.4&architecture=amd64
- Install Zabbix 5.0.31 - https://www.zabbix.com/rn/rn5.0.31
- Install NMAP - https://nmap.org/download
- Install Azurecopy - https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#download-azcopy

## Usage
One the required softwares are installed as listed in installation instructions, perform the following tasks.
SUTMS - Inventory Module 
- Configure Zabbix to detect devices automatically by performing SNMP walk, ping sweeps. 
- Detect devices by using SNMP strings or by install Zabbix device agent.
- Once the devices are detetected it will show up in Zabbix portal
  
SUTMS - IDS Module according to application detection
- Download the latest SUTMS rules by executing "sudo suricata-update".
- Learn the protocols in use via NTOP engine.
- Run the python script (sutms_suricate.py) to only enable the relevant signatures. (please select the protocols according to your environment)
- Automate the above tasks by adding the entries listed in "sutms_cronjobs" file.
- Review the logs and make sure for neccessary hits

SUTMS - Anomaly detection
- NTOP can be used to detect anomalies, certain use cases are include in "ntop_lua" file.

