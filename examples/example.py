from procoder.functional import format_prompt, replaced_submodule
from procoder.prompt import *

requirements = NamedBlock(
    "Requirements",
    Collection(
        NamedVariable(
            refname="input_req",
            name="Input Requirement",
            content="The input should be two numbers.",
        ),
        NamedVariable(
            refname="output_req",
            name="Output Requirement",
            content=Single(
                "The output should be the sum of the two numbers."
            ).set_refname("output_req_content"),
        ),
    ),
)
instruction = NamedBlock(
    "Instruction",
    "Write a function in {language} that satisfies the {input_req} and {output_req}.",
)
prompt = (
    Collection(requirements, instruction)
    .set_sep("\n\n")
    .set_indexing_method(sharp2_indexing)
)
another_prompt = replaced_submodule(
    prompt,
    "output_req_content",
    Single("The output should be the multiplication of the two numbers."),
)

inputs = {"language": "python"}
print("First prompt:")
print(format_prompt(prompt, inputs))
print("")
print("Second prompt:")
print(format_prompt(another_prompt, inputs))
