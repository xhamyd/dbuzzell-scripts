# Bash string manipulation cheat sheet

| Assignment | |
| --- | --- |
| Assign `value` to `variable` if `variable` is not already set. Value will be returned. | `${variable="value"}` |
| Couple with `:` no-op if return value is to be discarded. | `: ${variable="value"}` |

| Removal | |
| --- | --- |
| Delete shortest match of `needle` from front of `haystack` | `${haystack#needle}` |
| Delete longest match of `needle` from front of `haystack` | `${haystack##needle}` |
| Delete shortest match of `needle` from back of `haystack` | `${haystack%needle}` |
| Delete longest match of `needle` from back of `haystack` | `${haystack%%needle}` |

| Replacement | |
| --- | --- |
| Replace first match of `needle` with `replacement` from `haystack` | `${haystack/needle/replacement}` |
| Replace all matches of `needle` with `replacement` from `haystack` | `${haystack//needle/replacement}` |
| If `needle` matches front of `haystack` replace with `replacement` | `${haystack/#needle/replacement}` |
| If `needle` matches back of `haystack` replace with `replacement` | `${haystack/%needle/replacement}` |


| Substitution | |
| --- | --- |
| If `variable` not set, return `value`, else `variable` | `${variable-value}` |
| If `variable` not set or empty, return `value`, else `variable` | `${variable:-value}` |
| If `variable` set, return `value`, else null string | `${variable+value}` |
| If `variable` set and not empty, return `value`, else null string | `${variable:+value}`|

| Extraction | |
| --- | --- |
| Extract `length` characters from `variable` starting at `position` | `${variable:position:length}` |
| String length of `variable` | `${#variable}` |

## Reference
- http://tldp.org/LDP/abs/html/string-manipulation.html.
- http://tldp.org/LDP/abs/html/parameter-substitution.html.
- http://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02.
