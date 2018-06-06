#while loop in action
count=1
echo "Enter in a number"
read stop
while [ "$count" -le "$stop" ]
do
	if [ grep 7 count ]
	then
	echo "fizz"
	fi

	if [ grep 3 count ]
	then
	echo "buzz"
	fi
	
	echo $count
	count=$((count + 1))
done

