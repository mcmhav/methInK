function props = ba(T,  O,  S)
temp = T*O*S;               % calculate the value of the functions
a = 1/(temp(1) + temp(2));  % find a to make the probability 1
props = temp*a;             % multiply by a