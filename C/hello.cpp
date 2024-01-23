
#include <stdio.h>
int main() {

    int num1, num2, choice;
    printf("Enter two integers: ");
    scanf("%d %d", &num1, &num2);
    
    printf("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division: ");
    scanf("%d", &choice);
    
    switch(choice) {
        case 1:
            printf("Result: %d", num1 + num2);
            break;
        case 2:
            printf("Result: %d", num1 - num2);
            break;
        case 3:
            printf("Result: %d", num1 * num2);
            break;
        case 4:
            if(num2 != 0)
                printf("Result: %.2f", (float)num1 / (float)num2);
            else
                printf("Error! Division by zero is not allowed.");
            break;
        default:
            printf("Invalid choice!");
            break;
    }
    
    return 0;
}

