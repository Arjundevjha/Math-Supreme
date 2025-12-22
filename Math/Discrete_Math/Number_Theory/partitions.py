#calculating the value of p(n) for n is a positive integer
class Partition:

    def partition(n):
        if n < 0:
            return 0
        if n == 0:
            return 1

        partitions = [0] * (n + 1)
        partitions[0] = 1

        for i in range(1, n + 1):
            for j in range(i, n + 1):
                partitions[j] += partitions[j - i]

        return partitions[n]

# Example usage
if __name__ == "__main__":
    n = int(input("Enter a positive integer: "))
    print(f"The number of partitions of {n} is: {Partition.partition(n)}")
# This code calculates the number of partitions of a positive integer n.