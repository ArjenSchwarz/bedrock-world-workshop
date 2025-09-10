# Preparing for our journey

Before we can get to build our game, we need to get the boring stuff out of the way.

## Assumptions

This workshop assumes the following:

- You have access to an AWS account with sufficient permissons to run everything mentioned here
- You have access to a CLI to run Python commands
- You have access to a text editor

## Get access to the models

We'll be working in the Sydney region, as that is one of the 3 regions that AgentCore is currently available. If you have already requested access to any models you may want to use, that's great! Otherwise, follow the below steps:

1. Go to the model access page in the Bedrock Console [here](https://ap-southeast-2.console.aws.amazon.com/bedrock/home?region=ap-southeast-2#/modelaccess).
2. Click on Modify Model access
3. Select the models you want to use. The examples in the repo use Amazon's Nova Lite, so if you want to use these steps make sure to select that model at the very least.

## Install local tools for running agents

### The starter toolkit

First we need to ensure we can use the agentcore starter kit as described on [the getting started page](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/getting-started-starter-toolkit.html)

```bash
pip install --upgrade pip

pip install bedrock-agentcore strands-agents bedrock-agentcore-starter-toolkit mcp
```

The examples are written in Python, if you want to run things locally, you'll need some things installed there too.

The above installed the dependencies using pip globally, but the below uses uv so you have more control over what's installed. If you're happy to skip using environments and/or are confident in your Python skills, you can ignore this.

### Agents Prerequisites
- Ensure you have `uv` installed on your system (see [installation instructions](https://docs.astral.sh/uv/getting-started/installation/))
- Python 3.13 or higher

### 1. Navigate to the directory you want to build your agents
```bash
cd agents
```

### 2. Create a virtual environment with Python 3.13
```bash
uv venv --python 3.13
```

### 3. Activate the virtual environment
```bash
source .venv/bin/activate
```

And that should be it for the boring bits.