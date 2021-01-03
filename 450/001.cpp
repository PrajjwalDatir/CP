#include <iostream>
using namespace std;

void printArray(int arr[], int SIZE){
  for (int i=0; i<SIZE; i++){
    cout << arr[i] << ",";
  }
  cout << endl;
  return;
}

void reverseArray(int arr[], int start, int end){
  while (start < end)
  {
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start ++;
    end --;
  }

  return;
}


int main()
{
  int process[] = {1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10};
  int SIZE = sizeof(process)/sizeof(process[0]);
  printArray(process, SIZE);

  reverseArray(process, 0, SIZE - 1);

  printArray(process, SIZE);

// code



  return 0;

}