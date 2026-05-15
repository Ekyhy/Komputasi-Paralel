#include <stdio.h>  //Header yang wajib digunakan untuk Input Output / dalam bahasa C
#include <stdlib.h> //Header yang wajib digunakan jika memakai malloc dan free

int main(){
    int number,iteration;  //Membuat inisialisasi tipe data dan penamaan parameter
    int *ptr;              //Membuat pointer yang menunjuk ke dalam nilai penyimpanan memori untuk tipe data yang diinputkan
    
    printf("Masukkan Array Dinamis (misal : 10) : ");
    scanf("%d",&number); //Meminta user untuk menginputkan array list untuk data dalam bentuk integer

    ptr = (int*) malloc(number * sizeof(int)); //Mengalokasikan blok memori mentah dalam ukuran byte

    if (ptr == NULL) //Membuat desision untuk mengatasi jika pengalokasian blok memori gagal
    {
        printf("Gagal mengalokasikan memori\n");
        return 1;
    }

    for (int i = 0; i < number; i++) //Membuat for-loop untuk membaca dan menampilkan iterasi dari data yang ada dalam memori menggunakan pointer
    {
        printf("Element %d : %d \n", i, ptr[i] = i + 1);
    }
    free(ptr);
    printf("Memori Telah Dialokasikan"); //Melepaskan memori yang dialokasikan agar dapat kembali digunakan oleh sistem

    return 0;
    
}