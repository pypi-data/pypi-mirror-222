""" Binary runner and results classes.
"""
import copy
from typing import List, Optional, Union
from pathlib import Path
import os
import subprocess
import shutil
import time
import enum


from excitingtools.utils.jobflow_utils import special_serialization_attrs


class RunnerCode(enum.Enum):
    """ Runner codes.
     By default, the initial value starts at 1.
    """
    time_out = enum.auto


class SubprocessRunResults:
    """ Results returned from subprocess.run()
    """

    def __init__(self,
                 stdout,
                 stderr,
                 return_code: Union[int, RunnerCode],
                 process_time: Optional[float] = None):
        self.stdout = stdout
        self.stderr = stderr
        self.return_code = return_code
        self.success = return_code == 0
        self.process_time = process_time


class BinaryRunner:
    """ Class to execute a subprocess.
    """
    path_type = Union[str, Path]

    def __init__(self,
                 binary: str,
                 run_cmd: Union[List[str], str],
                 omp_num_threads: int,
                 time_out: int,
                 directory: Optional[path_type] = './',
                 args=None) -> None:
        """ Initialise class.

        :param str binary: Binary name prepended by full path, or just binary name (if present in $PATH).
        :param Union[List[str], str] run_cmd: Run commands sequentially as a list. For example:
          * For serial: ['./'] or ['']
          * For MPI:   ['mpirun', '-np', '2']
        or as a string. For example"
          * For serial: "./"
          * For MPI: "mpirun -np 2"
        :param int omp_num_threads: Number of OMP threads.
        :param int time_out: Number of seconds before a job is defined to have timed out.
        :param List[str] args: Optional arguments for the binary.
        """
        if args is None:
            args = []
        self.binary = binary
        self.directory = directory
        self.run_cmd = run_cmd
        self.omp_num_threads = omp_num_threads
        self.time_out = time_out
        self.args = args

        if not os.path.isfile(self.binary):
            # If just the binary name, try checking the $PATH
            self.binary = shutil.which(self.binary)
            if not self.binary:
                raise FileNotFoundError(
                    f"{binary} binary is not present in the current directory nor in $PATH"
                )

        if not Path(directory).is_dir():
            raise OSError(f"Run directory does not exist: {directory}")

        if isinstance(run_cmd, str):
            self.run_cmd = run_cmd.split()
        elif not isinstance(run_cmd, list):
            raise ValueError(
                "Run commands expected in a str or list. For example ['mpirun', '-np', '2']"
            )

        self._check_mpi_processes()

        if omp_num_threads <= 0:
            raise ValueError("Number of OMP threads must be > 0")

        if time_out <= 0:
            raise ValueError("time_out must be a positive integer")

    def as_dict(self) -> dict:
        """Returns a dictionary representing the current object for later recreation.
        The serialise attributes are required for recognition by monty and jobflow.
        """
        serialise_attrs = special_serialization_attrs(self)
        return {**serialise_attrs, **self.__dict__}

    @classmethod
    def from_dict(cls, d: dict):
        my_dict = copy.deepcopy(d)
        # Remove key value pairs needed for workflow programs
        # call function on class to get only the keys (values not needed)
        serialise_keys = special_serialization_attrs(cls)
        for key in serialise_keys:
            my_dict.pop(key, None)
        return cls(**my_dict)

    def _check_mpi_processes(self):
        """ Check whether mpi is specified and if yes that the number of MPI processes specified is valid.
        """
        # Search if MPI is specified:
        try:
            i = self.run_cmd.index('-np')
        except ValueError:
            # .index will return ValueError if 'np' not found. This corresponds to serial and omp calculations.
            return
        try:
            mpi_processes = int(self.run_cmd[i + 1])
        except IndexError:
            raise ValueError("Number of MPI processes must be specified after the '-np'")
        except ValueError:
            raise ValueError("Number of MPI processes should be an int")
        if mpi_processes <= 0:
            raise ValueError("Number of MPI processes must be > 0")

    def _compose_execution_list(self) -> list:
        """Generate a complete list of strings to pass to subprocess.run(), to execute the calculation.

        For example, given:
          ['mpirun', '-np, '2'] + ['binary.exe'] + ['>', 'std.out']

        return ['mpirun', '-np, '2', 'binary.exe', '>', 'std.out']
        """
        run_cmd = self.run_cmd

        if self.run_cmd[0] == './':
            run_cmd = []

        return run_cmd + [self.binary] + self.args

    def run(self) -> SubprocessRunResults:
        """Run a binary.
        """
        execution_list = self._compose_execution_list()
        my_env = {**os.environ, "OMP_NUM_THREADS": str(self.omp_num_threads)}

        time_start: float = time.time()
        try:
            result = subprocess.run(execution_list,
                                    env=my_env,
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE,
                                    timeout=self.time_out,
                                    cwd=self.directory)
            total_time = time.time() - time_start
            return SubprocessRunResults(result.stdout, result.stderr,
                                        result.returncode, total_time)

        except subprocess.TimeoutExpired as timed_out:
            error = 'BinaryRunner: Job timed out. \n\n'
            if timed_out.stderr:
                error += timed_out.stderr.decode("utf-8")
            return SubprocessRunResults(timed_out.output, error,
                                        RunnerCode.time_out, self.time_out)
