package main;

// comparison-based
// running time: O(nlogn)
// stable
// space: O(n)

public class MergeSortBU {

  private int[] array;
  private int n;

  public MergeSortBU(int[] array) {
    this.array = array;
    this.n = array.length - 1;
  }

  public void sort() {
    int length = 1;
    int[] temp = new int[n + 1];

    while (length <= n) {
      for (int i = 0; i <= n; i += 2 * length) {
        int lo = i;
        int mid = lo + length - 1;
        int hi = Math.min(lo + 2 * length - 1, n);
        merge(lo, hi, mid, temp);
      }
      length *= 2;
    }
  }

  public void merge(int lo, int hi, int mid, int[] temp) {
    int i = lo;
    int j = mid + 1;

    for (int k = lo; k <= hi; k++) {
      if (j > hi || (i <= mid && array[i] <= array[j])) {
        temp[k] = array[i];
        i++;
      } else {
        temp[k] = array[j];
        j++;
      }
    }

    for (int k = lo; k <= hi; k++) {
      array[k] = temp[k];
    }
  }
}
