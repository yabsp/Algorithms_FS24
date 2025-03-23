package main;

// comparison-based
// running time: best/average/worst; O(nlogn)/O(nlogn)/O(n^2)
// not-stable
// memory: best/average/worst; O(logn)/O(logn)/O(n)

import java.util.Random;

public class QuickSort {

  private int[] array;
  private int n;

  public QuickSort(int[] array) {
    this.array = array;
    this.n = array.length - 1;
  }

  public void sort(){
    sort_aux(0, n);
  }

  public void sort_aux(int lo, int hi){
    if(lo >= hi)
      return;
    randomPivotAndSwapToLo(lo, hi);
    int pivotPos = partition(lo, hi);
    sort_aux(lo, pivotPos - 1);
    sort_aux(pivotPos + 1, hi);

  }

  public void randomPivotAndSwapToLo(int lo, int hi){
    int pivotPos = lo + new Random().nextInt(hi-lo);
    int temp = array[lo];
    array[lo] = array[pivotPos];
    array[pivotPos] = temp;
  }

  public int partition(int lo, int hi){
    int j = hi;
    int pivot = array[lo];
    int i = lo + 1;

    while(true){
      while(i < hi && array[i] < pivot){
        i++;
      }
      while(j > lo && array[j] > pivot){
        j--;
      }
      if(j <= i)
        break;

      int temp = array[i];
      array[i] = array[j];
      array[j] = temp;

      i++; j--;

    }

    int temp = array[lo];
    array[lo] = array[j];
    array[j] = temp;

    return j;
  }
}
