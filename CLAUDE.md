# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project status

This repository is at its inception. `LICENSE` is **CC BY-NC-SA 4.0** (non-commercial; changed from an initial Apache 2.0 placeholder once `data/` began aggregating third-party non-commercial-only psychometric content — see the LICENSE file's "Why non-commercial" note and `data/README.md`). There is no application source code, dependency manifest, build tooling, or tests yet — `data/` (psychometric item banks) and `tools/annotator/` (a local review webapp) exist, but no product/app scaffold.

The `.gitignore` is the standard GitHub Python template, which signals the intended language is **Python**. No package manager, framework, or project layout has been chosen yet — when scaffolding, establish these deliberately rather than assuming them.

`README.md` states the project's intent (in Korean): *"나를 더 잘 설명할 수 있을 때, 우리는 서로를 조금 더 이해할 수 있다"* — "When I can explain myself better, we can understand each other a little more." The name **deepinme** and this tagline suggest a self-expression / self-understanding theme; confirm the concrete product direction with the user before building.

## When adding the first code

Once real structure exists, update this file with the actual build/test/run commands and architecture. Until then, there are no project-specific commands to document beyond standard `git`.
