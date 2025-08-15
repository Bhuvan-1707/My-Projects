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
        
        T& operator[](size_t index);
        int getSize();
        int getCapacity();
        bool isEmpty();
};

#endif