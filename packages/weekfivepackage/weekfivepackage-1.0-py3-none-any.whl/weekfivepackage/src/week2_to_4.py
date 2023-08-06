from functools import reduce
from ctypes import CDLL, c_int
import asyncio


def squared_numbers(numbers):
    return list(map(lambda x: x**2, numbers))


def even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def numbers_sum(numbers):
    return reduce(lambda x, y: x + y, numbers)


def call_async():
    async def task():
        print("Task started.")
        await asyncio.sleep(2)
        print("Task completed.")

    async def main():
        print("Main function started.")
        loop = asyncio.get_event_loop()
        task1 = loop.create_task(task())
        task2 = loop.create_task(task())
        await asyncio.gather(task1, task2)
        print("Main function completed.")

    asyncio.run(main())


def ctype_example():
    c_lib = CDLL("./c_library/add.dll")
    c_lib.add.argtypes = [c_int, c_int]
    c_lib.add.restype = c_int
    c_lib = CDLL("./c_library/add.dll")
    result_add = c_lib.add(5, 3)
    print(f"Using ctypes - add result: {result_add}")

    cpp_lib = CDLL("./c++_library/multiply.dll")
    cpp_lib.multiply.argtypes = [c_int, c_int]
    cpp_lib.multiply.restype = c_int
    result_multiply = cpp_lib.multiply(5, 3)
    print(f"Using ctypes - multiply result: {result_multiply}")
