str = "0 0 1 0 1 0 1 0 0 0; 0 0 1 0 1 0 0 0 0 0; 0 0 1 0 0 0 1 1 0 0; 0 0 1 0 0 0 0 0 0 0; 0 0 0 0 0 0 0 0 0 0; 0 0 0 0 0 1 0 1 0 0; 0 1 0 0 0 1 0 1 0 0; 0 0 0 0 0 1 0 1 0 0; 0 1 0 0 0 0 0 0 0 1; 0 1 0 0 1 0 0 0 0 0;"

i = 12
str = str[:i] + '0' + str[i+1:] 
print(str)