Hello! Let's get some test code in here - a whole file:

``[An example of a failing Python pytest test](../test/test_sample.py)

---

What if we only want a certain range of lines from a file?
Let's try and get just 2 lines, 6 and 7:

``6:7[An example of a failing Python pytest test](../test/test_sample.py)

---

What if we are referencing a single test in a file with many tests, which is likely to be modified in the future?
Line counts are not reliable... If we have some specific phrase to pin to, we can try and detect an even number of () {} or indentation.
Experimental.


