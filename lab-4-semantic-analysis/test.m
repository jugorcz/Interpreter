
a = 0;
b = 1;
a = b;

# uminus
c = -b;

# transposition
A = [1, 3];
B = A';
B = a';

# comparission OK
if (a <= b) {

}

# comparission not OK
if (A <= A) {
    
}

# zeros
M = zeros(3.14);
M = zeros(3);

# bin op
b = a + 2;

# dot bin op
A += A;

# range
for i = 1.10 : 10 {

}

while (1 < 2) {
    if (a <= b) {
        a = a';
        a = [1];
        break;
    }
}

break;

F = [1,2,3;
	 3,4,5,6];


F = [1,2,3;
	 3,4,5];

print a, b, c;
