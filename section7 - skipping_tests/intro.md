Skipping tests - Intro

In the unittest framework in Python, you can skip specific test cases or test methods when they are not applicable or when they are expected to fail for some reason. Skipping tests is useful in situations where you want to exclude certain tests temporarily or when they are not relevant to the current test run. Here's how you can skip tests in unittest:



Skipping Test Methods: To skip a specific test method, you can use the @unittest.skip() decorator. This decorator can be applied to individual test methods, marking them as skipped.

import unittest
 
class MyTestCase(unittest.TestCase):
 
    @unittest.skip("Skipped for demonstration purposes")
    def test_skip_example(self):
        # Test code that would be skipped
        pass
 
    def test_normal_case(self):
        # Regular test case
        pass


In this example, the test_skip_example method is marked with @unittest.skip, and it won't be executed when you run the test suite.



Conditional Skipping: You can also conditionally skip test methods based on certain criteria using the @unittest.skipIf and @unittest.skipUnless decorators. These decorators allow you to skip a test method depending on a specified condition.

import unittest
 
class MyTestCase(unittest.TestCase):
 
    @unittest.skipIf(1 + 1 != 2, "Skipped if 1 + 1 is not 2")
    def test_skip_if_example(self):
        # Test code that would be skipped based on the condition
        pass
 
    @unittest.skipUnless(2 + 2 == 4, "Skipped unless 2 + 2 is 4")
    def test_skip_unless_example(self):
        # Test code that would be skipped based on the condition
        pass


In this example, the test_skip_if_example method will be skipped if the condition 1 + 1 != 2 evaluates to True. Similarly, the test_skip_unless_example method will be skipped unless the condition 2 + 2 == 4 evaluates to True.



Skipping the Entire Test Case: You can skip the execution of an entire test case by using the @unittest.skip() decorator at the class level. This will skip all test methods within that test case.

import unittest
 
@unittest.skip("Entire test case is skipped")
class MyTestCase(unittest.TestCase):
 
    def test_example1(self):
        # This test method is skipped
        pass
 
    def test_example2(self):
        # This test method is skipped
        pass


In this case, both test_example1 and test_example2 will be skipped because the entire test case is marked as skipped.



Skipping with a Reason: It's a good practice to provide a reason when skipping a test method or test case. This reason helps communicate why the test is skipped, making it easier for developers to understand the intent behind the skip.



Skipped tests can be useful in scenarios like:

Dealing with incomplete or work-in-progress code.

Ignoring tests for platform-specific behavior.

Excluding tests that require specific dependencies.

Skipping tests that are expected to fail due to known issues.



To run tests with skips, you can use the -k option with unittest to specify patterns of test methods or test cases to run or skip based on their names or attributes. This allows you to control which tests are executed in different testing scenarios.