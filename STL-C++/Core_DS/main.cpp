#include <iostream>
#include "include/DynamicArray.hpp"

int main() {
    DynamicArray<int> arr;

    // Test addEnd
    for(int i = 1; i <= 10; i++)
        arr.addEnd(i);

    std::cout << "Array contents after addEnd: ";
    for(int i = 0; i < arr.getSize(); i++)
        std::cout << arr[i] << " ";
    std::cout << "\nSize: " << arr.getSize() << ", Capacity: " << arr.getCapacity() << "\n";

    // Test insert
    arr.insert(5, 99);
    std::cout << "After insert 99 at index 5: ";
    for(int i = 0; i < arr.getSize(); i++)
        std::cout << arr[i] << " ";
    std::cout << "\n";

    // Test remove
    arr.remove(2);
    std::cout << "After removing index 2: ";
    for(int i = 0; i < arr.getSize(); i++)
        std::cout << arr[i] << " ";
    std::cout << "\n";

    // Test removeEnd
    arr.removeEnd();
    std::cout << "After removeEnd: ";
    for(int i = 0; i < arr.getSize(); i++)
        std::cout << arr[i] << " ";
    std::cout << "\n";

    // Test copy constructor
    DynamicArray<int> arr2 = arr;
    arr2.addEnd(555);
    std::cout << "Copy constructor test: ";
    for(int i = 0; i < arr2.getSize(); i++)
        std::cout << arr2[i] << " ";
    std::cout << "\n";

    // Test assignment operator
    DynamicArray<int> arr3;
    arr3 = arr2;
    std::cout << "Assignment operator test: ";
    for(int i = 0; i < arr3.getSize(); i++)
        std::cout << arr3[i] << " ";
    std::cout << "\n";

    // Show method testing
    std::cout << "Show Method test: ";
    arr3.show();

    // Shrinktofit method testing
    std::cout << "Shrink To Fit Method test: ";
    arr3.shrinkToFit();
    std::cout<<arr3.getSize()<<" "<<arr3.getCapacity()<<std::endl;

    // Front and back testing method
    std::cout<<"Front: "<<arr3.front()<<" "<<"Back: "<<arr3.back()<<std::endl;

    // at and find method testing
    std::cout<<"At 5 is : "<<arr3.at(5)<<std::endl;
    size_t index;
    arr3.find(2,index);
    std::cout<<"Find 2 is : "<<index<<std::endl;

    // Clear method testing
    arr2.clear();
    arr2.addEnd(5);
    arr2.addEnd(2);
    arr2.addEnd(3);
    arr2.addEnd(5);
    arr2.show();
    std::cout<<"Count of 5 in arr2 : "<<arr2.count(5)<<std::endl;
    std::cout<<"Is 3 there in arr2 : "<<arr2.contains(3)<<std::endl;

    // Testing Bubble sort
    std::cout<<"Array 3 before bubble sort : ";
    arr3.show();
    arr3.sortbubble();
    std::cout<<"Array 3 after bubble sort : ";
    arr3.show();

    return 0;
}