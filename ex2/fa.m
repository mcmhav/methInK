function props = fa(O,  T,  S)
temp = O*T*S;               % calculate the value of the functions
a = 1/(temp(1) + temp(2));  % find a to make the probability 1
props = temp*a;             % multiply by a