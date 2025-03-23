package main;
// not comparison-based
/* running time:
m: Maximal number of digits in representation --> e.g base = 10 and max_val = 239 then m = 3
with given base b.
n: length of input sequence
==> O(m*(n+b))

==> linear for fixed m and b
 */
// stable
// memory: O(n + b)


import java.util.ArrayList;
import java.util.Iterator;

public class RadixSort {

  private int[] array;
  private int n;
  private int base;

  public RadixSort(int[] array, int base) {
    this.array = array;
    this.base = base;
    this.n = array.length;
  }

  public void sort(){
    if(array == null || array.length == 1) return;
    int max = Integer.MIN_VALUE;
    for(int i = 0; i < n; i++){
      max = Math.max(max, array[i]);
    }

    ArrayList<ArrayList<Integer>> buckets = new ArrayList<>(base);
    for(int i = 0; i < base; i++){
      buckets.add(new ArrayList<>());
    }
    int i = 0;
    while(Math.pow(base, i) <= max){
      for(int elem : array) {
        int digit = (int) ((elem / Math.pow(base, i)) % base);
        buckets.get(digit).add(elem);
      }
      int pos = 0;
      for(ArrayList<Integer> bucket : buckets){
        Iterator<Integer> iterator = bucket.iterator();
        while(iterator.hasNext()){
          array[pos++] = iterator.next();
          iterator.remove();
        }
      }
      i++;
    }

  }
}
