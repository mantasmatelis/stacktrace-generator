int sum_first(int n) {
	const int r =
		(n <= 1) ? 1 :
		n + sum_first(n-1);
	if(n==1) { asm volatile ("int3;"); } return r;
}
int main(void) {
	const int a = sum_first(3);
}
