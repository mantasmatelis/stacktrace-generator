
Stacktrace Generator
====

A certain class at a certain university (I'm told that I can't say which) requires students to generate stack traces by hand given the source code of a program, and a place in the code at which to break.

Of course, there is a better way.

```
mantas@mantas-laptop:
$ cat demo.c                                                                                                
int sum_first(int n) {
    const int r =
		(n <= 1) ? 1 :
		n + sum_first(n-1);
	if(n==1) { asm volatile ("int3;"); } return r;
}
int main(void) {
	const int a = sum_first(3);
}
 
mantas@mantas-laptop:
$ clang -g demo.c                                                                                            
 
mantas@mantas-laptop:
$ ./genstack.py                                                                                              
=========================
sum_first:
  n: 1
  r: 1
return addr: sum_first:4
=========================
sum_first:
  n: 2
  r: 0
return addr: sum_first:4
=========================
sum_first:
  n: 3
  r: 0
return addr: main:8
=========================
main:
  a: 32767
return addr: OS
=========================
 
```

Notice that ```asm volatile ("int3;");``` is included at a specific condition to induce ```a.out``` to breakpoint, at which point ```genstack.py``` does the heavy lifting of generating a stack trace in the required format.

The Python LLDB library is required.
