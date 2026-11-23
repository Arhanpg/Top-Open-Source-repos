# LevelDB

- **Company grouping:** Alphabet / Google
- **GitHub organization:** [google](https://github.com/google)
- **Repository:** [google/leveldb](https://github.com/google/leveldb)
- **Default branch:** master/main (verify from repository metadata)
- **README:** [Open upstream README](https://github.com/google/leveldb/blob/master/README.md)
- **Review status:** README inspected and summarized
- **README blob SHA:** `a5e541604df2e547a76b449e8adf99ada50b23c8`

## Project overview

LevelDB is an embeddable key-value storage library written at Google. It provides an ordered mapping from string keys to string values and is intended as a storage component, not a full client-server relational database.

## Features and capabilities

- Stores arbitrary byte-array keys and values in sorted-key order.
- Supports custom comparison functions to define key ordering.
- Provides Put, Get and Delete operations and atomic write batches.
- Supports transient snapshots and forward/backward iteration.
- Compresses data with Snappy and also supports Zstandard compression.
- Abstracts external filesystem activity through a virtual interface.

## Technology stack

C++ storage library; CMake build system; Snappy compression and optional Zstandard compression. README build instructions cover POSIX and Windows. The project exposes a library API and no built-in network service.

## Getting started

Clone with recursive submodules, create a build directory, configure with CMake in Release mode and build. The repository's doc/index.md contains library API and design documentation.

## Lifecycle and operational considerations

The README states maintenance is very limited and only critical bug fixes or changes needed by internally supported clients are expected to be reviewed. It explicitly says LevelDB is not SQL, has no relational data model or built-in indexes, permits only one process per database at a time, and has no built-in client-server support.

## Evaluation guidance

Check the exact release, manifests, supported platforms, licence and maintenance policy before adopting the project. This dossier is based on the upstream README, not a full source-code, vulnerability or performance audit.

## Upstream references

- [Repository](https://github.com/google/leveldb)
- [README](https://github.com/google/leveldb/blob/master/README.md)
- [Issues](https://github.com/google/leveldb/issues)
- [Releases](https://github.com/google/leveldb/releases)

*Evidence note: README blob SHA identifies the upstream version inspected. Technology claims are limited to the README's evidence; implementation details not established by that source are not inferred.*
