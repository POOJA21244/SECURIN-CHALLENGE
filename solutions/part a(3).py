# Initialize the 6*6 matrix
combi= [[0] * 6 for _ in range(6)]

# Calculating using for loop
for i in range(1,7):
    for j in range(1,7):
        combi[i-1][j-1]=i+j
        
# Probability 
probabilities = {}
for row in combi:
    for sum_value in row:
        if sum_value in probabilities:
            probabilities[sum_value] += 1
        else:
            probabilities[sum_value] = 1

for sum_value, count in probabilities.items():
    probabilities[sum_value] = count / 36

print("\nProbability of all possible sums:")
for sum_value, probability in probabilities.items():
    print(f"P(Sum={sum_value}) = {probability:.2f}")
