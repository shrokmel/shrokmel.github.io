---
layout: post
title: "Who actually KNOWS Python"
excerpt: "Custom written post descriptions are the way to go... if you're not lazy."
categories: articles
tags: [sample-post, video]
comments: true
share: true
modified: 2016-06-01T14:18:26-04:00
---

I realised how relevant this question really was, only recently, close to five years of actively using and coding in Python. What is "knowing"? When distracted about solving a given problem, it is very tempting to ignore thumbrules on writing good code. And there it is again, what is "good code". Veteran Python developers use the word "pythonic", almost interchangeably with good Python code. As I try to put a finger on what is actually pythonic, I am running the risk of the same issue that St. Augustine faced when trying to define time: "If no one ask of me, I know; if I wish to explain to him who asks, I know not." Nevertheless, let me try and bumble my way through this post, and put up some thumb rules for writing beautiful code.

However, these seemingly subjective terms, can, in fact, carry a tangible, and important meaning. There are multiple ways to solve any problem in Python. None of them are necessarily wrong, as long as you get the correct answer. But there are definitely only a small number of ways that makes your code readable, less verbose, and fast. This is what makes code pythonic. Pythonic code makes Python beautiful. In that brief moment, you read it, and go, "woah.. that's pretty cute." And, in my opinion, it is only in this context can one truly say that one "knows" Python. It is because of this peculiar quality to Python that I think it is worth mastering this versatile language. When you actually know Python, you can write readable, faster code, faster. This topic was covered in [this] (https://blog.startifact.com/posts/older/what-is-pythonic.html) blog post 12 years ago, and remains relevant to a large extent today.

The person who made me such a proponent of the language, Ryan Bradley, once said, "If you know what you're doing, you can write Python code, which is as fast your C code". I can't say that I have managed to achieve this all the time. But I can certainly see many instances where properly written Python scripts are faster than C scripts, if you include the actual writing of the code into the process.

For a terribly long time, I'm embarrased to admit, I had been oblivious to the Python faux pas that I had been committing. I became acutely aware of my inefficiencies largely after watching this video by Raymond Hettinger. 

<iframe width="560" height="315" src="https://youtu.be/OSGv2VnC0go" frameborder="0"> </iframe>

After the video, I left Python 2.7 for Python 3.6, and made it a point to consciously write pythonic code. Here is a collection of tricks that I have collated over this period (particularly in the context of scientific computing).

## Avoiding for loops

I realised that there is an incredible number of tools that you can use to avoid clunky, slow for loops in Python. The more you use these tricks, the faster, and more readable your code becomes. Let's say we have an array of numbers, between 0 - 100, in an arbitrary order. We want to simply pick out those values which are between 0 and 50, and populate a new array. In C this looks like this:

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

Although, this works, it wouldn't be considered pythonic. We can improve it by removing the for loop, and placing the condition as an array index.
```python
pick = arr[arr<50]
```
Cute, fast, readable, pythonic!



## Generators






Video embeds are responsive and scale with the width of the main content block with the help of [FitVids](http://fitvidsjs.com/).

```html
<iframe width="560" height="315" src="http://www.youtube.com/embed/PWf4WUoMXwg" frameborder="0"> </iframe>
```

And here's a Vimeo embed for testing purposes.

<iframe src="//player.vimeo.com/video/98146708?title=0&amp;byline=0" width="500" height="281" frameborder="0"> </iframe>
