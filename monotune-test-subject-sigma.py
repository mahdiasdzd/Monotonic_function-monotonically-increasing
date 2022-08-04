
#step 1 : import panda library for  data analysis
import pandas as pds

 

# step 2 :  input our number sequences

series1 = pds.Series([-1, 1.75, 3.7499, 4.2,7, 9.5]);

series2 = pds.Series([1, 0.75, 0.7499, 0.2, -.5, -2.5]);

 

# step 3 :  setup monotonic algorithm

monoDecr_series1 = series1.is_monotonic_increasing;

monoDecr_series2 = series2.is_monotonic_decreasing;

 
# final step : print results and sort

print("The series:");

print(series1);

print("is monotonically increasing: %s" % monoDecr_series1);

#show the longest monotonically
print("longest monotonically increasing in series1 is:", max(series1));


print("The series:");

print(series2);

print("is monotonically decreasing: %s" % monoDecr_series2);

#show the longest monotonically
print("longest monotonically decreasing in series2 is:", max(series2));


