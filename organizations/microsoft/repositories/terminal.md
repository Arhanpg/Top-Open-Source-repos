# Windows Terminal, Console and Command-Line

- **Company:** Microsoft
- **GitHub organization:** [microsoft](https://github.com/microsoft)
- **Repository:** [microsoft/terminal](https://github.com/microsoft/terminal)
- **Default branch:** main
- **README:** [Open upstream README](https://github.com/microsoft/terminal/blob/main/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `2bd2aa24a9210265cbdb34c8fbdfb110b521277f`

## Project overview

This repository contains source code for Windows Terminal, Windows Terminal Preview, the Windows console host (conhost.exe), shared components, ColorTool and sample projects that demonstrate how to consume Windows Console APIs.

## Features and capabilities

- Maintains the Windows Terminal stable product and Preview distribution.
- Contains the Windows console host and components shared by terminal and console projects.
- Includes ColorTool and sample projects for using Windows Console APIs.
- Documents installation through Microsoft Store, GitHub releases and WinGet, with unofficial Chocolatey and Scoop options.
- Provides a Canary build channel for trying the latest main-branch code.
- Includes developer guidance, build prerequisites, debugging and contribution documentation.

## Technology stack

The README confirms a Windows desktop/console codebase, MSIX packaging, PowerShell and WinGet installation workflows, and Visual Studio-oriented build guidance. It does not enumerate the full language/framework implementation stack in the overview.

## Getting started

The README states Windows 10 version 2004 (build 19041) or later is required. Microsoft Store installation is preferred because it receives automatic updates. Manual GitHub installation uses an MSIX bundle; WinGet installs the Microsoft.WindowsTerminal package.

## Lifecycle, licensing and operational notes

Manual installations do not automatically update. Canary is the least stable channel; its App Installer distribution is limited to Windows 11, while the portable ZIP supports Windows 10 (19041+) and Windows 11. Chocolatey and Scoop are explicitly marked unofficial.

## Evaluation guidance

Before adopting the project, inspect the exact release and its build/dependency manifests, supported operating systems, licence, security guidance and maintenance policy. This page summarizes the upstream README and is not a source-code, dependency vulnerability, security or performance audit.

## Upstream references

- [Repository](https://github.com/microsoft/terminal)
- [README](https://github.com/microsoft/terminal/blob/main/README.md)
- [Issues](https://github.com/microsoft/terminal/issues)
- [Releases](https://github.com/microsoft/terminal/releases)

*Evidence note: the README blob SHA above identifies the upstream README revision used for this summary. The project overview and feature descriptions are based on that README; implementation details not established by it are left unspecified.*
