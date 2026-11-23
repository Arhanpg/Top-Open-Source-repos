# dotnet/android-libzipsharp

- Company: Microsoft
- GitHub account: [https://github.com/dotnet](https://github.com/dotnet)
- Mapping status: official-project-linked
- Repository: [dotnet/android-libzipsharp](https://github.com/dotnet/android-libzipsharp)
- Default branch: main
- README: [Open upstream README](https://github.com/dotnet/android-libzipsharp/blob/main/README.md)
- README blob SHA: b7ca34aa36267615c14303084f11c290893ae43d
- Repository ID: 61309402
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A managed wrapper (and then some) around libzip (https://libzip.org/)

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Captured: 2026-11-23T20:22:14+00:00

### Short excerpt (up to 100 words)

> A managed wrapper (and then some) around libzip (https://libzip.org/) The core of `LibZipSharp` is the `ZipArchive` class. You can use this class to create/extract/update zip file. To create a new archive use the `FileMode.CreateNew`, this will behave exactly as it does with normal `File` operations. An exception will be thrown if the file already exists. using (var zip = ZipArchive.Open ("test.zip", FileMode.CreateNew)) { } To open an existing zip file use `FileMode.Open`. using (var zip = ZipArchive.Open ("test.zip", FileMode.Open)) { } There are a number of methods which can be used to add items to the zip file. The simplest

### README headings

- LibZipSharp
- Create a new Zip
- Open am existing Zip
- Add files to Zip
- Shipping the native libraries.

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| C# | 260,845 |
| CMake | 18,232 |
| Shell | 9,998 |
| Batchfile | 5,237 |
| C++ | 2,563 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- CMakeLists.txt (capture: captured)
- libZipSharp.sln (capture: captured)
- LibZipSharp.UnitTest/LibZipSharp.UnitTest.csproj (capture: captured)
- LibZipSharp/libZipSharp.csproj (capture: captured)
- ZipBenchmark/ZipBenchmark.csproj (capture: captured)
- ZipTest/ZipTest.csproj (capture: captured)

- Manifest scan truncated by GitHub: False
- Manifest capture state: captured

## Lifecycle metadata

- Archived: False
- Fork: False
- Disabled: False
- Licence SPDX: MIT
- Stars at capture: 30
- Forks at capture: 24
- Last updated: 2026-10-03T23:36:48Z
- Last pushed: 2026-10-03T23:36:46Z
- Topics: dotnet, libzip, mono, native-libraries

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/dotnet/android-libzipsharp)
- [README](https://github.com/dotnet/android-libzipsharp/blob/main/README.md)
- [Issues](https://github.com/dotnet/android-libzipsharp/issues)
- [Releases](https://github.com/dotnet/android-libzipsharp/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
