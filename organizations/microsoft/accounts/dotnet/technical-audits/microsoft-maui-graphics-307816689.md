# dotnet/Microsoft.Maui.Graphics

- Company: Microsoft
- Account: dotnet
- Repository: https://github.com/dotnet/Microsoft.Maui.Graphics
- Default branch: main
- Audit status: evidence_only
- Confidence: medium
- Generated: 2026-11-28T07:05:03+00:00

## Project purpose

Microsoft.Maui.Graphics is an experimental cross-platform graphics library for iOS, Android, Windows, macOS, Tizen and Linux written completely in C#. A Microsoft supported portion of this library has been merged with dotnet/maui and is maintained separately. This project remains separate for developers to experiment further on additional scenarios such as WASM, WinForms, WPF, Xamarin, and Linux.

## Why this project is used

An experimental cross-platform native graphics library.

## Core features

No separately supported feature list extracted.

## Technology stack

- Languages: C#, PowerShell, TypeScript, JavaScript, Shell, Batchfile, CSS, HTML
- Frameworks/libraries: Unknown / not established
- Dependency names: @types/emscripten, ts-loader, typescript, webpack, webpack-cli
- Build/package tools: npm-compatible manifest
- Runtimes: Unknown / not established
- Databases/storage: Unknown / not established
- Infrastructure: Unknown / not established
- Platforms: Unknown / not established

## Architecture

Architecture is not interpreted in evidence-only mode. Sampled source files: src/external/SharpDX.Desktop/Collections/EqualityComparer.cs, src/external/SharpDX.Desktop/Diagnostics/VSGraphicsDebugger.cs, src/external/SharpDX.Desktop/Direct3D/PixHelper.cs, src/external/SharpDX.Desktop/MessageFilterHook.cs

## Setup and usage

No setup information established.

## Limitations and caveats

- Supported Platforms: Platform | Supported Abstractions |
- Supported Platforms: -----------------------|-------------------------------------------|
- Supported Platforms: Xamarin.iOS | CoreGraphics & SkiaSharp |
- Supported Platforms: Xamarin.Android | Android.Graphics & SkiaSharp |
- Supported Platforms: Xamarin.Mac | CoreGraphics & SkiaSharp |
- Supported Platforms: WPF | SharpDX, SkiaSharp, Xaml & GDI |
- Supported Platforms: UWP | SharpDX, Win2D, Xaml, SkiaSharp |
- Supported Platforms: WinForms | SharpDX, SkiaSharp & GDI |

## Evidence and provenance

- README: https://github.com/dotnet/Microsoft.Maui.Graphics/blob/main/README.md
- README SHA: 7f68e7dc7bb09f373841abd79752394b4e2f1750
- Manifests: src/Microsoft.Maui.Graphics.Blazor.JS/package.json
- Sampled source files: src/external/SharpDX.Desktop/Collections/EqualityComparer.cs, src/external/SharpDX.Desktop/Diagnostics/VSGraphicsDebugger.cs, src/external/SharpDX.Desktop/Direct3D/PixHelper.cs, src/external/SharpDX.Desktop/MessageFilterHook.cs
- Git tree state: captured
- Evidence fingerprint: 542f96441745d40845efe6a3a9261f05a2fce6574742ae0eab9087354565cf8d

## Unverified / unknown

- Semantic feature and architecture interpretation is pending.
- Framework, database, runtime and infrastructure require direct evidence.

> Evidence-only output; not a complete semantic, source-code, security or runtime audit. Configure model credentials for semantic interpretation.

---

Generated from upstream repository evidence; verify source links before relying on interpretations.
