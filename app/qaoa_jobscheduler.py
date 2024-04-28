from qiskit import Aer, execute
from qiskit.circuit import QuantumCircuit, Parameter
from qiskit import algorithms
from qiskit_optimization import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit.algorithms import QAOA
from qiskit.utils import QuantumInstance


class QAOAJobScheduler():
    def __init__(self, anaylzer, jobs = 7, machines = 3, timecount = 3):
        self.jobs = jobs
        self.machines = machines
        self.timecount = timecount
        self.result = None

    def get_result(self):
        if (self.result is None):
            print("Please run the QAOA Job Scheduluer first")
        return self.result
    
    def run(self):
        if (self.jobs < 1 or self.machines < 1 or self.timecount < 1):
            print("Please provide valid values for the number of jobs, machines and time slots")
            return
        
        #Step 2: Define the Quadratic Program
        # Define the Quadratic Program
        qp = QuadraticProgram()


        # Add binary variables for each job-timeslot combination
        for i in range(1, self.machines+1):  # For 3 jobs
            for j in range(1, self.jobs+1):  # For 2 timeslots
                for k in range(1,self.timecount+1):
                    qp.binary_var(f'machine{i}job{j}time{k}')

        # Define the objective function (minimize the total duration)
        # For simplicity, we'll assume each job has a unit duration
        linear = {}
        for i in range(1, self.machines+1):
            for j in range(1, self.jobs+1):
                for k in range(1, self.timecount+1):
                    linear [f'machine{i}job{j}time{k}'] = 1
        qp.minimize(linear=linear)


            
        # 
        for i in range(1, self.timecount+1):
            job_vars = {f'machine{j}job{k}time{i}': 1 for j in range(1, self.machines+1) for k in range(1, self.jobs+1)}
            rhs= max(min(self.jobs-(self.machines*(i-1)), self.machines), 0)   
            # 7 3 7/3=2 7%3=2 i<7/3 ?
            qp.linear_constraint(linear=job_vars, sense='==', rhs= rhs)  # all variables for a machine and time must sum to 1
                            
        # all self.jobs are ran once: for job i, sum(machine_jjob_itime_k)=duration of job i,and sum on each machine for job i except for 1 should be 0
        for i in range(1, self.jobs+1): # iterating over self.machines
            job_vars = {f'machine{k}job{i}time{j}': 1 for k in range(1, self.machines+1) for j in range(1, self.timecount+1)}  # create a dict comprehension for all self.jobs
            qp.linear_constraint(linear=job_vars, sense='==', rhs=1)  # all variables for a machine and time must sum to 1

        # no intersection of intervals: for machine i and time j , sum(machine_ijob_ktime_j) for all k self.jobs must be 1
        for i in range(1, self.machines+1):      # iterating over self.machines
            for j in range(1, self.timecount+1):  # iterating over time slots
                job_vars = {f'machine{i}job{k}time{j}': 1 for k in range(1, self.jobs+1)}  
                qp.linear_constraint(linear=job_vars, sense='<=', rhs=1)  # all variables for a machine and time must sum to 1
            

        # Set up the QAOA algorithm
        qaoa = QAOA(quantum_instance=QuantumInstance(Aer.get_backend('qasm_simulator')))

        # Use the MinimumEigenOptimizer to solve the QUBO with QAOA
        optimizer = MinimumEigenOptimizer(qaoa)
        result = optimizer.solve(qp)

        self.result = result
        print(result)
        return result

if __name__ == "__main__":
    qaoa = QAOAJobScheduler()
    qaoa.run()




