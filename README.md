# Portfolio Pollution
Challenge description: `My favorite hero has an awesome portfolio page. It even lets you immediately contact him in case of emergencies.`
<details>
    <summary>Contains vulnerability/exploit spoilers</summary>
    This challenge revolves around chaining together prototype pollution and cross-site scripting in order to steal a cookie (the flag). There is also some specific encoding required to bypass an attempt at filtering out malicious payloads.
    There are two up-to-date yet still vulnerable npm packages used by the app that make all of this possible (specifically <pre>merge-objects</pre> and <pre>xss</pre>).
    <br>
    All of the required vulnerabilites are publicly documented whether thats in an npm warning, a GitHub issue, or a list of known exploits.
    The intended solution is for players to identify these vulnerable packages, research their specifics, and then use this information to piece together a payload that allows them to steal the cookie.
</details>

## For testers
The `portfolio-pollution.tar.gz` file contains everything needed to run the challenge and test it locally.
This is also the file that will be handed out to CTF participants so that they can analyze how the app works and develop their exploit.
<br>
Specific vulnerability details and a solver script are available in the `solution` directory.
Please feel free to reach out to me with any questions, issues, or concerns (`eddie` in the OSIRIS Discord or `eddie@osiris.cyber.nyu.edu`).
I'd also love to hear about any unintended solutions or functionality you might come across!

## Potential issues
<details>
    <summary>Contains vulnerability/exploit spoilers</summary>
    The prototype pollution vulnerability requires the global object prototype itself to be polluted (e.g., `{}.__proto`).
    This means that if one participant were to pollute the object, it would affect all other players using the same server.
    <br>
    Currently, this is solved by clearing the prototype pollution as soon as the vulnerable code snippet runs so that other players are not affected.
    This seems to work fine for now as a more robust solution would require separate instances for each player.
</details>
