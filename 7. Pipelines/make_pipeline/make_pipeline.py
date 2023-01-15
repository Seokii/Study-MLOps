import kfp
from kfp.components import create_component_from_func
from kfp.dsl import pipeline

@create_component_from_func
def print_and_return_number(number: int) -> int:
    print(number)
    return number

@create_component_from_func
def sum_and_print_numbers(number_1: int, number_2: int) -> int:
    sum_num = number_1 + number_2
    print(sum_num)
    return sum_num

@pipeline(name="example_pipeline")
def example_pipeline(number_1: int, number_2: int):
    number_1_result = print_and_return_number(number_1)
    number_2_result = print_and_return_number(number_2)
    sum_result = sum_and_print_numbers(
        number_1=number_1_result.output, number_2=number_2_result.output
    )

if __name__ == "__main__":
    kfp.compiler.Compiler().compile(example_pipeline, "example_pipeline.yaml")