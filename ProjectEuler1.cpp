/* 
 * File:   main.cpp
 * Author: sonyakhan
 *
 * Created on January 30, 2015, 2:28 PM
 */

#include <cstdlib>
#include <iostream>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    
    
    int sum = 0;
    int count = 999;
    while (count>=0)   
    {
        while (count%3==0 || count%5==0)
        {
            sum = sum + count;
            count--;
            }
        count--;
    }
    cout << sum;
    return 0;
}

