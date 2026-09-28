# Create a new process
The newly-created process has its own copy of the **address space**, **registers** and **PC**.

``` C++
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main(int argc, char *argv[]){
	printf("hello world (pid:%d)\n", (int) getpid());
	int rc = fork();
	if (rc < 0) { // fork failed; exit
		fprintf(stderr, "fork failed\n");
		exit(1);
	} else if (rc == 0) { // child (new process)
		printf("hello, I am child (pid:%d)\n", (int) getpid());
	} else { // parent goes down this path (main)
		int wc = wait(NULL);
		printf("hello, I am parent of %d (pid:%d)\n",
		rc, wc, (int) getpid());
	}
	return 0;
}
```
The process forks itself
E.g. invoking a program via terminal -> the terminal forks itself and replaces its code with the program's


Run a program that's different from the calling program
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
int main(int argc, char *argv[]){
	printf("hello world (pid:%d)\n", (int) getpid());
	int rc = fork();
	if (rc < 0) { // fork failed; exit
		fprintf(stderr, "fork failed\n");
		exit(1);
	} else if (rc == 0) { // child (new process)
		printf("hello, I am child (pid:%d)\n", (int) getpid());
		char *myargs[3];
		myargs[0] = strdup("wc"); // program: "wc" (word count)
		myargs[1] = strdup("p3.c"); // argument: file to count
		myargs[2] = NULL; // marks end of array
		execvp(myargs[0], myargs); // runs word count
		printf("this shouldn’t print out");
	} else { // parent goes down this path (main)
		int wc = wait(NULL);
		printf("hello, I am parent of %d (wc:%d) (pid:%d)\n",
		rc, wc, (int) getpid());
	}
	return 0;
}
```


All of the above with redirection
```c
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <fcntl.h>
#include <sys/wait.h>
int main(int argc, char *argv[]){
	int rc = fork();
	if (rc < 0) { // fork failed; exit
		fprintf(stderr, "fork failed\n");
		exit(1);
	} else if (rc == 0) { // child: redirect standard output to a file
		close(STDOUT_FILENO);
		open("./p4.output", O_CREAT|O_WRONLY|O_TRUNC, S_IRWXU);
		// now exec "wc"...
		char *myargs[3];
		myargs[0] = strdup("wc"); // program: "wc" (word count)
		myargs[1] = strdup("p4.c"); // argument: file to count
		myargs[2] = NULL; // marks end of array
		execvp(myargs[0], myargs); // runs word count
	} else { // parent goes down this path (main)
		int wc = wait(NULL);
	}
	return 0;
}
```


