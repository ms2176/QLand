from qiskit import Aer, execute
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit.utils import QuantumInstance
from math import ceil


class QAOAJobScheduler:
    def __init__(self, resources: dict, machines: int = 3):
        self.jobs = len(resources)
        self.machines = machines
        self.timecount = ceil(sum(resources.values()))
        self.result = None

    def get_result(self):
        # Ensures that results are available and returns them
        if self.result is None:
            self.run()
        return self.result

    def run(self):
        """Run the quantum scheduler to optimize the schedule of execution over multiple machines

        Returns:
            dic: a key-value pair, where the machine, job and timeslot are the key, and a boolean value indicating whether to run the job in that case or not
        """
        if self.jobs < 1 or self.machines < 1 or self.timecount < 1:
            print(
                "Please provide valid values for the number of jobs, machines and time slots"
            )
            return

        # Define the Quadratic Program
        qp = QuadraticProgram()

        # Add binary variables for each job-timeslot combination
        for i in range(1, self.machines + 1):  # For 3 jobs
            for j in range(1, self.jobs + 1):  # For 2 timeslots
                for k in range(1, self.timecount + 1):
                    qp.binary_var(f"machine{i}job{j}time{k}")

        # Define the objective function (minimize the total duration)
        # For simplicity, we'll assume each job has a unit duration
        linear = {}
        for i in range(1, self.machines + 1):
            for j in range(1, self.jobs + 1):
                for k in range(1, self.timecount + 1):
                    linear[f"machine{i}job{j}time{k}"] = 1
        qp.minimize(linear=linear)

        # Ensure that all machines are busy while jobs are still available
        for i in range(1, self.timecount + 1):
            job_vars = {
                f"machine{j}job{k}time{i}": 1
                for j in range(1, self.machines + 1)
                for k in range(1, self.jobs + 1)
            }
            rhs = max(min(self.jobs - (self.machines * (i - 1)), self.machines), 0)
            qp.linear_constraint(
                linear=job_vars, sense="==", rhs=rhs
            )  # all variables for a machine and time must sum to 1

        # Ensure all jobs are ran exactly once
        for i in range(1, self.jobs + 1):
            job_vars = {
                f"machine{k}job{i}time{j}": 1
                for k in range(1, self.machines + 1)
                for j in range(1, self.timecount + 1)
            }
            qp.linear_constraint(linear=job_vars, sense="==", rhs=1)

        # Ensure that every timeslot has no more than one job
        for i in range(1, self.machines + 1):
            for j in range(1, self.timecount + 1):
                job_vars = {
                    f"machine{i}job{k}time{j}": 1 for k in range(1, self.jobs + 1)
                }
                qp.linear_constraint(linear=job_vars, sense="<=", rhs=1)

        # Set up the QAOA algorithm
        qaoa = QAOA(quantum_instance=QuantumInstance(Aer.get_backend("qasm_simulator")))

        # Use the MinimumEigenOptimizer to solve the QUBO with QAOA
        optimizer = MinimumEigenOptimizer(qaoa)
        result = optimizer.solve(qp)

        self.result = result
        return result


if __name__ == "__main__":
    # Run and output the results of the scheduler
    qaoa = QAOAJobScheduler({1:1, 2:1, 3:1})
    qaoa.run()

    print(qaoa.result())
