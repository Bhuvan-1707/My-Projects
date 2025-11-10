#include<iostream>
#include<stdexcept>
#include "../include/DynamicArray.hpp"

template <class T>
DynamicArray<T>::DynamicArray(){
    // Default Constructor
    size=0;
    capacity=64;
    data = new T[capacity];
}

template <class T>
DynamicArray<T>::DynamicArray(size_t c){
    // Capacity based Constructor
    size=0;
    capacity=c;
    data = new T[capacity];
}

template <class T>
DynamicArray<T>::~DynamicArray(){
    // Destructor
    delete[] data;
};

template <class T>
DynamicArray<T>::DynamicArray(const DynamicArray& other){
    // Copying other variables of the Dynamic Array
    this->size = other.size;
    this->capacity = other.capacity;
    data = new T[capacity];

    // Copying all the elements from other to this constructed variable
    for(size_t i=0;i<size;i++){
        this->data[i] = other.data[i];
    }
}

template <class T>
DynamicArray<T>& DynamicArray<T>::operator=(const DynamicArray& other){
    // Copying other variables of the Dynamic Array
    this->size = other.size;
    this->capacity = other.capacity;
    delete[] data;
    data = new T[capacity];

    // Copying all the elements from other to this constructed variable
    for(size_t i=0;i<size;i++){
        this->data[i] = other.data[i];
    }
    return *this;
}

template <class T>
void DynamicArray<T>::resize(size_t cap){
    T* newdata = new T[cap];
    for(size_t i=0;i<size;i++){
        newdata[i] = data[i];
    }
    delete[] data;
    data = newdata;
    capacity = cap;
}

template <class T>
void DynamicArray<T>::addEnd(T value){
    // If the capacity is insufficient, increase the capacity by half
    if(size==capacity){
        resize(capacity/2 + capacity);
    }
    data[size++] = value;
}

template <class T>
bool DynamicArray<T>::removeEnd(){
    if(size<=0){
        return false;
    }
    data[size-1] = T();
    size--;
    return true;
}

template <class T>
bool DynamicArray<T>::insert(size_t index,T value){
    if(index > size){
        return false;
    }
    else if(index==size){
        addEnd(value);
        return true;
    }
    if(size==capacity){
        resize(capacity + capacity/2);
    }
    size++;
    for(size_t i=size;i>index;i--){
        data[i] = data[i-1];
    }
    data[index]=value;
    return true;
}

template <class T>
bool DynamicArray<T>::remove(size_t index){
    if(index>=size){
        return false;
    }
    for(size_t i=index;i<size-1;i++){
        data[i] = data[i+1];
    }
    size--;
    return true;
}

template<class T>
T& DynamicArray<T>::operator[](size_t index){
    if(index>=size){throw std::out_of_range("Index out of bounds in DynamicArray");}
    return data[index];
}

template <class T>
int DynamicArray<T>::getSize(){
    return size;
}

template <class T>
int DynamicArray<T>::getCapacity(){
    return capacity;
}

template <class T>
bool DynamicArray<T>::isEmpty(){
    return size==0;
}

template <class T>
void DynamicArray<T>::show(){
    for(size_t i=0;i<size;i++){
        std::cout<<data[i]<<" ";
    }
    std::cout<<std::endl;
}

template <class T>
void DynamicArray<T>::shrinkToFit(){
    resize(size);
}

template <class T>
T& DynamicArray<T>::front(){
    if (isEmpty()) {
        throw std::out_of_range("DynamicArray is empty: no last element");
    }
    return *(data+0);
}

template <class T>
T& DynamicArray<T>::back(){
    if (isEmpty()) {
        throw std::out_of_range("DynamicArray is empty: no last element");
    }
    return *(data+size-1);
}

template <class T>
T& DynamicArray<T>::at(size_t index){
    if(index>=size){throw std::out_of_range("Index out of bounds in DynamicArray");}
    return data[index];
}

template <class T>
bool DynamicArray<T>::find(T element,size_t& index){
    for(int i=0;i<size;i++){
        if(element == data[i]){
            index= i;
            return true;
        }
    }
    return false;
}

template <class T>
void DynamicArray<T>::clear(){
    size = 0;
}

template <class T>
int DynamicArray<T>::count(T element){
    int count=0;
    for(size_t i=0;i<size;i++){
        if(data[i]==element){
            count++;
        }
    }
    return count;
}

template <class T>
bool DynamicArray<T>::contains(T element){
    if(count(element)<=0){
        return false;
    }
    return true;
}

template <class T>
void DynamicArray<T>::sortbubble(){
    int* curr;
    int* next;
    int temp;
    for(int i=0;i<size-1;i++){
        for(int j=0;j<size-i-1;j++){
            curr = &data[j];
            next = &data[j+1];
            if(*curr>*next){
                temp = *next;
                *next = *curr;
                *curr = temp;
            }
        }
    }
}
