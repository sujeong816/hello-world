#include <stdio.h>

int main(void)
{
	int i = 0;
	int j = 0;
	int k = 0;

	for (i = 0; i < 5; i++){
		for ( j = 0; j < 5 - i - 1; j++)
			printf(" ");
		for ( k =0; k < 2 * i + 1; k++)
			printf("*");
		printf("\n");
	}
	

	for (i = 5; i > 0; i--){
		for ( j = 0; j < 5 - i ; j++)
			printf(" ");
		for (k = 0; k < 2 * i - 1; k++)
			printf("*");
		printf("\n");
	}
	

			return 0;
}