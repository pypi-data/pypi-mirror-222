"""
description: this provides the class FactoryTestSuite.
"""
import os
import subprocess
import time
from pathlib import Path

from pistar_echo_agent.utilities.constants.testcase import TEST_CASE, TEST_SUITE
from pistar_echo_agent.utilities.constants.testcase import FAIL_REASON
from pistar_echo_agent.utilities.testsuite.directory import Directory


class FactoryTestSuite:
    """
    description: this class is used to manage the testsuite sent by cloud test.
    """
    testcases_information = None
    logger = None
    stop = None
    __execute_testcase = None
    __execute_mode = None
    __exception_count = None
    __testcase_timeout = None
    exception_timeout = None
    exception_pause = None
    exception_stop = None
    exception_install = None
    fail_reason = None
    process = None
    process_return_code = None

    def __init__(
            self,
            testcases_information,
            script_root_path,
            logger,
            execute_mode,
            report_path,
            testcase_timeout=None
    ):
        self.logger = logger
        self.testcases_information = testcases_information
        self.script_root_path = script_root_path
        self.report_path = str(report_path)
        self.__execute_mode = execute_mode
        self.stop = False
        self.__exception_count = 0
        self.__testcase_timeout = testcase_timeout

    def execute(self):
        """
        description: this function is used to execute the testsuite.
        """
        if self.install_requirements() is False:
            return
        # 根据用例类型执行用例
        for testcase_type in self.testcases_information:
            if self.stop:
                self.logger.info("Stop flag is true, now stop the process.")
                return
            testcases = self.testcases_information[testcase_type]
            # 判断是否弹出异常
            is_execute_success = self.__execute_testcases(testcases, testcase_type, self.__execute_mode)
            if is_execute_success is False:
                self.exception_stop = True
                self.logger.info("Exception stop, now stop current task.")
                return

    def install_requirements(self):
        require_path = Path(self.script_root_path).joinpath("requirements.txt")
        if not require_path.exists():
            self.logger.warning("There is no requirements in the project.")
            return True
        command = ["pip3", "install", "-r", "requirements.txt"]
        with Directory(self.script_root_path):
            try:
                subprocess.run(
                    command,
                    env=os.environ,
                    check=True,
                    encoding="utf8",
                    timeout=100,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
            except subprocess.TimeoutExpired:
                self.logger.error("pip install run timeout.")
                self.exception_install = True
                self.fail_reason = FAIL_REASON.INSTALL_TIMEOUT
                return False
            except subprocess.CalledProcessError as exc:
                self.logger.error(f"pip install error.\n {exc.stderr}")
                self.exception_install = True
                self.fail_reason = f"{FAIL_REASON.INSTALL_ERROR}\n{exc.stderr}"
                return False
        self.logger.info("pip install success.")
        return True

    def __execute_testcases(self, testcases, testcase_type, execute_mode):
        command = self.get_testcase_execution_command(testcases, testcase_type, execute_mode)
        with Directory(self.script_root_path):
            self.process = subprocess.Popen(
                command,
                env=os.environ,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            # Set process timeout 2 hour temporarily.
            try:
                self.process.communicate(timeout=7200)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.logger.error("Test cases execute timeout.")
                # Set the timeout flag and set test cases result is timeout.
                self.exception_timeout = True
                return True
            self.process_return_code = self.process.returncode
            if self.stop is True:
                return True
            if self.process.returncode != 0:
                self.logger.warning("Test cases execute have some exceptions, now set exception pause.")
                self.exception_pause = True
                return False

        self.logger.info("pistar test cases execute completed.")
        return True

    def get_testcase_execution_command(self, testcases, testcase_type, execute_mode):
        command = ["pistar", "run"]
        for testcase in testcases:
            command.append(testcase[TEST_CASE.ABS_PATH])
        if testcase_type in [TEST_CASE.PYTEST, TEST_CASE.UITEST]:
            command += ['--type', 'pytest']
        else:
            if self.__testcase_timeout:
                second = self.__testcase_timeout/1000
                command += ['--case_timeout', str(second)]

        command += ['-o', self.report_path]
        # 并行模式下添加-n 参数, 去掉debug参数，防止并行模式下因为debug参数导致的进程异常退出
        if execute_mode == TEST_SUITE.PARALLEL_MODE:
            command += ['-n', 'auto']
        else:
            command += ['--debug']

        self.logger.info(f"Current command is: {command}")
        return command

    def kill_process(self):
        if self.process:
            self.process.kill()
