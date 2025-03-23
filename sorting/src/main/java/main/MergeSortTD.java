package main;

// comparison-based
// running time: O(nlogn)
// stable
// memory: O(n)

import java.util.Arrays;

public class MergeSortTD {

  private int[] array;
  private int n;

  public MergeSortTD(int[] array){
    this.array = array;
    this.n = array.length - 1;
  }

  public void sort(){
    int[] temp = new int[n+1];
    sort_aux(0, n, temp);
  }
  public void sort_aux(int lo, int hi, int[] temp){
    if(lo >= hi)
      return;

    int mid = lo + (hi - lo) / 2;

    sort_aux(lo, mid, temp);
    sort_aux(mid+1, hi, temp);

    merge(lo, hi, mid, temp);
  }

  public void merge(int lo, int hi, int mid, int[] temp){
    int j = mid + 1;
    int i = lo;

    for(int k = lo; k <= hi; k++){
      if(j > hi || (i <= mid && array[i] <= array[j])){
        temp[k] = array[i];
        i++;
      }
      else{
        temp[k] = array[j];
        j++;
      }
    }

    for(int k = lo; k <= hi; k++){
      array[k] = temp[k];
    }
  }

}
