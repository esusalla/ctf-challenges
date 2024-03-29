# Portfolio Pollution
This challenge was built and used for NYU's CSAW CTF Qualification Round 2021.

Challenge description: `My favorite hero has an awesome portfolio page. It even lets you immediately contact him in case of emergencies.`
<details>
    <summary>Contains vulnerability/exploit spoilers</summary>
    This challenge revolves around chaining together prototype pollution and cross-site scripting in order to steal a cookie (the flag). There is also some specific encoding required to bypass a blacklist filter.
    There are two up-to-date yet still vulnerable npm packages used by the app that make all of this possible (specifically <code>merge-objects</code> and <code>xss</code>).
    <br><br>
    All of the required vulnerabilites are publicly documented whether that's in an npm warning, a list of known exploits, or a GitHub issue.
    The intended solution is for players to identify these vulnerable packages, research their specifics, and then use this information to piece together a payload that allows them to bypass the filters and steal the cookie.
</details>

## For testers
The `portfolio-pollution.tar.gz` file contains everything needed to run the challenge and test it locally.
This is also the file that will be handed out to CTF participants so that they can analyze how the app works and develop their exploit.

Specific vulnerability details and a solver script are available in the `solution` directory.
Please feel free to reach out to me with any questions, issues, or concerns.
I'd also love to hear about any unintended solutions or functionality you might come across!

<details>
    <summary>Contains vulnerability/exploit spoilers</summary>
    Please note that due to the persistent nature of the global object prototype (as noted in the potential issues section below), attempting to pollute the same property more than once will cause an array length error in the Docker container.
    <br><br>
    This can be circumvented locally by either adding the same reset mechanism used in the <code>challenge/index.js</code> file, restarting the container, or wrapping the merge function in a try-catch block as you work on the next stage of the exploit.
</details>

## Potential issues
<details>
    <summary>Contains vulnerability/exploit spoilers</summary>
    The prototype pollution vulnerability requires the global object prototype itself to be polluted (i.e., <code>{}.__proto__</code>).
    This means that if one participant were to pollute the object, it would affect all other players using the same server.
    <br><br>
    Currently, this is solved by clearing the prototype pollution as soon as the vulnerable code snippet runs so that other players are not affected.
    This functionality does not exist in the packaged source code that is distributed to players as it would too clearly indicate the solution.
    <br><br>
    For now this seems to work, but it's something I'll keep an eye on. A more robust solution would require separate instances for each player which should be avoided if possible.
</details>
