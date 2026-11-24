# aws/audit-plugin-for-mysql

- **Company:** Amazon / AWS
- **Repository:** https://github.com/aws/audit-plugin-for-mysql
- **Default branch:** mysql-8.0
- **Audit status:** manual_reviewed
- **Evidence confidence:** high

## Project purpose

A loadable MySQL Server audit plugin that logs server activity. The README says Amazon RDS for MySQL uses it for security and compliance logging.

## Why this project is used

MySQL operators can enable server-activity auditing for security monitoring and compliance-related record keeping. AWS explicitly disclaims warranties and support for this community-published source.

## Core features

- **MySQL server activity auditing:** provides a server plugin for auditing MySQL server activity.
- **MySQL 8.0 plugin integration:** adapts the MariaDB Audit Plugin lineage to the MySQL 8.0 plugin API.
- **Loadable server plugin:** documents installing server_audit.so and enabling it through plugin_load_add or INSTALL PLUGIN.
- **Optional MTR tests:** mysql-test files are optional for users who want to run MTR tests.

Evidence: [README](https://github.com/aws/audit-plugin-for-mysql/blob/mysql-8.0/README.md).

## Technology stack

- **Languages:** C, C++
- **Integration API:** MySQL Server plugin API
- **Build tools:** CMake and MySQL build macros
- **Runtime:** MySQL 8.0 server plugin
- **Database:** MySQL Server
- **Use context:** README identifies Amazon RDS for MySQL as a user of the plugin.

## Architecture

The inspected CMake file registers server_audit.cc and file_logger.cc as a MODULE_ONLY MySQL plugin target. It must be built in the context of a MySQL source tree; it is not documented as a standalone service.

## Setup and usage

- Copy the plugin source into the MySQL source tree plugin directory before compiling.
- Install server_audit.so into the MySQL plugin directory.
- Enable it using plugin_load_add in my.cnf or INSTALL PLUGIN.
- Consult the linked upstream MariaDB plugin documentation for detailed audit variables and logging settings.

## Limitations and caveats

- AWS provides no warranty or support for this community project.
- The README says Amazon Linux has been tested, other operating systems have not been tested, and Windows is unsupported.
- The README says there are no plans for major new features and describes the intent as stable maintenance.
- GitHub license metadata is NOASSERTION; the inspected CMake file contains a GPL-2.0 SPDX header, so repository-wide licensing should be checked before redistribution.

## Evidence and provenance

- [README](https://github.com/aws/audit-plugin-for-mysql/blob/mysql-8.0/README.md)
- [plugin/server_audit/CMakeLists.txt](https://github.com/aws/audit-plugin-for-mysql/blob/mysql-8.0/plugin/server_audit/CMakeLists.txt)

**Review boundary:** README and the plugin CMake file checked; implementation source and runtime behavior were not tested.
