// Buble sort in C++

#include <iostream>
using namespace std;

// perform buble sort
void bubbleSort(int array[], int size) {

  // loop to compare aray element
  for (int step = 0; step < size -1; ++step) {

    // loop to compare array elements
    for (int i = 0; i < size - 1; ++i) {

      // compare two adjacent elements
      // change > to < to sort descending order
      if (array[i] > array[i + 1]){

        // swapping elements if elements
        //  are not in the intended order
        int temp = array[i];
        array[i] = array[i + 1];
        array[i + 1] = temp;
      }
    }
  }  
}

// print array
void printArray(int array[], int size) {
  for (int i = 0; i < size; ++i) {
    cout << " " << array[i];
  }
  cout << "\n";
}

int main() {
  int data[] = {-2, 45, 0, 11, -9};

  // find array's length
  int size = sizeof(data) / sizeof(data[0]);

  bubbleSort(data, size);

  cout << "Sorted Array in Ascending order;\n";
  printArray(data, size);
}

