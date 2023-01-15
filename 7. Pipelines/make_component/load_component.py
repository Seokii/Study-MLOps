from kfp.components import load_component_from_file

print_and_return_number = load_component_from_file("print_and_return_number.yaml")
print(print_and_return_number(100))

# 출력 결과 값
# TaskSpec(component_ref=ComponentReference(name=None,
# digest='7e049205a01e75b13722bbaee1b8932f7d4d743e25de5301dc77c4f03c745872',
# tag=None, url='print_and_return_number.yaml',
# spec=ComponentSpec(name='Print and return number', description=None, metadata=None,
# inputs=[InputSpec(name='number', type='Integer', description=None,
# default=None, optional=False, annotations=None)],
# outputs=[OutputSpec(name='Output', type='Integer', description=None, annotations=None)],
# implementation=ContainerImplementation(container=ContainerSpec(image='python:3.7',
# command=['sh', '-ec', 'program_path=$(mktemp)\nprintf "%s" "$0" >
# "$program_path"\npython3 -u "$program_path" "$@"\n', 'def print_and_return_number(number):\n
# print(number)\n    return number\n\ndef _serialize_int(int_value: int) -> str:\n
# if isinstance(int_value, str):\n
# return int_value\n    if not isinstance(int_value, int):\n
# raise TypeError(\'Value "{}" has type "{}" instead of int.\'.format(\n
# str(int_value), str(type(int_value))))\n
# return str(int_value)\n\nimport argparse\n_parser =
# argparse.ArgumentParser(prog=\'Print and return number\',
# description=\'\')\n_parser.add_argument("--number", dest="number",
# type=int, required=True, default=argparse.SUPPRESS)\n_parser.add_argument("----output-paths",
# dest="_output_paths", type=str, nargs=1)\n_parsed_args = vars(_parser.parse_args())\n_output_files =
# _parsed_args.pop("_output_paths", [])\n\n_outputs =
# print_and_return_number(**_parsed_args)\n\n_outputs = [_outputs]\n\n_output_serializers = [\n    _
# serialize_int,\n\n]\n\nimport os\nfor idx, output_file in enumerate(_output_files):\n    try:\n
# os.makedirs(os.path.dirname(output_file))\n    except OSError:\n
# pass\n    with open(output_file, \'w\') as f:\n
# f.write(_output_serializers[idx](_outputs[idx]))\n'], args=['--number',
# InputValuePlaceholder(input_name='number'), '----output-paths', OutputPathPlaceholder(output_name='Output')],
# env=None, file_outputs=None)), version='google.com/cloud/pipelines/component/v1')),
# arguments={'number': '100'}, is_enabled=None, execution_options=None, annotations=None)