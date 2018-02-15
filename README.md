**Tested with Python 3 on MacOS, Mac OS X and Windows 10**

- With associated AWS IAM Policy (json) attached, a user must enable MFA in order to see any resources in the console and CLI

- Run 'get-session-credentials' to use current AWS Access Keys to pull STS credentials
    - Script will backup current Keys and use STS credentials
- Run 'replace-credentials-file' to move original Keys back
