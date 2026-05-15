#include <stdio.h>



int main(){
    int y = 100;
    int *ptr = &y;

    printf("Nilai dari pointer adalah: %p \n", ptr);
    printf("Alamat dari nilai pointer adalah: %d \n", *ptr);

    return 0;
}
