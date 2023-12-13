from qiskit import QuantumCircuit
from qiskit import ClassicalRegister
from qiskit import QuantumRegister
from qiskit import execute
from qiskit import BasicAer

from bell_updater import BellStateUpdater


class TeleportingUpdater:
    """"""

    def __init__(self, qbits: QuantumRegister, circuit: QuantumCircuit) -> None:
        """
        Initial method for bell state updater
        :param qbits:
        :param circuit:
        """
        self._qbits = qbits
        self._circuit = circuit

    def teleport(self, teleport_from, transport_qbit, teleport_to, barriers: bool = True):
        """"""
        BellStateUpdater(qbits=self._qbits, circuit=self._circuit).bell_phi_plus(
            qbit_indexes=[transport_qbit, teleport_to]
        )
        if barriers:
            self._circuit.barrier()
        self._circuit.cx(control_qubit=teleport_from, target_qubit=transport_qbit)
        self._circuit.h(teleport_from)
        if barriers:
            self._circuit.barrier()

        self._circuit.measure(teleport_from, teleport_from)
        self._circuit.measure(transport_qbit, transport_qbit)

        if barriers:
            self._circuit.barrier()

        self._circuit.cx(control_qubit=transport_qbit, target_qubit=teleport_to)
        self._circuit.cz(control_qubit=teleport_from, target_qubit=teleport_to)


# Creating qbit register for 3 quantum bits
qbit_register = QuantumRegister(3)

# Creating classical register to store measure results
classical_register = ClassicalRegister(3)

# Circuit for algorithm execution
circuit = QuantumCircuit(qbit_register, classical_register)

TeleportingUpdater(qbits=qbit_register, circuit=circuit).teleport(teleport_from=0, transport_qbit=1, teleport_to=2)

circuit.measure(2, 2)

print(circuit)

result = execute(experiments=circuit, backend=BasicAer.get_backend('qasm_simulator'), ).result()

print(result.get_counts())
