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
    
    def random_exponential(self, rate, num_samples):
        results = []
        for _ in range(num_samples):
            u = self.generate()
            results.append(-np.log(u) / rate)
        return results
    
    def random_binomial(self, n, p, num_samples):
        results = []
        for _ in range(num_samples):
            count = 0
            for _ in range(n):
                if self.generate() < p:
                    count += 1
            results.append(count)
        return results
    
    def random_poisson(self, lam, num_samples):
        results = []
        for _ in range(num_samples):
            l = np.exp(-lam)
            k = 0
            p = 1
            while p > l:
                k += 1
                p *= self.generate()
            results.append(k - 1)
        return results
    
    def random_geometric(self, p, num_samples):
        results = []
        for _ in range(num_samples):
            results.append(int(np.ceil(np.log(1 - self.generate()) / np.log(1 - p))))
        return results
    
    def random_choice(self, choices, probabilities, num_samples):
        results = []
        cumulative_probs = np.cumsum(probabilities)
        for _ in range(num_samples):
            r = self.generate()
            for i, cp in enumerate(cumulative_probs):
                if r < cp:
                    results.append(choices[i])
                    break
        return results

def main():
    rng = EnhancedRandomGenerator()
    
    while True:
        print("\nRandom Number Generator Menu")
        print("1. Generate random float between 0 and 1")
        print("2. Generate random integer between two values")
        print("3. Generate random numbers from a uniform distribution")
        print("4. Generate random numbers from a normal distribution")
        print("5. Generate random numbers from an exponential distribution")
        print("6. Generate random numbers from a binomial distribution")
        print("7. Generate random numbers from a Poisson distribution")
        print("8. Generate random numbers from a geometric distribution")
        print("9. Generate random choices from a list")
        print("10. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            for _ in range(10):
                print(rng.generate())
        elif choice == 2:
            low = int(input("Enter low value: "))
            high = int(input("Enter high value: "))
            for _ in range(10):
                print(rng.generate_int(low, high))
        elif choice == 3:
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_uniform(num_samples))
        elif choice == 4:
            mean = float(input("Enter mean: "))
            std_dev = float(input("Enter standard deviation: "))
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_normal(mean, std_dev, num_samples))
        elif choice == 5:
            rate = float(input("Enter rate: "))
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_exponential(rate, num_samples))
        elif choice == 6:
            n = int(input("Enter number of trials: "))
            p = float(input("Enter probability of success: "))
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_binomial(n, p, num_samples))
        elif choice == 7:
            lam = float(input("Enter lambda: "))
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_poisson(lam, num_samples))
        elif choice == 8:
            p = float(input("Enter probability of success: "))
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_geometric(p, num_samples))
        elif choice == 9:
            choices = input("Enter choices separated by space: ").split()
            probabilities = list(map(float, input("Enter probabilities separated by space: ").split()))
            num_samples = int(input("Enter number of samples: "))
            print(rng.random_choice(choices, probabilities, num_samples))
        elif choice == 10:
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
