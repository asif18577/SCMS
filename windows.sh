grep -E -i ’192.168.*.*| windows’ scms_scan.xml
>microsoft_scan ; sed ’/ˆNmap/ s/$/ *** Score=5,
Risk=Medium *** /’ microsoft_scan> medium_risk
