grep -E -i ’192.168.*.*| Apple’ scms_scan.xml >ap-
ple_scan ; sed ’/ˆNmap/ s/$/ *** Score=5, Risk=Medium
*** /’ apple_scan > medium_risk
