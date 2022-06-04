# Editorconfig Notes

## Format

EditorConfig files are in an INI-like file format. In an EditorConfig file, all beginning whitespace on each line is considered irrelevant. Each line must be one of the following:



- Blank: contains only whitespace characters.
- Comment: starts with a ; or a #.
	- Inserting an unescaped # or ; after non-whitespace characters in a line (i.e. inline) is not parsed as a comment, nor as part of the section name, the key pair (see below), or the value it was inserted into. This behavior may change in the future; therefore this kind of insertion is not recommended.
- Section Header: starts with a [ and ends with a ].
	- May not use any non-whitespace characters outside of the surrounding brackets.
	- May contain any characters between the square brackets (e.g., [ and ] and even spaces and tabs are allowed).
	- Forward slashes (/) are used as path separators.
	- Backslashes (\\) are not allowed as path separators (even on Windows).
- Key-Value Pair (or Pair): contains a key and a value, separated by an =.
	- Key: the part before the first = (trimmed of whitespace).
	- Value: The part after the first = (trimmed of whitespace).

Any line that is not one of the above is invalid.

EditorConfig files should be UTF-8 encoded, with LF or CRLF line separators.

Additionally, EditorConfig defines the following terms:

- Preamble: the lines that precedes the first section. The preamble is optional and may contain key-value pairs, comments and blank lines.
- Section Name: the string between the beginning [ and the ending ].
- Section: the lines starting from a Section Header until the beginning of the next Section Header or the end of the file.


## Globs

Section names in EditorConfig files are filepath globs, similar to the format accepted by .gitignore. They support pattern matching through Unix shell-style wildcards. These filepath globs recognize the following as special characters for wildcard matching:

<table border="1" class="docutils">
<colgroup>
<col width="50%">
<col width="50%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Special Characters</th>
<th class="head">Matching</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">*</span></code></td>
<td>any string of characters, except path separators (<code class="docutils literal notranslate"><span class="pre">/</span></code>)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">**</span></code></td>
<td>any string of characters</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">?</span></code></td>
<td>any single character, except path separators (<code class="docutils literal notranslate"><span class="pre">/</span></code>)</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">[seq]</span></code></td>
<td>any single character in seq</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">[!seq]</span></code></td>
<td>any single character not in seq</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">{s1,s2,s3}</span></code></td>
<td>any of the strings given (separated by commas, can be nested)</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">{num1..num2}</span></code></td>
<td>any integer numbers between <code class="docutils literal notranslate"><span class="pre">num1</span></code> and <code class="docutils literal notranslate"><span class="pre">num2</span></code>, where <code class="docutils literal notranslate"><span class="pre">num1</span></code> and <code class="docutils literal notranslate"><span class="pre">num2</span></code>
can be either positive or negative</td>
</tr>
</tbody>
</table>

The backslash character (\\) can be used to escape a character so it is not interpreted as a special character.

Cores must accept section names with length up to and including 1024 characters. Beyond that, each implementation may choose to define its own upper limit or no explicit upper limit at all.


## File Processing

When a filename is given to EditorConfig a search is performed in the directory of the given file and all parent directories for an EditorConfig file (named “.editorconfig” by default). Non-existing directories are treated as if they exist and are empty. All found EditorConfig files are searched for sections with section names matching the given filename. The search shall stop if an EditorConfig file is found with the root key set to true in the preamble or when reaching the root filesystem directory.

Files are read top to bottom and the most recent rules found take precedence. If multiple EditorConfig files have matching sections, the rules from the closer EditorConfig file are read last, so pairs in closer files take precedence.

## Supported Pairs

EditorConfig file sections contain key-value pairs separated by an equal sign (=). With the exception of the root key, all pairs MUST be located under a section to take effect. EditorConfig plugins shall ignore unrecognized keys and invalid/unsupported values for those keys.

<table border="1" class="docutils">
<colgroup>
<col width="50%">
<col width="50%">
</colgroup>
<thead valign="bottom">
<tr class="row-odd"><th class="head">Key</th>
<th class="head">Supported values</th>
</tr>
</thead>
<tbody valign="top">
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">indent_style</span></code></td>
<td>Set to <code class="docutils literal notranslate"><span class="pre">tab</span></code> or <code class="docutils literal notranslate"><span class="pre">space</span></code> to use hard tabs or soft tabs respectively. The
values are case insensitive.</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">indent_size</span></code></td>
<td>Set to a whole number defining the number of columns used for each
indentation level and the width of soft tabs (when supported). If this
equals <code class="docutils literal notranslate"><span class="pre">tab</span></code>, the <code class="docutils literal notranslate"><span class="pre">indent_size</span></code> shall be set to the tab size, which
should be <code class="docutils literal notranslate"><span class="pre">tab_width</span></code> (if specified); else, the tab size set by the
editor. The values are case insensitive.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">tab_width</span></code></td>
<td>Set to a whole number defining the number of columns used to represent
a tab character. This defaults to the value of <code class="docutils literal notranslate"><span class="pre">indent_size</span></code> and should
not usually need to be specified.</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">end_of_line</span></code></td>
<td>Set to <code class="docutils literal notranslate"><span class="pre">lf</span></code>, <code class="docutils literal notranslate"><span class="pre">cr</span></code>, or <code class="docutils literal notranslate"><span class="pre">crlf</span></code> to control how line breaks are
represented. The values are case insensitive.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">charset</span></code></td>
<td>Set to <code class="docutils literal notranslate"><span class="pre">latin1</span></code>, <code class="docutils literal notranslate"><span class="pre">utf-8</span></code>, <code class="docutils literal notranslate"><span class="pre">utf-8-bom</span></code>, <code class="docutils literal notranslate"><span class="pre">utf-16be</span></code> or <code class="docutils literal notranslate"><span class="pre">utf-16le</span></code> to
control the character set. Use of <code class="docutils literal notranslate"><span class="pre">utf-8-bom</span></code> is discouraged.</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">trim_trailing_whitespace</span></code></td>
<td>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to remove all whitespace characters preceding newline
characters in the file and <code class="docutils literal notranslate"><span class="pre">false</span></code> to ensure it doesn’t.</td>
</tr>
<tr class="row-even"><td><code class="docutils literal notranslate"><span class="pre">insert_final_newline</span></code></td>
<td>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> ensure file ends with a newline when saving and <code class="docutils literal notranslate"><span class="pre">false</span></code>
to ensure it doesn’t.</td>
</tr>
<tr class="row-odd"><td><code class="docutils literal notranslate"><span class="pre">root</span></code></td>
<td>Must be specified in the preamble. Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to stop the
<code class="docutils literal notranslate"><span class="pre">.editorconfig</span></code> file search on the current file. The value is case
insensitive.</td>
</tr>
</tbody>
</table>

For any pair, a value of unset removes the effect of that pair, even if it has been set before. For example, add indent_size = unset to undefine the indent_size pair (and use editor defaults).

Pair keys are case insensitive. All keys are lowercased after parsing.

Cores must accept keys and values with lengths up to and including 1024 and 4096 characters respectively. Beyond that, each implementation may choose to define its own upper limits or no explicit upper limits at all.
