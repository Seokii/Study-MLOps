from kfp.components import create_component_from_func

@create_component_from_func
def print_and_return_number(number: int) -> int:
    print(number)
    return number

if __name__ == "__main__":
    print_and_return_number.component_spec.save("print_and_return_number.yaml")
