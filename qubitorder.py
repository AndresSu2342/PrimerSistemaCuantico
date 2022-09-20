import matplotlib.pyplot as plt
from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, transpile
from qiskit.providers.aer import QasmSimulator
from qiskit.visualization import plot_histogram

nqb = 7  #numero qubits
nbc = 7  #numero bits clasicos

# Use Aer's qasm_simulator
simulator = QasmSimulator()

qreg_q = QuantumRegister(nqb, 'q')
creg_c = ClassicalRegister(nbc, 'c')
circuit = QuantumCircuit(qreg_q, creg_c)

circuit.x(qreg_q[2])
circuit.barrier()

for x in range(nqb):
    circuit.measure(qreg_q[x], creg_c[nbc-1-x])  #Ciclo para imprimir el circuito en orden correcto

# compile the circuit down to low-level QASM instructions
# supported by the backend (not needed for simple circuits)
compiled_circuit = transpile(circuit, simulator)

# Execute the circuit on the qasm simulator
job = simulator.run(compiled_circuit, shots=1000)

# Grab results from the job
result = job.result()

# Returns counts
counts = result.get_counts(compiled_circuit)
print("\nTotal count for 00 and 11 are:",counts)

# Draw the circuit
print(circuit)

# Plot a histogram
plot_histogram(counts)
plt.show()