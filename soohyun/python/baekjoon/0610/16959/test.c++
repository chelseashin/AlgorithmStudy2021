#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <tuple>
#include <cstring>
#include <fstream>
#include <iostream>
#include <string>

using namespace std;

#define MAX 101

void string_format(char * str, char * buf, int size)
{
    for (int i=0; i<size; i++)
        buf[i] = ' '; // initialize the string with spaces

    int x = 0;
    while (str[x])
    {
        if (x >= size) break;
        buf[x] = str[x]; // fill up the string
    }

    buf[size-1] = 0; // termination char
}

int main()
{   int n;
    int N = 0;
    int *arr;
    int *new_arr;
    int sorting = 0;
    string filePath = "";
    cin >> n;
    N = n*n;
    arr = new int[N];
    new_arr = new int[N];


    for(int i = 0; i < N; i++){
        arr[i] = i+1;
    }
    printf("%d", n);
        for(int i = 0; i < N; i++){
            if (i % (n) == 0){
                printf("%s", "\n");
            }
            printf("%d ", arr[i]);
        }
        printf("\n");
    
    while(std::next_permutation(arr, arr+N)){
        filePath = string_format("in/%d.txt", sorting);
        ofstream writeFile(filePath.data());

        if (writeFile.is_open()){
            for(int i = 0;i<N;i++){
                new_arr[i] = arr[i];
            }
            //printf("%d", n);
            writeFile << string_format("%d", n);
            for(int i = 0; i < N; i++){
                if (i % (n) == 0){
                    writeFile << string_format("%s", "\n");
                    printf("%s", "\n");
                }
                printf("%d ", new_arr[i]);
                writeFile << string_format("%d ", new_arr[i]);
            }
            printf("\n");
        }
        sorting++;

            // printf("%d ",arr[i]); 
    }

    

}