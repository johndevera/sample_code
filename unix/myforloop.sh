count=1
echo "Enter a number"
read target
while [ $count -le target ]
do
echo $count
count=$((count+1))
done

