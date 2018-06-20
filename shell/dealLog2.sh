#/bin/sh
exc_type=`awk -F " " '{for(i=3;i<=NF;i++)printf("%s ",$i);print ""}' a.log`
for item in $exc_type;
  do
    echo $item
  done



for item in $(cat a.log | awk '{print $1}' | uniq);do echo $item; cat a.log | grep $item | wc -l; cat a.log | grep $item |awk -F " " '{for(i=3;i<=NF;i++)printf("%s ",$i);print "\n"}';done