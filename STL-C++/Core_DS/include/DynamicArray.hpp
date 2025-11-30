#ifndef DYNAMIC_ARRAY_H
#define DYNAMIC_ARRAY_H

template <class T>
class DynamicArray{
    private:
        size_t size;
        size_t capacity;
        T* data;

        void resize(size_t cap);
    public:
        // Default Constructor
        DynamicArray();
        // Parameterized constructor
        DynamicArray(size_t c);
        // Destructor
        ~DynamicArray();
        // Copy constructor
        DynamicArray(const DynamicArray& other);            
        // Copy Assignment constructor
        DynamicArray& operator=(const DynamicArray& other);
        // Move constructor
        DynamicArray(DynamicArray&& other) noexcept;
        // Move Assignment Operator
        DynamicArray& operator=(DynamicArray&& other) noexcept;


        void addEnd(T value); // Add an element at the end
        bool removeEnd(); // Remove an element at the end
        bool insert(size_t index, T value); // Insert an element at the index
        bool remove(size_t index); // Remove an element from the index
        void show(); // Show the dynamic array
        T& front(); // Return the first element
        T& back(); // Return the last element
        T& at(size_t index); // Return the element at the index
        bool find(T element,size_t& index); // Find the element and return the index using args
        int count(T element); // Count of the elements
        bool contains(T element); // If element present return true else false
        void reserve(size_t new_capacity);
        void sortbubble(); // Bubble sort of the DA

        // Capacity and properties
        T& operator[](size_t index); // Index accessing operator "[]"
        int getSize(); // Get Size of the DynamicArray
        int getCapacity(); // Get the Max Capacity of the Dynamic Array
        bool isEmpty(); // Whether the DA is empty or not
        void shrinkToFit(); // Whenever u need no more insertions,... use this - but still insertions will work
        void clear(); // Clear the array with keeping the capacity same

};

#include "../src/DynamicArray.tpp"

#endif