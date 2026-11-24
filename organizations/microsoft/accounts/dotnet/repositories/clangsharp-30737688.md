# dotnet/ClangSharp

- Company: Microsoft
- GitHub account: [https://github.com/dotnet](https://github.com/dotnet)
- Mapping status: official-project-linked
- Repository: [dotnet/ClangSharp](https://github.com/dotnet/ClangSharp)
- Default branch: main
- README: [Open upstream README](https://github.com/dotnet/ClangSharp/blob/main/README.md)
- README blob SHA: 898fdf5ca5e3114a20ee8b62d52e150b19a8f90f
- Repository ID: 30737688
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

Clang bindings for .NET written in C#

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-24T03:40:32+00:00

### Short excerpt (up to 100 words)

> ClangSharp provides Clang bindings written in C#. It is self-hosted and auto-generates itself by parsing the Clang C header files using ClangSharpPInvokeGenerator. A nuget package for the project is provided here: https://www.nuget.org/packages/clangsharp. A .NET tool for the P/Invoke generator project is provided here: https://www.nuget.org/packages/ClangSharpPInvokeGenerator **NOTE:** If you are running as a dotnet tool, you may need to manually copy the appropriate DLLs from NuGet due to limitations in the dotnet tool support. A convenience package which provides the native libClang library for several platforms is provided here: https://www.nuget.org/packages/libclang A helper package which exposes many Clang APIs missing from libClang is

### README headings

- ClangSharp
- Table of Contents
- Code of Conduct
- License
- Features
- Building Managed
- Building Native
- Windows
- Linux
- Regenerating native binaries
- lift the prebuilt libclang out of the matching LLVM release
- compile libClangSharp against that same LLVM release
- Generating Bindings
- Using as a Library
- Using locally built versions
- Spotlight

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 3,489,408 |
| C++ | 302,214 |
| C | 58,292 |
| PowerShell | 22,571 |
| Shell | 20,995 |
| CMake | 5,863 |
| Batchfile | 664 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- sources/CMakeLists.txt (capture: captured)
- sources/ClangSharp.Interop/ClangSharp.Interop.csproj (capture: captured)
- sources/ClangSharp.PInvokeGenerator/ClangSharp.PInvokeGenerator.csproj (capture: captured)
- sources/ClangSharp/ClangSharp.csproj (capture: captured)
- sources/ClangSharpPInvokeGenerator/ClangSharpPInvokeGenerator.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 1269
- Forks at capture: 192
- Last updated: 2026-11-19T19:28:51Z
- Last pushed: 2026-11-14T23:01:49Z
- Topics: hacktoberfest

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/dotnet/ClangSharp)
- [README](https://github.com/dotnet/ClangSharp/blob/main/README.md)
- [Issues](https://github.com/dotnet/ClangSharp/issues)
- [Releases](https://github.com/dotnet/ClangSharp/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
