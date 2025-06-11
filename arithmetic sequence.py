# Generate arithmetic sequence: a_n = a_1 + (n-1) * d
# where a_1 = 5 (first term), d = 3 (common difference), n = 8 (number of terms)

def generate_arithmetic_sequence(first_term, common_diff, num_terms):
    """Generate an arithmetic sequence."""
    sequence = []
    for i in range(num_terms):
        term = first_term + i * common_diff
        sequence.append(term)
    return sequence

# Parameters
first_term = 5
common_diff = 3
num_terms = 8

# Generate the sequence
sequence = generate_arithmetic_sequence(first_term, common_diff, num_terms)

# Display the results
print(f"Arithmetic sequence starting at {first_term} with common difference {common_diff}:")
print(f"First {num_terms} terms: {sequence}")

# Alternative: Print each term with its position
print("\nTerm by term:")
for i, term in enumerate(sequence, 1):
    print(f"Term {i}: {term}")

# Verify using the formula: a_n = a_1 + (n-1) * d
print(f"\nVerification using formula a_n = {first_term} + (n-1) * {common_diff}:")
for n in range(1, num_terms + 1):
    term = first_term + (n - 1) * common_diff
    print(f"a_{n} = {first_term} + ({n}-1) * {common_diff} = {term}")
