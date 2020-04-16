%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Alexa Kelly
%
% % Eulers problem 9
% Program: E9.m
% Purpose: There exists exactly one Pythagorean triplet for which a+b+c =1000.
% Find the product abc.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

ai= 333 ;
bi= 499 ;

flag= true;
while flag== true
for i= 1:ai
    for j= 1:bi
        c= (i^2 + j^2)^.5 ; 
            if i+j+c==1000
                solution= i*j*c ;
               flag =false;
            end
    end
end
end 
fprintf('The solution to Eulers problem 9: %8.0f \n', solution)