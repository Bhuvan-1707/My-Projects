#include <iostream>
#include "Core_DS/include/DynamicArray.hpp"

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

    std::cout << "=== Testing Move Constructor ===\n";

    DynamicArray<int> a(5);
    a.addEnd(10);
    a.addEnd(20);
    a.addEnd(30);

    std::cout << "Original a: ";
    a.show();

    // Use move constructor
    DynamicArray<int> b = std::move(a);

    std::cout << "After moving, b: ";
    b.show();

    std::cout << "After moving, a (should be empty): ";
    a.show();


    std::cout << "\n=== Testing Move Assignment ===\n";

    DynamicArray<int> c(5);
    c.addEnd(100);
    c.addEnd(200);

    DynamicArray<int> d(5);
    d.addEnd(1);
    d.addEnd(2);
    d.addEnd(3);

    std::cout << "Before move assignment, c: ";
    c.show();

    std::cout << "Before move assignment, d: ";
    d.show();

    // Move assignment
    c = std::move(d);

    std::cout << "After c = std::move(d), c: ";
    c.show();

    std::cout << "After move, d (should be empty): ";
    d.show();

    std::cout << "=== Testing reserve() ===\n";

    DynamicArray<int> resarr(5);
    resarr.addEnd(10);
    resarr.addEnd(20);
    resarr.addEnd(30);

    std::cout << "Before reserve:\n";
    std::cout << "Size: " << resarr.getSize() << "\n";
    std::cout << "Capacity: " << resarr.getCapacity() << "\n";
    resarr.show();

    // Test 1: Increase capacity
    resarr.reserve(20);
    std::cout << "\nAfter reserve(20):\n";
    std::cout << "Size: " << resarr.getSize() << " (should stay 3)\n";
    std::cout << "Capacity: " << resarr.getCapacity() << " (should become 20)\n";
    resarr.show();  // should still print 10 20 30

    // Test 2: Reserve smaller than current capacity (should do nothing)
    resarr.reserve(10);
    std::cout << "\nAfter reserve(10) [should not change]:\n";
    std::cout << "Size: " << resarr.getSize() << "\n";
    std::cout << "Capacity: " << resarr.getCapacity() << " (should still be 20)\n";
    resarr.show();  // still 10 20 30

    return 0;
}
