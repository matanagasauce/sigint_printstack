# sigint_printstack
a tool for debuging, print stack info when received SIGINT.

# Usage
- Add `python import sigint_printstack` to the top of your code and it just works!
- If you have your own handler for `SIGINT` in your code, don't worry, the module redifines `signal.signal` to first print the stack, then invoke your own handler.
