#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define MAX 100000

int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;
    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            int temp = arr[i]; arr[i] = arr[j]; arr[j] = temp;
        }
    }
    int temp = arr[i + 1]; arr[i + 1] = arr[high]; arr[high] = temp;
    return i + 1;
}

void quick_sort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quick_sort(arr, low, pi - 1);
        quick_sort(arr, pi + 1, high);
    }
}

int binary_search_any(int arr[], int n, int key) {
    int low = 0, high = n - 1;
    while (low <= high) {
        int mid = (low + high) / 2;

        if (arr[mid] == key) {
            return mid;
        } else if (arr[mid] < key) {
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    return -1;
}

void print_all_occurrences(int arr[], int n, int key) {
    int idx = binary_search_any(arr, n, key);
    if (idx == -1) {
        printf("Element %d not found in the array.\n", key);
        return;
    }

    int count = 0;
    int i = idx;
    printf("Element %d found at index %d :\n", key,idx);


    while (i >= 0 && arr[i] == key) {
        i--;
    printf("Element %d  is also found at index %d :\n", key,i);    

    }
    while(idx < n && arr[idx] == key) {
        // printf("%d ", i);
        // count++;
        idx++;
        printf("Element %d is also found at index %d :\n", key,idx);
    }
    

    // printf("Element %d found at index %d :\n", key,idx);
    // while (left < n && arr[left] == key) {
    //     printf("%d ", left);
    //     count++;
    //     left++;
    //      printf("Element %d is also  found at index %d :\n", key,i);
    // }
    // printf("\nTotal occurrences: %d\n", count);
}

void display(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int main() {
    srand(time(NULL));
    double d;
    time_t t1, t2;
    int n, key;

    int arr[MAX];
    printf("Enter the number of elements (max %d): ", MAX);
    scanf("%d", &n);

    if (n <= 0 || n > MAX) {
        printf("Invalid array size.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    quick_sort(arr, 0, n - 1);

    printf("Enter the element to search: ");
    scanf("%d", &key);
    printf(" %d ", arr[585]);

    if (n <= 100) {
        printf("Sorted array:\n");
        display(arr, n);
    }

    t1 = time(NULL);
    print_all_occurrences(arr, n, key);
    t2 = time(NULL);

    d = difftime(t2, t1);
    printf("Time taken to search: %lf seconds\n", d);

    return 0;
}
