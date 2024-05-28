grep -E -i ’192.168.*.*| linux’ scms_scan.xml
>linux_scan ; sed ’/ˆNmap/ s/$/ *** Score=5,
Risk=Medium *** /’ linus_scan> medium_risk
