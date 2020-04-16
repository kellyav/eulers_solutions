%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Alexa Kelly
%
% % Eulers problem 10
% Program: E10_short.m
% Purpose: Find the sum of all the primes below two million.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Euler's Problem 10:
% The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
% Find the sum of all the primes below two million.

tic
lop= primes(2000000);       % List of primes from 2 to 1000000. 
sop= cumsum(lop);          % cumsum finds the cummulative sum of elements. aka, sop= (cummulative) sum of primes
L= length(lop);

solution=sop(L);
sprintf('%13.f', solution)

toc

%  this used mostly matlabs commands instead of coding it from scratch. good for comparison.