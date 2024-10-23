# CrewAI is great! ... but

... getting start is hard. I'm a seasoned developer and using AzureOpenAI with CrewAI when it's always being updated is tricky. This repo is designed to demostrate how to use the (almost) latest version of CrewAI with AzureOpenAI.

## Instructions

I've set up github codespaces. A few things: Chroma requires a modern version of sqlite3. The universal githubcodespace comes with a very old version of sqlite3 and uses conda for python. Very confusing. Even if we install python again, it will still take the old sqlite3 version. Also, the python docker image itself *also* has an old version of sqlite3. So, we need to use ubuntu as our base image and install python3 in the codespace.