#until loop in action
count=1
echo "type in a number"
read stop
until [ $count -ge $stop ]
do
	echo $count
	count=$((count + 1))
done
 
