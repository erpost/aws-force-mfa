**Enforce AWS MFA for a User in both the GUI and CLI**

- Attach JSON AWS IAM Policy to User
- Run 'get-session-credentials' to use current AWS Access Keys to pull STS credentials
    - Script will backup current Keys and use STS credentials
- Run 'replace-credentials-file' to move original Keys back

***Tested with Python 3 on MacOS, Mac OS X and Windows 10***