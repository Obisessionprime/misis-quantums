# Creating qbit register for 3 quantum bits
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, execute, BasicAer

for initial_state in ('0', '1'):
    qbit_register = QuantumRegister(2)

    # Creating classical register to store measure results
    classical_register = ClassicalRegister(2)

    # Circuit for algorithm execution
    circuit = QuantumCircuit(qbit_register, classical_register)

    circuit.initialize('0' + initial_state, qbit_register)
    circuit.x(0)
    circuit.cx(control_qubit=0, target_qubit=1)
    circuit.x(0)
    circuit.measure(0, 0)
    circuit.measure(1, 1)
    result = execute(experiments=circuit, backend=BasicAer.get_backend('qasm_simulator'),).result()

    print(circuit)
    print(result.get_counts())
