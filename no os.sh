grep -E -i ’192.168.*.*| No OS matches’ scms_scan.xml
>undetected_OS_scan ; sed ’/ˆNmap/ s/$/ *** Score=1,
Risk=High (NO OS DETECTECD) *** /’ undetected_OS_scan
> high_risk
