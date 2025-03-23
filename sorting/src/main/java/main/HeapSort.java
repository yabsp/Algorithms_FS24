package main;

// comparison-base
// running time: O(nlogn)
// not stable
// memory: O(1)

public class HeapSort {

  private final int[] array;
  private int n;

  public HeapSort(int[] array){
    this.array = array;
    this.n = array.length - 1;
  }

  public void sort(){

    for(int i = n / 2; i >= 0; i--){
      heapify(array, i, n);
    }

    for(int i = n; i >= 0; i--){
      int swap = array[0];
      array[0] = array[i];
      array[i] = swap;

      heapify(array, 0, i - 1);
    }

  }

  private void heapify(int[] heap, int i, int size){
    int l = i * 2 + 1;
    int r = i * 2 + 2;
    int largest = i;

    if(l <= size && heap[l] > heap[i])
      largest = l;
    if(r <= size && heap[r] > heap[largest])
      largest = r;
    if(largest != i) {
      int swap = heap[i];
      heap[i] = heap[largest];
      heap[largest] = swap;
      heapify(heap, largest, size);
    }
  }
}
