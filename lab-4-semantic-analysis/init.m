#1 OK
A = 2;

#2 OK
A = B;

#3 OK
C += A;

#4 OK
D = zeros(2.5);
D = ones(K);
D = eye(A);

#5 OK
E = 2;
E += eye(1);
E -= 1;

#6 OK
F = [1,2,3;
	 3,4,5,6];

F = [1,2;
     3,4];


#7 OK
H = F[9,2,3];
H = F[1,A];
H = F[9,0];