#include <cstdlib>
#include <iostream>


int main(int argc, char** argv) {

int fib;
int sum = 0;

for (x=1; x<=4000000; x++)
{
	fib = x + (x+1);
	while (fib%2==0)
	{
		sum+=fib;
	}

	cout << sum;
}


return 0; 
}