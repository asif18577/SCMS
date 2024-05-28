# Artifact
SCMS - Secure Centralized Management System – Management Platform for Home Network Devices

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
- Once the devices are detected it will show up in Zabbix portal
  
SUTMS - Security Module
- Perform an NMAP scan using "nmap.sh" Script
- Run Custom scripts as shown in files according to the OS i.e. microsoft.sh, linux.sh etc.
- Verify the results by running "root@scms:/home/scms# more medium_risk", "root@scms:/home/scms# more high_risk", "root@scms:/home/scms# more low_risk"
- Merge the files by running the following command "root@scms:/home/scms# cat low_risk medium_risk high_risk >scms_scan_result
- Verify the content of the file "scms_scan_result", it should look like the sample file " scms_scan_result"

SUTMS - Cloud Integration 
- Microsoft Azure Blob storage has to be configured according to the template "azcopy_template". Make sure to change allowed IP addresses according to your public IP's.
- Run the "scms_azure_transfer.sh" script to upload the file to Azure blob storage.
- Automate the above tasks by adding the entries listed in "scms_cronjobs" file.
- Access the storage via Azure mobile app or webui, review the logs and make sure the file is getting updated

