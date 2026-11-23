"""Real-Life Patch Notes: The Comedy Changelog (make.fun).

The line (pass 2, final, 83 characters):

    v4.0.1: fixed a bug where crossing a doorway flushed working memory
    without saving.

REVISION (pass 2): re-read pass 1 against the hiccup runner-up and
tightened the verb. "Cleared the working memory buffer" is accurate
but wordy; "flushed working memory" is the precise engineering verb
for a buffer (a buffer flush) and says the same thing in two fewer
words, dropping "the" and "buffer" as well. The sentence gets
tighter and more release-note-like -- real changelogs say "flushed
the cache", not "cleared the cache buffer" -- while the joke (walk
through a door, lose the thought, no save) is unchanged and the
punch still lands on "without saving". 94 -> 83 characters, still
well inside the 160 gate, no padding left.

Candidate lines weighed (all one line, <=160 chars, release-note register):

1. DOORWAY AMNESIA (chosen) -- "v4.0.1: fixed a bug where crossing a
   doorway cleared the working memory buffer without saving."
   The doorway effect is a real, documented quirk of human memory:
   everyone has walked into a room and forgotten why. Mapping it onto
   a working-memory buffer flushed without saving is a genuine
   engineering metaphor, not a joke wearing a patch-note costume. The
   wince is immediate and universal, the register is exactly a real
   changelog entry (version + "fixed a bug where"), and there is no
   padding: every word works.

2. HICCUP RETRY LOOP (runner-up) -- "v1.9.3: fixed a bug where the
   diaphragm entered a retry loop with no backoff and no cancel button."
   "No backoff" is a lovely engineering detail and hiccups are
   recognisable, but the wince is smaller and more situational than
   doorway amnesia, and the line leans on two punch phrases where one
   would do. Loses to (1) on universality and tightness.

3. CONTAGIOUS YAWN -- "v2.7.1: fixed a bug where seeing another user
   yawn triggered an identical yawn without consent."
   "Without consent" is a funny dry touch and the bug is universal,
   but the joke is slightly thinner: the bug itself feels less like a
   system fault and more like a social quirk. Loses to (1) on the
   strength of the comedic idea.

4. EARWORM LOOP -- "v3.3.0: fixed a bug where a 12-second chorus
   looped in the background process with no kill switch."
   Very recognisable and "no kill switch" is a good dry punch, but
   "12-second chorus" is invented-specific rather than felt, and the
   bug reads a touch more like an annoyance than a system fault.
   Loses to (1) on specificity that is real rather than invented.

5. PHOTIC SNEEZE -- "v3.1.0: fixed a bug where stepping into sunlight
   triggered an unscheduled sneeze with no opt-out."
   Specific and real, but the sneeze reflex is a smaller, quirkier
   wince than forgetting why you entered a room, and "no opt-out"
   does less work than the buffer-flush image in (1).

The brief's own example line (left-ear audio 40ms late) is deliberately
NOT used: it is the house's example text and may match a fixed text.

Gate: /output/entry.txt must be UTF-8 text of 1 to 160 characters,
not only white space. This program asserts that before writing.
"""

import os

LINE = (
    "v4.0.1: fixed a bug where crossing a doorway flushed working "
    "memory without saving."
)


def main() -> None:
    assert 1 <= len(LINE) <= 160, "line must be 1-160 characters"
    assert LINE.strip(), "line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
