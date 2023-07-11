# import bad_hello and good_hello functions

# the print(bad_hello("Bad Yann")) is executed while importing bad_hello :( 
from bad_import_lib import bad_hello
# the print(bgood_hello("Bad Yann")) is NOT executed while importing good_hello :)
from good_import_lib import good_hello

# execute bad_hello and good_hello functions
print(bad_hello("Bad World"))
print(good_hello("Good Coders"))