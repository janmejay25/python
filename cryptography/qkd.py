import random

# Define the two bases
BASES = ['+', 'x']  # '+' = rectilinear (|, –), 'x' = diagonal (/,\)

# Step 1: Alice generates random bits and bases
def generate_bits_and_bases(n):
    bits = [random.randint(0, 1) for _ in range(n)]
    bases = [random.choice(BASES) for _ in range(n)]
    return bits, bases

# Step 2: Alice encodes bits (for simulation purposes)
def encode_qubits(bits, bases):
    # In real QKD, this would be photon polarization
    return list(zip(bits, bases))

# Step 3: Bob chooses random bases and "measures" the qubits
def measure_qubits(qubits, bob_bases):
    measured_bits = []
    for i, (bit, alice_basis) in enumerate(qubits):
        bob_basis = bob_bases[i]
        if bob_basis == alice_basis:
            measured_bits.append(bit)  # correct measurement
        else:
            measured_bits.append(random.randint(0, 1))  # wrong basis, random outcome
    return measured_bits

# Step 4: Compare bases to keep matching bits
def sift_key(alice_bits, alice_bases, bob_bits, bob_bases):
    sifted_alice = []
    sifted_bob = []
    for i in range(len(alice_bits)):
        if alice_bases[i] == bob_bases[i]:
            sifted_alice.append(alice_bits[i])
            sifted_bob.append(bob_bits[i])
    return sifted_alice, sifted_bob

# Step 5: Eavesdropper Eve (optional)
def intercept_and_resend(qubits):
    intercepted = []
    for bit, basis in qubits:
        # Eve randomly measures with random basis
        eve_basis = random.choice(BASES)
        if eve_basis == basis:
            measured = bit
        else:
            measured = random.randint(0, 1)
        intercepted.append((measured, eve_basis))  # She resends what she saw
    return intercepted

# Step 6: Test a subset to detect eavesdropping
def detect_eavesdrop(alice_key, bob_key):
    test_sample = min(10, len(alice_key))  # test up to 10 bits
    sample_indices = random.sample(range(len(alice_key)), test_sample)
    mismatches = 0
    for i in sample_indices:
        if alice_key[i] != bob_key[i]:
            mismatches += 1
    error_rate = mismatches / test_sample
    return error_rate

# Main function
def run_bb84_simulation(n_bits=100, simulate_eve=False):
    print(f"\nRunning BB84 Simulation with {n_bits} qubits")
    
    # Alice generates bits and bases
    alice_bits, alice_bases = generate_bits_and_bases(n_bits)
    qubits = encode_qubits(alice_bits, alice_bases)

    # Eve intercepts and resends (if simulated)
    if simulate_eve:
        qubits = intercept_and_resend(qubits)
        print("  Eve has intercepted the qubits!")
    # Bob chooses bases and measures
    bob_bases = [random.choice(BASES) for _ in range(n_bits)]
    bob_bits = measure_qubits(qubits, bob_bases)

    # Sifting keys
    alice_key, bob_key = sift_key(alice_bits, alice_bases, bob_bits, bob_bases)
    print(f" Key length after sifting: {len(alice_key)} bits")

    # Check for eavesdropping
    error_rate = detect_eavesdrop(alice_key, bob_key)
    print(f" Sample Error Rate: {error_rate * 100:.2f}%")

    if error_rate > 0.2:
        print(" Possible Eavesdropping Detected! Key is not secure.")
    else:
        print(" No eavesdropping detected. Key is secure.")

    # Show final keys
    print(f"\n Final Shared Key (Alice): {alice_key}")
    print(f"Final Shared Key (Bob):   {bob_key}")

# Run the simulation (set simulate_eve=True to test eavesdropping)
run_bb84_simulation(n_bits=50, simulate_eve=False)
