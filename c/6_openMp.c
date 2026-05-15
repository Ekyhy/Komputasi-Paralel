#include <omp.h>
#include <stdio.h>

int main(){
#pragma omp parallel
{
    int id = omp_get_thread_num();
    int total = omp_get_num_threads();

    
    printf("Saya Thread %s dari Thread %d dengan total keseluruhan Thread [%d]\n", (id % 2 == 0) ? "Genap":"Ganjil", id, total); //Menggunakan ternary operator

    //Menggunakan if-else statement
    // if (id % 2 == 0)
    // {
    //     printf("Saya Thread Genap [%d] dari Total [%d]\n",id,total);
    // }
    // else {
    //     printf("Saya Thread Ganjil [%d] dari Total [%d]\n",id,total);
    // }
}
return 0;
}