Assertion methods - Intro

In the unittest framework in Python, assertion methods are special methods provided by the framework that allow you to check whether specific conditions are met during the execution of your test cases. These assertion methods are used to validate the behavior of your code and ensure that it produces the expected results.



Here's an overview of some commonly used assertion methods in unittest:

assertEqual(first, second, msg=None):

This method checks if first and second are equal. If they are not, it raises an AssertionError with an optional msg message. Useful for testing if two values or objects are expected to be equal.

assertNotEqual(first, second, msg=None):

This method checks if first and second are not equal. If they are equal, it raises an AssertionError with an optional msg message. Useful for testing if two values or objects are expected to be different.

assertTrue(expr, msg=None):

This method checks if expr evaluates to True. If expr is False, it raises an AssertionError with an optional msg message. Useful for verifying that a condition is true.

assertFalse(expr, msg=None):

This method checks if expr evaluates to False. If expr is True, it raises an AssertionError with an optional msg message. Useful for verifying that a condition is false.

assertIsNone(obj, msg=None):

This method checks if obj is None. If obj is not None, it raises an AssertionError with an optional msg message. Useful for verifying that an object is None.

assertIsNotNone(obj, msg=None):

This method checks if obj is not None. If obj is None, it raises an AssertionError with an optional msg message. Useful for verifying that an object is not None.

assertRaises(exception, callable, *args, **kwargs):

This method checks if calling callable with the specified arguments raises an exception of type exception. If the expected exception is not raised, it raises an AssertionError. This is useful for testing exception handling.

assertIn(member, container, msg=None):

This method checks if member is present in container. If member is not in container, it raises an AssertionError with an optional msg message. Useful for testing membership in lists, sets, and other collections.

assertNotIn(member, container, msg=None):

This method checks if member is not present in container. If member is in container, it raises an AssertionError with an optional msg message. Useful for testing that an element is not in a collection.



These are some of the commonly used assertion methods in unittest. They help you write test cases that check various conditions and verify the correctness of your code. When an assertion fails, the test framework raises an AssertionError with an optional message, making it easy to identify which test case failed and why. Using these assertion methods, you can systematically validate the behavior of your code and ensure that it meets the expected specifications and requirements.