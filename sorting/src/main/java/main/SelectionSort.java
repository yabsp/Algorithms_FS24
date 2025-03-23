package main;

// comparison based
// running time: O(n^2)
// not stable
// space: O(1)
public class SelectionSort {

  int[] array;
  int n;

  public SelectionSort(int[] array) {
    this.array = array;
    this.n = array.length - 1;
  }

  public void sort(){
    for(int i = 0; i <= n; i++){
      int min = i;
      for(int j = i+1; j <= n; j++){
        if(array[j] < array[min])
          min = j;
      }
      int temp = array[i];
      array[i] = array[min];
      array[min] = temp;
    }

  }
}