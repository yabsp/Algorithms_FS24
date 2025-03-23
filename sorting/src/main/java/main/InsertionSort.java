package main;

// comparison-based
// running time: best/average/worst; O(n)/O(n^2)/O(n^2)
// stable
// space: O(1)
public class InsertionSort {

  private int[] array;
  private int n;

  public InsertionSort(int[] array) {
    this.array = array;
    this.n = array.length;
  }

  public void sort() {
    for (int i = 1; i < n; i++) {
      int j = i;
      while (j > 0 && array[j - 1] > array[j]) {
        int temp = array[j - 1];
        array[j - 1] = array[j];
        array[j] = temp;
        j--;
      }
    }
  }
}