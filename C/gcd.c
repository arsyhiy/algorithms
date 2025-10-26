#include <stdio.h>

int gcd_step(int a, int b) {
	printf("Начало: a=%d, b=%d\n", a, b);
	while (b != 0) {
		printf("Вычисляем: a=%d, b=%d, a mod b=%d\n", a, b, a % b);
		int temp = b;
		b = a % b;
		a = temp;

	}
	printf("НОД найден: %d\n", a);
	return a;
}

// Пошаговый НОК через НОД
int lcm_step(int a, int b) { 
	int gcd_val = gcd_step(a, b);
	int lcm_val = (a * b) / gcd_val;
	printf("НОК: %d\n", lcm_val);
	return lcm_val;
}

int main() {
	int a = 24, b = 36;


	gcd_step(a, b); // Показывает шаги вычисления НОД
	lcm_step(a, b); // Показывает шаги вычисления НОК
	

	return 0;
}
