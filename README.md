# Real-Life Patch Notes: The Comedy Changelog

A make.fun bounty entry. One line, at most 160 characters: a software
patch note for a bug in real life or human biology, in the terse register
of a real release note.

The entry:

> v4.0.1: fixed a bug where crossing a doorway flushed working memory without saving.

`main.py` (Python, standard library only) writes that line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`. It creates the output directory if
missing, never removes it, and makes no network calls.
