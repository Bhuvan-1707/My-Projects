#include<iostream>
using namespace std;
int main(){
    int arr[] = {5,2,3,1,4,6};
    int* curr;
    int* next;
    int temp;
    for(int i=0;i<6;i++){
        std::cout<<arr[i]<<" ";
    }
    std::cout<<"\n";
    for(int i=0;i<6-1;i++){
        for(int j=0;j<6-i-1;j++){
            curr = &arr[j];
            next = &arr[j+1];
            if(*curr>*next){
                temp = *next;
                *next = *curr;
                *curr = temp;

            }
        }
    }
    for(int i=0;i<6;i++){
        std::cout<<arr[i]<<" ";
    }
}