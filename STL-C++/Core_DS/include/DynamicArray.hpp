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


        void addEnd(T value);
        bool removeEnd();
        bool insert(size_t index, T value);
        bool remove(size_t index);
        void show();
        T& front();
        T& back();
        T& at(size_t index);
        bool find(T element,size_t& index);
        int count(T element);
        bool contains(T element);

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