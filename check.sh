
#!/bin/bash
time=$(date "+%Y-%m-%d %H-%M-%S")
/usr/bin/python3 /test/upload_status.py >/test/log/upload_status.log
num1=`ps -ef | grep -w /test/upload_sum_info.py |grep -v grep | tr -s ' ' | awk -F' ' '{print $2}'`
if [ $num1 ];
then
echo "upload_sum_info is runing,$time and this pid=$num1">/test/log/runing.log
else
nohup /usr/bin/python3 /test/upload_sum_info.py &
echo "/test/upload_sum_info.py is start $time">/test/log/start.log
fi
