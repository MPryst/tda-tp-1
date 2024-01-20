#!/bin/bash

#from 500k to 25M step 500k
for i in {500000..25000000..500000}
do
  python3 generador.py $i 2000 $1 >| ./data/$i.dat  
  echo Generated the file $i.dat under ./data
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

