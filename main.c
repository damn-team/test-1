#include <stdio.h>
#include <string.h>
#include <stdlib.h>

// Function prototypes
void login();
void secret_admin_panel();
void process_data(char *input);

int main() {
    login();
    return 0;
}

void login() {
    char password[16];
    int authenticated = 0; // VULNERABILITY 1: Stack variable placement

    printf("Enter Admin Password: ");
    
    // VULNERABILITY 2: Classic Buffer Overflow (No bounds checking)
    // A long input can overwrite the 'authenticated' variable or the return address.
    gets(password); 

    if (strcmp(password, "p4ssw0rd123") == 0) {
        authenticated = 1;
    }

    if (authenticated) {
        printf("Access Granted!\n");
        secret_admin_panel();
    } else {
        printf("Access Denied.\n");
    }
}

void secret_admin_panel() {
    char cmd[100];
    printf("Enter system command to run: ");
    
    // VULNERABILITY 3: Command Injection
    // Direct execution of user input via system()
    fgets(cmd, sizeof(cmd), stdin);
    system(cmd); 
}

void process_data(char *input) {
    // VULNERABILITY 4: Format String Vulnerability
    // Passing user-controlled input directly as the format string
    printf(input); 

    // VULNERABILITY 5: Integer Overflow
    // Using signed shorts for size calculations can lead to wraps
    short size;
    printf("Enter data size: ");
    scanf("%hd", &size);
    
    if (size > 0) {
        char *buffer = (char *)malloc(size); // If size is 32767 + 1, it wraps to negative
        // ... do something with buffer
        free(buffer);
    }
}