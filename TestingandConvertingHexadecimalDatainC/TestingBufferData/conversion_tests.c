/**
 * conversion_test.c
 *
 * Conversion Tests Module code
 * This module test's the accuracy of our hex values being converted with sprintf
 * This file can optionally be compiled with the main program.
 * This file should be recognized with compile.py
 **/
#include <stdio.h>
#include <string.h>
#include "conversion_tests.h"


/**
 * Our test function manually converts the decimal represented decimalHexValue 
 * to a hex value by hand.
 *
 * The hex value is then compared against the output of sprintf to check accuracy
 * and to check if we can assert accuracy on sprintf for converting hex values.
 */
int test_sprintf_hex_data(unsigned int decimalHexValue, int size) {

	// This implementation is fairly wasteful in terms of memory
    // The three char arrays represent an optomistic chunk of memory to prove our test
    // Using an assigned char limit could be dangerous in this situation
    // It might be better to look into dynamically allocation memory using calloc in a running app
	char hexChars[16] = "0123456789abcdef";
	unsigned int decimalValue = decimalHexValue;
	char reverseBuffer[10], swapBuffer[10], compareBuffer[10];
	int whileFlag = 1, index = 0, reverseIndex = 0;

	// Zero out the reverseBuffer and compareBuffer for potential memory issues
	for (int j = 0; j < 10; j += 1) {
    	reverseBuffer[j] = 0;
    	compareBuffer[j] = 0;
    }

	while(whileFlag) {
		if (decimalValue > 0) {
			reverseBuffer[index] = hexChars[decimalValue % 16];
			index += 1;
			decimalValue = decimalValue / 16;

		} else {
			whileFlag = 0;
		}
	}

	if (index > 0) {
		for (int e = (index-1); e >= 0; e -= 1) {
			compareBuffer[reverseIndex] = reverseBuffer[e];
			reverseIndex += 1;
		}
	} else {
		compareBuffer[reverseIndex] = '0';
	}
		
	// Print out the swap and compare buffers
	sprintf(swapBuffer, "%x", decimalHexValue);
    printf("swap buffer : %s\n", swapBuffer);
    printf("compare buffer: %s\n", compareBuffer);

	return strcmp(swapBuffer, compareBuffer);
}