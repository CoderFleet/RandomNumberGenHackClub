# RandomNumberGenHackClub

## Introduction

Hey everyone! I've been diving into the world of random number generators. This project is all about understanding how these generators create numbers that seem random but are actually generated using some clever math tricks.

## How Random Number Generators Work

From what I've been reading, random number generators start with a seed (a starting number) and use methods like a linear congruential generator (LCG). This method applies mathematical formulas to produce a sequence of numbers that appear random. It's interesting to note that there are no 'true' random number generators—they simply generate numbers that look random to us, but they follow predictable patterns.

![Random Number Generator](https://github.com/CoderFleet/RandomNumberGenHackClub/blob/main/image.png)

## Project Details

### Objectives

The primary goal of this project is to develop a custom random number generator in Python. This generator will initially produce numbers between 0 and 1 and will later extend to generate integers and allow customization of the range of numbers generated.

### Stage 1: Generating Random Numbers Between 0 and 1

I've begun exploring how to build a simple random number generator. This would give me numbers between 0 and 1. The initial approach involves using the current time as a seed and applying basic mathematical operations. However, I'm still in the process of understanding how to refine this method to improve its randomness and distribution.

### Stage 2: Understanding Randomness and Distribution

As I delve deeper into my research, I'm focusing on improving the randomness and distribution of the generated numbers. This stage involves learning about different algorithms and techniques that can enhance the unpredictability and spread of the generated numbers.

### Stage 3: Exploring Integer Generation and Custom Ranges

In my exploration, I'm also looking into extending the generator to produce whole numbers (integers) and allowing customization of the range of generated numbers. This includes understanding scaling and rounding techniques to convert fractional results into integers and generating numbers within specified ranges.

### Stage 4: Seeding and Reproducibility

Another aspect I'm researching is how to seed the generator with specific values to reproduce the same sequence of random numbers. This is crucial for testing and debugging purposes, where reproducibility of results is desired.

## After Full Info Gathering and Research

#### 1
To kick off, I'll start with a simple implementation using the current time as a seed. The core mathematics here will involve implementing a linear congruential generator (LCG) algorithm. This algorithm uses multiplication, addition, and modulus operations to produce a sequence of pseudo-random numbers.

#### 2
As I progress, I'll explore methods to improve the randomness and distribution of the generated numbers. This stage may involve experimenting with more advanced algorithms such as the Mersenne Twister or cryptographic algorithms like Blum Blum Shub. I'll dive into the mathematics behind these algorithms to understand how they achieve better randomness.

#### 3
Next, I'll extend the generator to produce integers and allow users to specify custom ranges for the generated numbers. This will require additional mathematical operations such as scaling, rounding, and possibly implementing transformation functions to map decimal outputs to integers within specified ranges.

---

I'm excited to continue my exploration and share more insights as I dive deeper into the mechanics of randomness and probability!

