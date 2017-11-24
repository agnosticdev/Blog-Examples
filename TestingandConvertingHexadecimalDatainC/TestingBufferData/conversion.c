/**
 * Hexadecimal character conversion to ascii
 * Included testing module to test our accuracy in our conversion
 *
 * Compile: (compile.py handles this for you)
 * gcc -c conversion.c -o conversion.o
 * gcc -c conversion_tests.c -o conversion_tests.o
 * gcc conversion.o conversion_tests.o -o conversion
 *
 * ./compile.py form the command line with at least Python 2.7
 **/
#include <stdio.h>
#include "conversion_tests.h"

#define SMALL_BUFFER_SIZE 2
#define LARGE_BUFFER_SIZE 8

int main(int argc, char **argv) {
	
	// Value between 0 and 255
	unsigned char hexData[SMALL_BUFFER_SIZE] = {0x6a, 0xdc};
	char hexSwapArray[4];

	for (int i = 0; i < SMALL_BUFFER_SIZE; i += 1) {
		// hexSwapArray contains the original characters and hexData has the
		// current set being formatted as lowercase hexidecimal
    	sprintf(hexSwapArray, "%x", hexData[i]);
    	printf("char string: %s\n", hexSwapArray);
    }

    // Now let's test our code out using the algorithm implemented above
    // Check the accuracy of sprintf by manually converting the decimal value
    // to a hex value and comparing the two char arrays

    // Can no longer use unsigned char as values are now outside 0 and 255
    unsigned int hexDataRetro[LARGE_BUFFER_SIZE] = {0x00, 0x3f3f, 0x0d, 0x3f, 
    	                                            0xdddd, 0xcd, 0x02, 0x5f};
    for (int e = 0; e < LARGE_BUFFER_SIZE; e += 1) {
    	printf("-------- TEST START --------\n");
    	if (test_sprintf_hex_data(hexDataRetro[e], LARGE_BUFFER_SIZE) == 0) {
    		printf("PASSED: The comparison using sprintf DID compare correctly\n");
    	} else {
    		printf("FAILED: The comparison using sprintf did not compare correctly\n");
    	}
    	printf("----------------------------\n");
    }
    
    return 0;
}