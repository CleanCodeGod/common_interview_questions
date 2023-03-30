**Question:**
Write a program to count up to ten and print each even number. 

**Solution:**
I approach this problem by utilizing the Observer design pattern. We can have a Subject class that will count up to ten and notify the Observer class whenever an even number is encountered. The Observer class will then print the even number.


As you can see, we are utilizing the Observer design pattern to separate the counting logic and the even number printing logic. This allows for greater flexibility and modularity in our code. Additionally, we are using abstract classes to ensure that our code follows the Liskov substitution principle.

Of course, as a Clean Code Evangelist, I would also ensure that our code is properly formatted to my liking, documented as I see fit, and follows other best practices that I prefer.
