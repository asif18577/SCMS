grep -E -i ’192.168.*.*| FreeBSD’ scms_scan.xml
>linux_scan ; sed ’/ˆNmap/ s/$/ *** Score=5,
Risk=Medium *** /’ linux_scan > medium_risk
