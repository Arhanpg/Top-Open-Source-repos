# Microsoft PowerToys

<sub>Company: Microsoft · Repository: [microsoft/PowerToys](https://github.com/microsoft/PowerToys) · Default branch: `main` · Review status: **README reviewed**</sub>

## At a glance

PowerToys is a collection of Windows utilities designed to help users customize Windows and streamline everyday tasks. Instead of being a single-purpose application, it groups small tools that improve window management, file workflows, keyboard use, desktop navigation and other power-user activities.

**Problem it addresses:** advanced Windows users often need quick system-level helpers that are not available as one integrated set of utilities. PowerToys collects these tools in one installable suite and provides a shared release and community contribution process.

## Utility coverage

The README states that PowerToys includes more than 30 utilities. Its utility table includes (among others):

| Utility | Function suggested by the utility's documented role |
|---|---|
| Advanced Paste | Additional paste workflows |
| Always on Top | Keep a selected window above others |
| Awake | Prevent the machine from sleeping during a task |
| Color Picker | Capture a color from the screen |
| Command Palette | Launch commands and actions |
| FancyZones | Arrange windows into custom layouts |
| File Explorer add-ons | Add preview or integration capabilities in Explorer |
| Image Resizer | Resize images from the Windows workflow |
| Keyboard Manager | Remap keyboard keys and shortcuts |
| PowerRename | Rename groups of files |
| Text Extractor | Extract text from screen content |
| Workspaces | Reopen a defined set of applications and windows |
| ZoomIt | Screen zoom and presentation-oriented utilities |

The names above are drawn from the README's utility list. For exact behaviour, limitations and shortcuts, open each utility's own documentation through the official PowerToys docs.

## Installation options

The README documents several supported installation paths:

- **GitHub Releases:** download the installer asset matching architecture and install scope.
- **Microsoft Store:** install and update through the Store.
- **WinGet:** install from the command line. The README provides separate user-scope and machine-scope commands.
- **Community tools:** Chocolatey and Scoop are linked as community-driven options.

Example WinGet commands from the README:

```powershell
winget install Microsoft.PowerToys -s winget
winget install --scope machine Microsoft.PowerToys -s winget
```

For system requirements and detailed installation guidance, use the [official installation documentation](https://learn.microsoft.com/windows/powertoys/install).

## Technology and delivery profile

| Area | README-supported details |
|---|---|
| Target platform | Windows |
| Product form | Collection of desktop utilities |
| Delivery channels | GitHub Releases, Microsoft Store and WinGet |
| Documentation | Microsoft Learn / PowerToys docs |
| Development model | Community contributions, issue reporting and design/documentation work |

The README's overview does not provide a complete language/framework breakdown. The repository's source projects and build files must be inspected before adding a precise implementation stack to this catalogue.

## Community and development model

The maintainers explicitly welcome contributions beyond code, including feature specifications, design, documentation and bug reports. They ask contributors to read the Contributor's Guide before starting work on a proposed feature so that maintainers can advise on scope and avoid duplicate effort.

The README also points users to release notes and a roadmap. Because individual utilities evolve independently, consult those sources to confirm whether a particular feature is currently shipped, experimental or planned.

## Where it is useful

- Improving productivity on Windows workstations.
- Managing complex multi-window layouts.
- Standardizing common file and keyboard operations.
- Adding small utilities to developer, design and IT support workflows.
- Discovering examples of how Windows desktop utilities can be packaged and maintained as an open-source suite.

## Upstream references

- [Repository](https://github.com/microsoft/PowerToys)
- [Primary README](https://github.com/microsoft/PowerToys/blob/main/README.md)
- [Official documentation](https://aka.ms/powertoys-docs)
- [Installation guide](https://learn.microsoft.com/windows/powertoys/install)
- [Release notes](https://github.com/microsoft/PowerToys/releases)
- [Contributor's Guide](https://github.com/microsoft/PowerToys/blob/main/CONTRIBUTING.md)

**Evidence note:** README blob inspected: `ae0ed8458fac186d8543f1397646907720af2434`.
