🔍 Function: Search for a Character in a String

This Python script defines a function that searches for the first occurrence of a specified character inside a given string.

How it works

The function function(str1, chr) loops through the string str1 from index 0 to len(str1)-2.

At each position, it checks whether the current character matches chr.

If a match is found, it immediately returns the index of that character.

If the loop finishes without finding the character, the function returns "not found".

User Input

The program:

Accepts a string from the user (a)

Accepts a character to search for (b)

Prints the result returned by the function

Example
Input:
hello
l

Output:
2

Notes

The loop uses range(len(str1) - 1), so it does not check the last character of the string.
If you want to include the last character, use range(len(str1)) instead.

The function returns a string "not found" instead of -1, which may be useful for user messages.# program_1
This Python script defines a function that searches for the first occurrence of a specified character inside a given string.
