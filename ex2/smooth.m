function props = smooth(PF, PB)
tem2 = [];                 % initiate tem2
for i = 1:2:length(PF)*2   % go trough the matrix, 2 steps at the time
    tem = [PF(i); PF(i+1)] * [PB(i) PB(i+1)]; % calculate value
    a = 1/(tem(1) + tem(4));  % calculate a to make probability 1
    tem2 = [tem2 [tem(1)*a; tem(4)*a]]; % add a, and add to tem2
end
props = tem2; % return tem2, witch hold all the smooth values