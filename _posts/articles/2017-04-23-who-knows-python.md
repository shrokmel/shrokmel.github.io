---
layout: post
title: "Who actually knows Python?"
excerpt: "Many people claim to know Python, but who actually does?"
categories: articles
author: arvind_ravichandran
tags: [idiomatic, beautiful, pythonic]
comments: true
share: true
modified: 2017-04-23T20:08:14-04:00
---

I realised how relevant this question really was, only recently, close to five years of actively using and coding in Python. What is "knowing"? When distracted about solving a given problem, it is very tempting to ignore thumbrules on writing good code. And there it is again, what is "good code". Veteran Python developers use the word "pythonic", almost interchangeably with good Python code. As I try to put a finger on what is actually pythonic, I am running the risk of the same issue that St. Augustine faced when trying to define time: "If no one ask of me, I know; if I wish to explain to him who asks, I know not." Nevertheless, let me try and bumble my way through this relatively vague notion, because these seemingly subjective terms, "knowing Python", or writing "pythonic" code," can, in fact, carry a tangible, and important meaning.

There are multiple ways to solve any problem in Python. None of them are necessarily wrong, as long as you get the correct answer. But there are definitely only a small number of ways that makes your code readable, less verbose, and fast. This is what makes code pythonic. Pythonic code makes Python beautiful. In that brief moment, you read it, and go, "woah.. that's pretty cute." And, in my opinion, it is only in this context can one truly say that one "knows" Python. It is because of this peculiar quality to Python that I think it is worth mastering this versatile language. When you actually know Python, you can write readable, faster code, faster. This topic was covered in [this](https://blog.startifact.com/posts/older/what-is-pythonic.html) blog post 12 years ago, and remains relevant to a large extent today.

The person who made me such a proponent of the language, Ryan Bradley, once said, "If you know what you're doing, you can write Python code, which is as fast your C code". I can't say that I have managed to achieve this all the time. But I can certainly see many instances where properly written Python scripts are faster than C scripts, if you include the actual writing of the code into the process.

For a terribly long time, I'm embarrased to admit, I had been oblivious to the Python faux pas that I had been committing. I became acutely aware of my inefficiencies largely after watching this video by Raymond Hettinger.

<iframe width="560" height="315" src="https://www.youtube.com/embed/OSGv2VnC0go" frameborder="0" allowfullscreen></iframe>

After the video, I left Python 2.7 for Python 3, and made it a point to consciously write pythonic code. Here is a collection of tricks that I have collated over this period (particularly in the context of scientific computing).

Over the years of coding, I've come to learn that optimising Python code comes in clear discrete steps. We must always begin by writing a program that gives correct results. Then check where the program is slow, by way of profiling, and over time, just by looking at parts which are sloppy. Every step of the optimisation process, you can check your results with the one that you are sure is correct. In general, one can follow [these steps](https://wiki.python.org/moin/PythonSpeed/PerformanceTips):

1. Get it right
2. Test it's right
3. Profile if slow
4. Optimise
5. Repeat from 2

Certain optimizations amount to good programming style and so should be learned as you learn the language. An example would be moving the calculation of values that don't change within a loop, outside of the loop. We will see instances of this shortly.

## Avoiding for loops

I've come to learn that that there is an incredible number of tools that you can use to avoid clunky, slow for loops in Python. The more you use these tricks, the faster, and more readable your code becomes.

Let's say we have an array of numbers, between 0 - 100, in an arbitrary order. We want to simply pick out those values which are between 0 and 50, and populate a new array. In C this looks like this:

```c
// "arr" contains these numbers
// we want to populate the array, "pick" with numbers between 0 - 50

ct=0;         // counter for pick
for (i=0; i<list_length; i++){
    if arr[i]<50{
        pick[ct]=arr[i];
        ct++;
    }
}
```

The direct equivalent for this in Python would be this:

```python
for i in range(list_length):
    if arr[i]<50:
        pick[ct] = arr[i]
        ct++
```

Although, this works, it wouldn't be considered pythonic. Firstly, we have this ugly array "pick", which needs to be defined before hand, and is of unknown size. Even if we made it a list, to which we append these numbers as they arrive, we have to convert it back to an array to operate on it. We can improve this, substantially, and firstly by removing the for loop, and making the if condition an array index.
```python
pick = arr[arr<50]
```
This reads, all values in _arr_, which have values less than 50, are now _pick_. Cute, fast, readable, pythonic! This method of selecting values based on condition is rather versatile. We can add conditions together, and place it inside the array index too. For instance, if we want values greater than 25, smaller than 50, we write:

```python
pick = arr[(arr>25) & (arr<50)]
```

This trick becomes incredibly powerful, when you have two arrays, _arr1_ and _arr2_, describing the same set, and are hence of the same size. Now, if you want to select values in _arr1_, based on a criteria that satisfies _arr2_, we can use the same method that we used eariler. For instance, we have particles with _x_ and _y_ values in two different arrays, _arrx_ and _arry_, respectively. You want the _x_ axis values of those particles who have _y_ values greater than 75:

```python
pick = arrx[arry>75]
```

No for loops!


<!-- ## List comprehensions -->



<!-- ## Generators -->
