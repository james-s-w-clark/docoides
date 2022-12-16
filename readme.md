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

# Extra ideas / notes
- Ideally, whole files should be resembled in docs
  - It might be a bit ugly
  - All the context is there - imports, EOF, everything
  - Might fragment test code too much
  - Referencing a file with multiple tests in would be too large
    - Could link to specific line numbers
    - Could link to a keyword (e.g. a test name)
    - Both are brittle, but it'd be a nice option to have.