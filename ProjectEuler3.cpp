/* 
 * File:   main.cpp
 * Author: sonyakhan
 *
 * Created on February 3, 2015, 4:51 PM
 */

#include <cstdlib>
#include <iostream>
#include <math.h>

using namespace std;

/*
 * 
 */

bool isPrime (int a)
{
    
    int b = sqrt(a);
    for (int c = 2; c <= b; c++)
    {
        if (a % c == 0)
        {
            return false;
        }
        if (a== 0 || a== 1 || a== -1)
        {
            return false;
        }
            
        return true; 
    }
}

int main(int argc, char** argv) {
    
    
    long long y = (600851475143)/2;
    int largestNum = -1;
    
    cout << isPrime(1) << endl;
    cout << isPrime(4) << endl;
    cout << isPrime(11) << endl;


    
    for (int x=2; x<=y; x++)
    {
        if (600851475143 % x == 0 && isPrime(x) == true)
        {
            while (x > largestNum)
            {
                largestNum = x;
            }
            
        }
            
    }
    
    cout << largestNum;
    
    return 0;
}

