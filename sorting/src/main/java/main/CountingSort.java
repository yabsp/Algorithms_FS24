package main;

// not comparison-based
// k being the maximum number
// running time: O(n+k) ==> linear if k is fixed
// not stable ==> no original element is found in the array afterwards
// memory: O(k) for the array that stores the occurrences

public class CountingSort {

  private int[] array;
  private int n;
  private int k;

  public CountingSort(int[] array, int k) {
    this.array = array;
    this.n = array.length;
    this.k = k;
  }

  public void sort(){
    int[] counts = new int[k+1];

    for(int elem : array){
      counts[elem]++;
    }
    int pos = 0;
    for(int i = 0; i <= k; i++){
      int occOfElemAtPosI = counts[i];
      for(int j = 0; j < occOfElemAtPosI; j++){
        array[pos + j] = i;
      }
      pos += occOfElemAtPosI;
    }
  }
}
