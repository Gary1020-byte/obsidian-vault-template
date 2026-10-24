# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2026-10-24

The first tagged release. The template has been in use since 2026-10-02; this
release marks the point where it is internally consistent and mechanically
checked.

### Added

- `check_template.py` — a consistency checker that verifies every folder the
  docs name exists, every QuickAdd macro points at a real folder and template,
  the plugin list matches the committed plugin configs, the markdown tables are
  well-formed, every file ends with a newline, and no string from the author's
  private system survived into the tree.
- CI, Dependabot, `CONTRIBUTING.md`, and issue templates. CI runs the checker on
  every push and pull request.
- `.obsidian/plugins/calendar/data.json` — the Calendar plugin was listed in
  `community-plugins.json` but had no committed config, so all five advertised
  plugins are now actually configured.

### Fixed

- The shipped mode was called `Productivity`, which is the name of the author's
  own notes, and the docs promised "three modes" while listing one. The mode is
  now `Productivity`, and the `Knowledge` mode the docs already referred to is
  spelled out.
- One table row in `AGENTS.md` was missing its leading pipe and rendered broken.
- Seven files had no trailing newline.
- `log.md`'s init entry claimed four plugin configs and a `raw/emails/` +
  `raw/drafts/` layout that the tree does not have.
