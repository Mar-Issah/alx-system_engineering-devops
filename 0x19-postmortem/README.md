# Postmortem

## I was unable to connect to my remote servers after I created ssh key using Putty

![An image of the command line where repeated ssh attempts result in “port 22: connection refused.”](./connection_issue.png)

## Issue Summary:

Duration: 3 days
Start time: 28 Aug, 2023
End time: 30 Aug, 2023
Impact: Inability to connect to remote server, 268033-web-01, via SSH using the Putty format SSH key. It affected the ability to complete my task on time.

## Root Cause:

The root cause of the issue was the use of a Putty format SSH key instead of an OpenSSH format key. The Putty format key was not compatible with the SSH authentication process, causing the connection failure.

## Timeline:

- 28th Aug,2023 10:00 AM: The issue was detected when I was unable to connect to remote servers using Putty format SSH keys.
- 28th Aug, 2023 1:10 PM: Investigations began to identify the root cause of the authentication issue. Assumptions were made that the SSH server configuration might be misconfigured or the SSH keys might be expired.
- 28th Aug,2023 8:20 PM: Debugging efforts focused on checking the SSH server configuration and verifying the expiration status of the SSH keys.
- 29th Aug, 2023: Attempted to converted generated keys into Open SSH format. I successfully converted it into the format, yet connection still kept failing.

Tasks:

Conduct regular audits of SSH key configurations to identify any non-compliant keys and take corrective actions.

In conclusion, the SSH connectivity issue was caused by the use of Putty format SSH keys instead of OpenSSH format keys. The incident was resolved by generating new keys in the correct format and replacing the existing keys. Preventative measures include documentation updates, automated checks, regular audits, and user education to mitigate similar issues in the future.
AM: It was discovered that the issue was not related to the server configuration or SSH key expiration. Further investigation revealed that the SSH keys were in the Putty format instead of the required OpenSSH format.

- 30th Aug,2023 11:40 AM: The investigations were redirected to find a solution for converting the Putty format SSH keys to the OpenSSH format.
- 30th Aug,2023 9:40 PM: The incident was resolved by generating new SSH keys in the correct OpenSSH format and replacing the existing Putty format keys.

## Root Cause and Resolution:

The root cause of the issue was the use of Putty format SSH keys, which were incompatible with the SSH authentication process. The resolution involved generating new SSH keys using the key generation tool (key-gen) in the desired OpenSSH format. The new keys were then deployed, replacing the existing Putty format keys. This allowed users to establish SSH connections successfully.

## Corrective and Preventative Measures:

To prevent similar issues in the future, the following measures can be taken:

1. Provide proper documentation and guidelines to users regarding SSH key formats and their compatibility with various systems.
2. Implement automated checks and validation mechanisms to verify the
3. Implement SSH key validation checks during the generation process to ensure the correct format.
4. Set up monitoring and alerting systems to detect any issues related to SSH key authentication.
5. Review incident escalation and resolution processes and ensure that appropriate teams and individuals are involved and aware of the procedures.
