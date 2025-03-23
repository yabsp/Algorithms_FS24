// ignore no package declaration warning

import static org.junit.jupiter.api.Assertions.*;

import java.util.Arrays;
import java.util.Random;
import javax.annotation.processing.SupportedAnnotationTypes;
import org.junit.jupiter.api.Test;

  class SortingTest {

    @Test
    void testInsertionSort() {
      Random random1 = new Random();

      int n = random1.nextInt(10)+1;
      int[] arr = new int[n];
      for(int i = 0; i < n; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      System.out.println("Insertions unsortiert: " + Arrays.toString(arr));
      main.InsertionSort insertion = new main.InsertionSort(arr);
      insertion.sort();
      System.out.println("Insertion Sortiert: " + Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr , arrVrgl);
    }

    @Test
    void testSelectionSort() {
      Random random1 = new Random();

      int m = random1.nextInt(20)+1;
      int[] arr = new int[m];
      for(int i = 0; i < m; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      System.out.println("Selection unsortiert: " + Arrays.toString(arr));
      main.SelectionSort selection = new main.SelectionSort(arr);
      selection.sort();
      System.out.println("Selection sortiert: " + Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr, arrVrgl);
    }

    @Test
    void testQuickSort() {
      Random random1 = new Random();

      int m = random1.nextInt(20)+1;
      int[] arr = new int[m];
      for(int i = 0; i < m; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      System.out.println("Quick unsortiert: " + Arrays.toString(arr));
      main.QuickSort quick = new main.QuickSort(arr);
      quick.sort();
      System.out.println("Quick sortiert: " + Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr, arrVrgl);
    }

    @Test
    void testMergeSortTD() {
      Random random1 = new Random();

      int n = random1.nextInt(20)+1;
      int[] arr = new int[n];
      for(int i = 0; i < n; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      System.out.println("Merge top down unsortiert: " +Arrays.toString(arr));
      main.MergeSortTD mergeTD = new main.MergeSortTD(arr);
      mergeTD.sort();
      System.out.println("Merge top down sortiert: " +Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr, arrVrgl);
    }

    @Test
    void HeapSort(){
      Random random1 = new Random();

      int n = random1.nextInt(20)+1;
      int[] arr = new int[n];
      for(int i = 0; i < n; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      System.out.println("Heap unsortiert: " +Arrays.toString(arr));
      main.HeapSort heap = new main.HeapSort(arr);
      heap.sort();
      System.out.println("Heap sortiert: " +Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr, arrVrgl);
    }

    @Test
    void testMergeSortBU() {
      Random random1 = new Random();

      int n = random1.nextInt(20)+1;
      int[] arr = new int[n];
      for(int i = 0; i < n; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      System.out.println("Merge bottom up unsortiert: " +Arrays.toString(arr));
      main.MergeSortBU mergeBU = new main.MergeSortBU(arr);
      mergeBU.sort();
      System.out.println("Merge bottom up sortiert: " +Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr, arrVrgl);
    }

    @Test
    void testCountingSort() {
      Random random1 = new Random();

      int n = random1.nextInt(20)+1;
      int[] arr = new int[n];
      for(int i = 0; i < n; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int[] arrVrgl = arr.clone();
      Arrays.sort(arrVrgl);
      System.out.println("Counting unsortiert: " +Arrays.toString(arr));
      main.CountingSort counting = new main.CountingSort(arr, arrVrgl[arrVrgl.length - 1]);
      counting.sort();
      System.out.println("Counting sortiert: " +Arrays.toString(arr));
      assertArrayEquals(arr, arrVrgl);
    }

    @Test
    void testRadixSort() {
      Random random1 = new Random();

      int n = random1.nextInt(20)+1;
      int[] arr = new int[n];
      for(int i = 0; i < n; i++) {
        arr[i] = random1.nextInt(1000);
      }
      int base = random1.nextInt(10);
      while(base == 1 || base == 0)
        base = random1.nextInt(10);

      int[] arrVrgl = arr.clone();
      System.out.println("Radix unsortiert: " +"(" +base +")" +Arrays.toString(arr));
      main.RadixSort radix = new main.RadixSort(arr, base);
      radix.sort();
      System.out.println("Radix sortiert: " +"(" +base +")" +Arrays.toString(arr));
      Arrays.sort(arrVrgl);
      assertArrayEquals(arr, arrVrgl);
    }
}
