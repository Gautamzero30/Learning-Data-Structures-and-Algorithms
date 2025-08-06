#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#define MAX 100000

void linear_search(int arr[], int n, int key) {
    int found = 0;
    for (int i = 0; i < n; i++) {
        if (arr[i] == key) {
            printf("Element is found at index %d\n", i);
            found = 1;
            break; // stop after first occurrence
        }
    }
    if (!found) {
        printf("The element is not found in the array\n");
    }
}

void display(int arr[], int n){
    for(int i = 0; i < n; i++){
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

    if (n > MAX || n <= 0) {
        printf("Invalid array size.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 1000;
    }

    printf("Enter the element to search: ");
    scanf("%d", &key);

    display(arr, n);

    t1 = time(NULL);
    linear_search(arr, n, key);
    t2 = time(NULL);

    d = difftime(t2, t1);
    printf("Time taken to search: %lf seconds\n", d);

    return 0;
}
