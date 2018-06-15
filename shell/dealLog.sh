#!/bin/sh
#目录下a.log 有10w行，希望统计其中出现的log种类个数，按照日期统计：

time1=`cat ./a.log | awk '{print $1}' | uniq`
#echo $time1
for item in $time1;
do
    #echo $item
    item_with_exc=`cat ./a.log | grep $item`
    num=`cat ./a.log | grep $item | grep "${item_with_exc:15}" | wc -l`
    if [ $num ];then
        echo "$item $num ${item_with_exc:15}"
    fi
done