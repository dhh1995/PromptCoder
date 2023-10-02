# PromptCoder

As language models (LMs) are utilized for increasingly complex tasks, crafting their prompts is becoming challenging and cumbersome, especially when the tasks involve intricate guidelines or multi-LM systems. 

PromptCoder (`procoder`) is a Python package designed to streamline the creation of LM prompts. 
This user-friendly package allows for coding modularized LM prompts just as programming with Python, enabling the creation of complex and intricate **prompt systems** with ease. 

Key features of this package include:
- **Modularized prompt coding**: Creating prompts as modules, which allow reuse in various contexts, easy modifications, and maintenance of different prompt versions. Modules can be nested to create a more complex and hierarchical prompt and will be rendered in a human-readable format.
- **Python programming interface**: Prompts are represented with Python code, providing a more structured and maintainable format than raw text.
- **Cross-referencing**: Define elements in your prompt as variables and refer to them thereafter, enabling easy cross-referencing of different parts of the prompt. The structure of forward referencing could potentially be more compatible with the auto-regressive nature of current LMs.

By using the `procoder` package, we developed and maintained a system of prompts that has **in total more than 20k tokens** in the [ToolEmu](https://github.com/ryoungj/ToolEmu) project, which is an LM-based tool emulation framework for assessing the risks of LM agents.

**Note that the package is still in its early stages and under active development.**

## Installation
```bash
git clone https://github.com/dhh1995/PromptCoder
cd PromptCoder
pip install -e .
```

## Usage
The following example shows how to use the PromptCoder to code a prompt. The example uses the modules implemented in the `procoder.prompt` package. The output prompt is shown below the code.

```python
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
```

The output of the first prompt is:
```markdown
## Requirements
1. Input Requirement: The input should be two numbers.
2. Output Requirement: The output should be the sum of the two numbers.

## Instruction
Write a function in python that satisfies the [Input Requirement] and [Output Requirement].
```
The output of the second prompt is:
```markdown
## Requirements
1. Input Requirement: The input should be two numbers.
2. Output Requirement: The output should be the multiplication of the two numbers.

## Instruction
Write a function in python that satisfies the [Input Requirement] and [Output Requirement].
```

For more examples, please refer to the [ToolEmu prompts](https://github.com/ryoungj/ToolEmu/tree/main/toolemu/prompts) that was developed using the `procoder` package.


## Contributors
- Honghua Dong [@dhh1995](https://github.com/dhh1995)
- Yangjun Ruan [@ryoungj](https://github.com/ryoungj)
