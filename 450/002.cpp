#include <iostream>
#include<limits.h>
using namespace std;

void printArray(int arr[], int SIZE)
{
  for (int i = 0; i < SIZE; i++)
  {
    cout << arr[i] << ",";
  }
  cout << endl;
  return;
}

void reverseArray(int arr[], int start, int end)
{
  while (start < end)
  {
    int temp = arr[start];
    arr[start] = arr[end];
    arr[end] = temp;
    start++;
    end--;
  }

  return;
}

void minMaxOfArray(int arr[], int SIZE)
{
  int min = INT_MAX, max = INT_MIN;
  for (int i = 0; i < SIZE; i++)
  {
    if (arr[i] < min)
      min = arr[i];
    else if (arr[i] > max)
      max = arr[i];
  }
  cout << "Min: " << min << "\nMax: " << max << endl;
  return;
}

int main()
{
  int process[] = {114, 122, 43, 1254, 635, 366, 747, 88, 59, 810};
  int SIZE = sizeof(process) / sizeof(process[0]);
  printArray(process, SIZE);

  // reverseArray(process, 0, SIZE - 1);
  minMaxOfArray(process, SIZE);
  printArray(process, SIZE);

  return 0;
}