# dna-sequence
## What is it?
A algorithm for the shortest common supersequence problem. Given n strings, find the shortest string such that all n strings are subsequences of that string. This algorithm uses a greedy approach to recursively find the string in the list of strings that creates the greatest overlap with the running output, where overlap is defined as the number of consecutive characters at the end of the running ouput that match the beginning of the string, or vice versa. This approximation produces a result that is within 2.5 times the size of the optimal solution.

This is intended to be similar to the shotgun sequencing algorithm used for DNA splicing in the Human Genome Project.
