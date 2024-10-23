# CrewAI is great! ... but

... getting started is hard. I'm a seasoned developer and using AzureOpenAI with CrewAI when it's always being updated is tricky. This repo is designed to demonstrate how to use the (almost) latest version of CrewAI with AzureOpenAI.

## Explanation

* This devcontainer has been carefully set up to use the right python and sqlite3 versions.
* This project has been set up as per the [CrewAI Quickstart](https://docs.crewai.com/quickstart).
* Effectively, only the `azure_llm.py` file has been added
* `crew.py` has been updated to reference the `azure_llm.py` file.

## Instructions

1. Clone this repo
2. Run in GitHub codespaces (or locally, but instructions are for codespaces)
3. In `/latest_ai_development/src/latest_ai_development/azure_llm.py` replace the `AZURE_API_KEY` and `AZURE_API_BASE` and `AZURE_API_VERSION` and `DEPLOYMENT_NAME` with your own values.
4. As per the [CrewAI Quickstart](https://docs.crewai.com/quickstart), cd into the `latest_ai_development` directory and run `crewai install`
5. Run `crewai run` to start the CrewAI crew

## Notes

I've set up GitHub codespaces as a few things: Chroma requires a modern version of sqlite3. At time of writing (Oct 2024) the universal GitHub codespace comes with Ubuntu LTS 20 and very old version of sqlite3 and uses conda for python. Very confusing; even if we install python again, it will still take the old sqlite3 version. Also, if we swap the universal codespaces image with the python docker image, it *also* has an old version of sqlite3. So, we need to use a modern Ubuntu version as our base image and install python3 in the codespace using features.

I've added a `requirements.txt` which is the most important file as it tracks the latest *working* version of CrewAI. It will lag behind the actual latest version of CrewAI until I've had time to test the very latest version actually works.