# Docoides

> -oides, -odes: Pronunciation: /oiːdiːz/, /oʊːdiːz/. Origin: Ancient Greek: εἶδος (eîdos). Meaning: likeness. Used for species that resemble other species
 
_Docoides lets you documentation have snippets exactly resembling your source or test code_


When writing technical documentation, you often want to include examples of source or test code. Why write bespoke untested example, when you can do better?

Docoides is a POC documentation preprocessor to lift (extremely) atomic tests into your documentation.

# Goals

- As a user, I want a simple unique syntax in my markdown files that lifts code from tests into my documentation
  - Ideation:
    - Markdown links are usually like [description](link)
    - Sometimes we will want to replace our link with all of the code in a file. Maybe ```[description](link)``` works well?
      - 3x ` before & after implies a code block
      - What's in the code block?
        - Some code from a linked file
        - Some description... maybe that's more before the example (like in adoc)
      - By using the typical link syntax, IDEs can let users in .md files navigate to the target code instantly. This is *very* important!
- Just a little POC here - it should probably be in .js or .ts, but I can iterate faster in Python
- As a reader, I want code blocks to have correct highlighting
  - Code blocks for .scala files should have ```scala, .py -> python, .sh -> shell, etc. 
- ~~Docoides should link to the code they are sourced from~~
  - locally: relative file path in project
    - actually, the non-processed markdown text will link just fine
  - online: link to github
    - doesn't really add much value
- As a documenter, I want Docoides to fail and let me know if:
  - it can't find a file
  - it can't fine a chosen line range in that file
  - it can't find a test name in that file

# Extra ideas / notes
- Ideally, whole files should be resembled in docs
  - It might be a bit ugly - imports
  - All the context is there - imports, EOF, everything
  - Might fragment test code too much
  - Referencing a file with multiple tests in would be too large
    - Could link to specific line numbers
    - Could link to a keyword (e.g. a test name)
    - Both are brittle, but it'd be a nice option to have.
- By referencing an existing file, duplication is reduced - so with Docoides there's less chance of having working but technically inaccurate/outdated code in your documentation
- There are great tools that can test your Scala snippets, like scala-cli or mdoc
  - scala-cli can run your code snippets if you point it to the file
  - It would be interesting to explore the ergonomics of users navigating to actual src/test code in your repo from markdown documentation 
- Probably only works well when your code is in the same repo as your website... which I have seen quite a few times e.g. [growthbook](https://github.com/growthbook/growthbook/tree/main/docs), [smithy4s](https://github.com/disneystreaming/smithy4s/tree/main/modules/website)
- Linked code will usually be a different kind of "test" - authors may want to put runnable examples in a directory like `test/docs-examples`.
  - If your code snippets in documentation are runnable examples that are guaranteed to work, that's probably a great thing!