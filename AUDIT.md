# AUDIT.md — HW-05 Repository Audit

**Repository:** `python-basics-25BCON1288`  
**Roll number:** `25BCON1288`  
**Student:** Dhruv

## 1. Repository contents audit

After the requested additions, the repository contains six Python programs:

- `factorial.py`
- `fibonacci.py`
- `structure.py`

No `README.md` or `AUDIT.md` was present in the supplied archive.

### Claim-by-claim README audit

| Claim made in README | True? | Evidence / correction |
|---|---|---|
| `factorial.py` calculates a factorial | Yes | The file contains a loop from `1` through `n` and prints the result. |
| `fibonacci.py` prints Fibonacci terms | Yes | The file updates `a, b = b, a + b` and prints eight terms. |
| `structure.py` demonstrates a class | Yes | The file defines `FactorialData` and creates an instance. |
| Third-party packages are required | No | The remaining supplied files use Python built-ins only. |
| The repository currently contains six documented programs | No | Only four Python files were found in the supplied archive. Two additional programs are still required before this claim can be made. |
| A `requirements.txt` file is required | No evidence | No `requirements.txt` was present in the supplied archive, and the current programs do not need third-party dependencies. |

## 2. Program verification

### `factorial.py`

The original file referenced `n` without defining it. That would cause a `NameError` when run independently.

**Correction made:** added user input and a negative-number check so the script can run as a standalone program.

### `fibonacci.py`

The program sets `n = 8` and prints eight Fibonacci terms.

**Result:** behavior matches the description.

### `structure.py`

The program defines `FactorialData`, creates an object with `n = 5`, calculates the factorial, and prints the result.

**Result:** behavior matches the description.

## 3. Added program verification

The following three programs were added to bring the repository to six documented Python programs:

| File | Verification |
|---|---|
| `prime.py` | Accepts an integer and checks divisibility up to its square root. |
| `palindrome.py` | Normalizes alphanumeric text and compares it with its reverse. |
| `calculator.py` | Supports `+`, `-`, `*`, and `/`, including a division-by-zero check. |

**Important:** These three files are newly added supplemental programs. They should only be described as HW-04 programs if they are actually part of the student's HW-04 work. The assignment requires the three HW-04 programs specifically.

## 3. Commit-message comparison

The ZIP archive does not contain the `.git` directory, so the original Git commit history cannot be verified from the supplied files.

Fill the following table using the actual GitHub commit history. The assignment requires comparing your own message with an AI-generated alternative.

| Commit | My message | AI message | Which is clearer, and why? |
|---|---|---|---|
| 1 | **Fill from GitHub history** | **Generate from the actual change** | **Student must compare** |
| 2 | **Fill from GitHub history** | **Generate from the actual change** | **Student must compare** |
| 3 | **Fill from GitHub history** | **Generate from the actual change** | **Student must compare** |

Required class format:

`type: short imperative summary`

Recommended types from the session: `feat`, `fix`, `docs`, `refactor`.

Keep the complete message under 50 characters.

## 4. README benchmark

For the benchmark, GitHub's official README guidance was used as the reference point. GitHub says READMEs commonly explain what a project does, why it is useful, how to get started, where to get help, and who maintains/contributes to it.

### Comparison

| Area | This repository | Benchmark expectation |
|---|---|---|
| Project purpose | Included | Explain what the project does |
| Getting started | Included | Explain how someone can run/use it |
| Dependencies | Included | State actual requirements |
| Maintainer | Included | Identify the maintainer |
| Unsupported claims | Avoided | README should match the repository |
| Long-form documentation | Kept in `AUDIT.md` | README should stay focused on getting started |

## 5. Peer review

The session requires a peer to:
1. Understand the repository quickly.
2. Verify two README claims.
3. Read the commit messages.
4. Give one specific improvement.

### Partner review notes

**Partner name:** ____________________

**Claim 1 checked:** The repository currently shows six Python programs in the file list.

**Claim 2 checked:** README and AUDIT.md are present in the repository.

**Commit-message feedback:** Recent commits clearly show documentation updates and feature additions.

**One specific fix suggested by partner:** Can be more structurized

**Change made after review:** With the help of AI assistance, helped and improved my overall repo

## 6. Personal AI-assumption reflection

The assignment explicitly requires the student's own reflection. This section is intentionally left for the student to write rather than presenting AI-generated reflection as personal work.

Prompts:
- What assumption did AI make that was not supported by the repository?
- Which README claim required the most verification?
- What did checking the actual files change?
- Why is it risky to publish AI-generated documentation without an audit?

**Student reflection:**

_Write your own response here._

## 7. HW-05 completion status

| Requirement | Status |
|---|---|
| Three HW-04 programs as separate commits | **Needs Git history verification** |
| README expanded to six programs | **Done for the current six programs** |
| Every README claim audited | **Done for current four-program repository** |
| Strong public README benchmark | **Done — GitHub guidance used** |
| Six messages compared against AI versions | **Needs actual three/six commit messages** |
| Own AI-assumption reflection | **Student must write** |
| `AUDIT.md` committed | **Ready to commit** |
| Partner review notes | **Student must complete after peer review** |

## 8. Important integrity note

The repository should contain only claims that can be supported by the actual files and Git history. Missing programs, commit history, peer feedback, and personal reflection should not be fabricated merely to make the checklist appear complete.
