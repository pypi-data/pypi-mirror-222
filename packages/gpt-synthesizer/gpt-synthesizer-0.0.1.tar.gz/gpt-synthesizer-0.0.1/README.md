# GPT Synthesizer

**Collaboratively build an entire codebase for any project with the help of an AI.**

GPT Synthesizer takes a programming task and analyzes every component of your software that needs to be implemented. Powered by [LangChain](https://python.langchain.com/docs/get_started/introduction), human feedback will be used to ***dynamically synthesize prompts*** for code generation. Our human-in-the-loop approach ensures maximal alignment of the generated code with your needs.

## Installation

- `pip install gpt-synthesizer`

- For development:
  - `git clone https://github.com/RoboCoachTechnologies/GPT-Synthesizer.git`
  - `cd gpt-synthesizer`
  - `pip install -e .`

## Usage

- Start GPT Synthesizer by typing `gpt-synthesizer` in the terminal.
- Briefly tell your programming task and the implementation language:
  - `Programming task: *I want to implement an edge detection method from live camera feed.*`
  - `Programming language: *python*`
- GPT Synthesizer will analyze your task and suggest a set of components needed for the implementation.
  - You can add more components by listing them in quotation marks: `Components to be added: *Add 'component 1: what component 1 does', 'component 2: what component 2 does', and 'component 3: what component 3 does' to the list of components.*`
  - You can remove any redundant component in a similar manner: `Components to be removed: *Remove 'component 1' and 'component 2' from the list of components.*`
- After you are done with modifying the component list, GPT Synthsizer will start asking questions in order to find all the details needed for implementing each component.
- When GPT Synthesizer learns about your specific requirements for each component, it will write the code for you!

## What makes GPT Synthesizer unique?

The design for GPT Synthesizer is rooted in the core, and rather contrarian, belief that a single prompt is not enough to build a complete codebase. This is mainly due to the fact that, even in presence of powerful LLMs, there are still many crucial implementation aspects which can only be captured via detailed conversations between a human user and an AI.

In particular, GPT Synthesizer takes a high-level description of a programming task and finds all the components a user might need for implementation. This step essentially turns 'unknown unknowns' into 'known unknowns', which can be very helpful for novice programmers who want to understand an overall flow of their desired implementation. Next, GPT Synthesizer and the user ***collaboratively*** find out the design details that will be eventually used in the implementation of each program component.

GPT Synthesizer distinguishes itself from other LLM-based code generation tools by maximizing interaction between the AI assistant and the user. However, it is acknowledged that users can come from diverse programming skill levels; hence, each of them might prefer a different level of interactivity with the AI assistant. GPT Synthesizer finds the right balance between user partcipation and AI autonomy through evaluating the informativeness of user's prompts.

## Make your own GPT Synthesizer!

In addition to the easy to use AI assistant interface, GPT Synthesizer is made with a very simple structure so that anyone can customize the code for their specific applications. Most importantly, the codebase is tightly integrated with [LangChain](https://python.langchain.com/docs/get_started/introduction), allowing utilization of various tools such as [internet search](https://python.langchain.com/docs/integrations/tools/ddg) and [vector databases](https://python.langchain.com/docs/modules/memory/types/vectorstore_retriever_memory).

GPT Synthesizer's hierarchical strategy to build the codebase allows using OpenAI's GPT3.5 as a viable choice for the backend LLM, which is currently the default model. We believe GPT3.5 provides a good trade-off between cost and contextual understanding, while GPT4 might be too expensive for many users. Nevertheless, [switching to another LLM](https://python.langchain.com/docs/integrations/llms/) is made easy thanks to LangChain integration.

## Roadmap

GPT Synthesizer will be actively maintained as an open-source project. We welcome everyone to contribute to our community of building systems for human-in-the-loop code generation!

Here is a (non-exhaustive) list of our future plans for GPT Synthesizer:

- An additional step in code generation that ensures creating a main/entrypoint.
- Creating setup instructions based on the programming language, e.g. `CMakelists.txt` for C++ and `setup.py`+`requirements.txt` for python.
- Adding benchmarks and testing scripts.
