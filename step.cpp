#include <iostream>
//step.cpp(C++'s step.c)

long double step_add(long double max)  //max must be float
{	
 	long double j=0.0; //define j
 	for (long double i=0.0;i<max+1;i+=1)  //a easy for loop
 	{
 		j+=i;  //Plus
 	}
 	
 	return j;  //return j
}


int main()
{
	return 0;
}
