#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define TABLE_SIZE 10

typedef struct {
    char key[100];
    int value;
    bool isFilled;
    bool isDeleted;
} Entry;

Entry hashTable[TABLE_SIZE];

int hash(char* key) {
    int sum = 0;
    for (int i = 0; key[i]; i++)
        sum += key[i];
    return sum % TABLE_SIZE;
}

void insert(char* key, int value) {
    int index = hash(key);
    int i = 0;

    while (i < TABLE_SIZE) {
        int newIndex = (index + i * i) % TABLE_SIZE;
        if (!hashTable[newIndex].isFilled || hashTable[newIndex].isDeleted) {
            strcpy(hashTable[newIndex].key, key);
            hashTable[newIndex].value = value;
            hashTable[newIndex].isFilled = true;
            hashTable[newIndex].isDeleted = false;
            printf("Inserted (%s, %d) at index %d\n", key, value, newIndex);
            return;
        }
        i++;
    }
    printf("Hash table is full! Could not insert %s\n", key);
}

int search(char* key) {
    int index = hash(key);
    int i = 0;

    while (i < TABLE_SIZE) {
        int newIndex = (index + i * i) % TABLE_SIZE;

        if (!hashTable[newIndex].isFilled && !hashTable[newIndex].isDeleted)
            return -1;

        if (hashTable[newIndex].isFilled && !hashTable[newIndex].isDeleted &&
            strcmp(hashTable[newIndex].key, key) == 0)
            return hashTable[newIndex].value;

        i++;
    }
    return -1;
}

void delete(char* key) {
    int index = hash(key);
    int i = 0;

    while (i < TABLE_SIZE) {
        int newIndex = (index + i * i) % TABLE_SIZE;

        if (hashTable[newIndex].isFilled && !hashTable[newIndex].isDeleted &&
            strcmp(hashTable[newIndex].key, key) == 0) {
            hashTable[newIndex].isDeleted = true;
            printf("Deleted key: %s from index %d\n", key, newIndex);
            return;
        }
        if (!hashTable[newIndex].isFilled && !hashTable[newIndex].isDeleted)
            break;
        i++;
    }
    printf("Key not found: %s\n", key);
}

void display() {
    for (int i = 0; i < TABLE_SIZE; i++) {
        printf("[%d]: ", i);
        if (hashTable[i].isFilled && !hashTable[i].isDeleted)
            printf("(%s, %d)\n", hashTable[i].key, hashTable[i].value);
        else if (hashTable[i].isDeleted)
            printf("<deleted>\n");
        else
            printf("NULL\n");
    }
}

int main() {
    insert("Kathmandu", 1);
    insert("Pokhara", 2);
    insert("Lalitpur", 3);
    insert("Bhaktapur", 4);
    insert("Biratnagar", 5);
    insert("Janakpur", 6);
    insert("Butwal", 7);
    insert("Dharan", 8);
    insert("Hetauda", 9);
    insert("Nepalgunj", 10); 

    printf("\nHash Table:\n");
    display();

    printf("\nSearch 'Dharan': %d\n", search("Dharan"));

    delete("Butwal");
    delete("Lalitpur");

    printf("\nHash Table after deletions:\n");
    display();

    return 0;
}
