import time
import numpy as np

class EnhancedRandomGenerator:
    def __init__(self):
        self.seed = int(time.time())
        self.a = 1664525
        self.c = 1013904223
        self.m = 2**32

    def generate(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed / self.m

    def generate_int(self, low, high):
        if low >= high:
            raise ValueError("Low value must be less than high value")
        return int(self.generate() * (high - low + 1)) + low

    def set_seed(self, seed):
        self.seed = seed

    def get_seed(self):
        return self.seed

    def set_parameters(self, a, c, m):
        self.a = a
        self.c = c
        self.m = m

    def get_parameters(self):
        return self.a, self.c, self.m

    def random_uniform(self, num_samples):
        return [self.generate() for _ in range(num_samples)]

    def random_normal(self, mean, std_dev, num_samples):
        # Box-Muller transform for generating normal distribution
        results = []
        for _ in range(num_samples // 2):
            u1 = self.generate()
            u2 = self.generate()
            z1 = (-2 * np.log(u1)) ** 0.5 * np.cos(2 * np.pi * u2)
            z2 = (-2 * np.log(u1)) ** 0.5 * np.sin(2 * np.pi * u2)
            results.append(z1 * std_dev + mean)
            results.append(z2 * std_dev + mean)
        if num_samples % 2 == 1:
            results.append(z1 * std_dev + mean)
        return results

if __name__ == "__main__":
    rng = EnhancedRandomGenerator()

    # print 10 random float numbers between 0 and 1
    print("Generating random float numbers between 0 and 1:")
    for _ in range(10):
        print(rng.generate())

    # print 10 random integers between 1 and 10
    print("\nGenerating random integers between 1 and 10:")
    for _ in range(10):
        print(rng.generate_int(1, 10))

    # Generate 5 samples from a uniform distribution
    print("\nGenerating 5 samples from a uniform distribution:")
    print(rng.random_uniform(5))

    # Generate 6 samples from a normal distribution with mean 0 and std_dev 1
    print("\nGenerating 6 samples from a normal distribution:")
    print(rng.random_normal(0, 1, 6))
