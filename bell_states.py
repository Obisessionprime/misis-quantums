from qiskit import QuantumCircuit
from qiskit import ClassicalRegister
from qiskit import QuantumRegister
from qiskit import execute
from qiskit import BasicAer

from bell_updater import BellStateUpdater

bell_states = ('bell_phi_plus', 'bell_phi_minus', 'bell_psi_plus', 'bell_psi_minus')


# Iteration over created states
for bell_state in bell_states:
    qbit_register = QuantumRegister(2)
    classical_register = ClassicalRegister(2)
    circuit = QuantumCircuit(qbit_register, classical_register)

    bell_state_updater = BellStateUpdater(qbits=qbit_register, circuit=circuit)

    getattr(bell_state_updater, bell_state)()

    # Measuring qbits to classical bit registers
    for index, qbit in enumerate(qbit_register):
        circuit.measure(qubit=qbit_register[index], cbit=classical_register[index])

    # Printout the circuit image
    print(circuit)

    result = execute(experiments=circuit, backend=BasicAer.get_backend('qasm_simulator'),).result()

    print(result.get_counts())
