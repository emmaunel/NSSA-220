ls -LR /etc > /tmp/output 2> /tmp/error

cat /tmp/error | awk '{print $5}' | tail -n +2 | tr -d ':'
#use head to remove the head