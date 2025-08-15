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

    return 0;
}
