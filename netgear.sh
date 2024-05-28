grep -E -i ’192.168.*.*| netgear’ scms_scan.xml >net-
gear_scan ; sed ’/ˆ Nmap/ s/$/ *** Score=7, Risk=Low
*** /’ cisco_scan > low_risk
