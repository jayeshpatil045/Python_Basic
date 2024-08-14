'''
@Author: Jayesh Patil


@Date: 2024-12-08 


@Last Modified by: Jayesh Patil


@Last Modified time: 2024-12-08 10:23 PM


@Title : coupon_Numbers
'''
import random

class CouponCollector:
    
    @staticmethod
    def generate_random_number(max_value):
        """Generates a random number between 0 and max_value-1."""
        return random.randint(0, max_value - 1)
    
    @staticmethod
    def collect_coupons(N):
        """Simulates the coupon collection process for N distinct coupons."""
        collected_coupons = set()  
        total_random_numbers = 0  
        
        while len(collected_coupons) < N:
            new_coupon = CouponCollector.generate_random_number(N)
            total_random_numbers += 1
            collected_coupons.add(new_coupon)
        
        return total_random_numbers

def main():
    N = int(input("Enter the number of distinct coupon numbers: "))
    total_random_numbers = CouponCollector.collect_coupons(N)
    print(f"Total random numbers needed to collect all {N} distinct coupons: {total_random_numbers}")

if __name__ == "__main__":
    main()
