import time

class SimpleRandomGenerator:
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

if __name__ == "__main__":
    rng = SimpleRandomGenerator()
    
    print("Generating random float numbers between 0 and 1:")
    for _ in range(10):
        print(rng.generate())
    
    print("\nGenerating random integers between 1 and 10:")
    for _ in range(10):
        print(rng.generate_int(1, 10))
    
    rng.set_seed(12345)
    rng.set_parameters(48271, 0, 2**31 - 1)
    print("\nUpdated seed:", rng.get_seed())
    print("Updated parameters:", rng.get_parameters())
    
    print("\nGenerating with updated settings:")
    for _ in range(5):
        print(rng.generate())
