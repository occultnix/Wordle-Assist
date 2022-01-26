# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Highest Concerns
- Wordle Assist does not semantically separate single-item lists from multi-item lists.
- Wordle Assist only processes words from a hard-coded array.
- Wordle Assist output is difficult to read.
- Wordle Assist only checks for single letters, not composite sounds or letter combinations.

### Future Concerns
- Wordle Assist runs from the command line with no user interface, hurting user experience.
- Wordle Assist does not provide user with word options based on most likely letters.
- Wordle Assist does not filter intaken words based on unavailable letters.


## [0.03.0] - 2022-01-25
### Added
- Multi-line comments to define function purposes at a glance and to be used as section breaks.

### Changed
- Wordle Assist now begins output by listing ONLY the letters that appeared!
- Wordle Assist now lists all letters that DON'T appear on a single line!
- Wordle Assist now lists any non-letter characters IF they appear! Also on a single line!

### Removed
- "Current Limitations / Issues" section in README.md.

## [0.02.0] - 2022-01-24
### Added
- Changelog! With semantic versioning info!! Hurrah! 🥳
- Added functionality to capture and view characters that aren't letters.

### Changed
- Converted individual letter frequency variables to dictionary to be able to iterate through them.
- Improved massive if/elif chain to two options with full effectiveness.
- Moved print() statements to another function for improved modular state.

### Depreciated
- "Current Limitations / Issues" section in README.md.

## [0.01.0] - 2022-01-23
### Added
- Initial release.
- 'main.py' processes a hard-coded array of words and outputs letter frequency.
