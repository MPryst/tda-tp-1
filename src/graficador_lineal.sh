#!/bin/bash

#from 500k to 25M step 500k
start=25000000
end=1
for (( i=$start; i>=$end; i=i-500000 ))
do
  #create i.dat
  echo "Si,Ai" >| ./data/$i.dat 
  for(( j=$i; j>=$end; j-- ))
  do
    echo $j,$j >> ./data/$i.dat 
  done 
  echo "generated data for $i"
done

echo "x,y" >| ./data/run-results.csv

for i in {500000..25000000..500000}
do
  start_time=$(date +%s%3N)
  echo $i
  #echo $start_time
  python3 algoritmo.py ./data/$i.dat;
  end_time=$(date +%s%3N)
  #echo $end_time
  miliseconds_passed=`expr $end_time - $start_time`
  echo Execution time was `expr $miliseconds_passed` miliseconds.  
  expr $i,$miliseconds_passed >> ./data/run-results.csv
done

