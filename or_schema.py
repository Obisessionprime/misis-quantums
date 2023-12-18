# Creating qbit register for 3 quantum bits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, BasicAer

for qbits_initial in ('00', '01', '10', '11'):

    qbit_register = QuantumRegister(3)

    # Creating classical register to store measure results
    classical_register = ClassicalRegister(3)

    # Circuit for algorithm execution
    circuit = QuantumCircuit(qbit_register, classical_register)

    circuit.initialize('0' + qbits_initial, qbit_register)
    circuit.cx(0, 2)
    circuit.cx(1, 2)
    circuit.ccx(0, 1, 2)

    circuit.measure(2, 2)

    result = execute(experiments=circuit, backend=BasicAer.get_backend('qasm_simulator'),).result()

    print(circuit)
    print(result.get_counts())
