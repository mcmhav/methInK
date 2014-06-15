O = [0.9 0.0; 0.0 0.2];   % Observed umbrella true
O2 = [0.1 0.0; 0.0 0.8];  % Observed umbrella false

T = [0.7 0.3; 0.3 0.7];   % Transition probabilities

farr = [0.5 ;0.5];        % start condition forward 
barr = [1;1];             % start condition backward

% Here the "fa" function is called for each day
% "fa" computes forward probabilities
farr = [farr fa(O, T, [farr(end-1); farr(end)])]; 
farr = [farr fa(O, T, [farr(end-1); farr(end)])];
farr = [farr fa(O2, T, [farr(end-1); farr(end)])];
farr = [farr fa(O, T, [farr(end-1); farr(end)])];
farr = [farr fa(O, T, [farr(end-1); farr(end)])];

farr % print farr

% Here the "ba" function is called for each day
% "ba" computes backward probabilities
barr = [barr ba(T, O, [barr(end -1); barr(end)])];
barr = [barr ba(T, O, [barr(end -1); barr(end)])];
barr = [barr ba(T, O2, [barr(end -1); barr(end)])];
barr = [barr ba(T, O, [barr(end -1); barr(end)])];
barr = [barr ba(T, O, [barr(end -1); barr(end)])];

barr % print barr

smbarr = fliplr(barr); % flip the barr so it is easier to smooth

temp3 = smooth(farr, smbarr); % call "smooth" on farr and barr(fliped)
temp3 % print the smooth probabilities