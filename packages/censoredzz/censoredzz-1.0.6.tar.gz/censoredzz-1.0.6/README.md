# Censoredzz

censor your profane words in Nepali-(Roman) text

## Installation

You can install the package using pip:

```bash
pip install censoredzz
```

## usage

```bash
from censoredzz import censor, profanity
```
To censor the word.
input: "text".
output: "censored text"
```bash
censor.censor_text("ta badword ho")
```
output:
"ta ****** ho"

To check the profane word.
input: "text".
output: "1/0"
```bash
profanity.has_profanity("ta badword ho")
```
output:
1
