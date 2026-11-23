# Company-to-GitHub organization discovery

## Why a company may have multiple GitHub accounts

A single `company -> GitHub handle` mapping is not necessarily a complete company-wide inventory. Large companies can publish through a primary organization, product teams, cloud businesses, research labs, open-source foundations, subsidiaries and acquired businesses.

The catalogue separates:

1. **Company** — the company in the supplied source list.
2. **GitHub account** — one specific organization or user account.
3. **Account inventory** — the public repositories owned by that account.
4. **Company account directory** — the set of accounts discovered and verified for that company.

A company-wide inventory is complete only after relevant official accounts are identified and every account's public repository pagination is complete.

## Verified starting accounts

| Company | Starting GitHub account | Evidence | Scope |
|---|---|---|---|
| Microsoft | [microsoft](https://github.com/microsoft) | [Microsoft Open Source](https://opensource.microsoft.com/) | Primary account only. Microsoft's open-source programme describes more than 100 GitHub organizations; product and research organizations still need discovery. |
| Alphabet / Google | [google](https://github.com/google) | [Google organization reference](https://opensource.google/documentation/reference/github/orgs) | Primary account only. Google documents multiple product-area and project organizations. |
| Apple | [apple](https://github.com/apple) | [Apple Open Source](https://opensource.apple.com/) | This organization only. |
| NVIDIA | [NVIDIA](https://github.com/NVIDIA) | [NVIDIA repository directory](https://github.com/orgs/NVIDIA/repositories) | This organization only; its public directory contains hundreds of projects. |
| Amazon / AWS | [aws](https://github.com/aws) | [AWS GitHub organization](https://github.com/aws) | AWS engineering only, not every Amazon business or subsidiary. |

These are verified starting points, not proof that they are the only official accounts associated with each company.

## Discovery procedure for additional accounts

1. Start from the company's own website, open-source programme, engineering blog or official developer documentation.
2. Follow explicit links to GitHub organizations. A similar account name alone does not establish ownership.
3. Add the exact GitHub login, account type, source URL, review date and scope note to `config/company_accounts.csv`.
4. Use `account_type=auto` until the API confirms whether the account is an organization or user; then record `org` or `user` where useful.
5. Add multiple account rows for one company when official sources link to multiple organizations.
6. Keep product organizations separate under `organizations/<company>/accounts/<account>/`; do not merge unrelated repositories into one synthetic owner.
7. Investigate acquired businesses separately and document whether their account remains independently maintained.
8. Mark a mapping `verified` only when official evidence exists. Candidate mappings remain excluded from scheduled runs by default.

## Completion states

- **Account inventory complete:** the public repository endpoint has reached the final page.
- **README captured:** the default-branch README was fetched and a source SHA recorded.
- **Manifest evidence captured:** selected build/dependency files were retrieved.
- **Technical review complete:** purpose, features, technology claims and limitations were interpreted and checked.
- **Company discovery complete:** relevant official accounts are documented and every account inventory is complete.

These are distinct states. Completing one organization's pages does not prove that every repository has been interpreted or every company organization has been discovered.


## AWS official-directory expansion — 24 November 2026

The official [Open Source at AWS](https://aws.github.io/) site lists 30 GitHub organization links in its **AWS GitHub Organizations** section. Two of the listed organizations (OpenSearch and AWS Amplify) are also linked as standalone projects elsewhere on the same site; the directory therefore resolves to 30 distinct accounts including the primary `aws` account.

The catalogue records the 29 additional logins with the distinct mapping status `official-directory-listed`. The source is a company-controlled open-source directory, which supports a documented AWS open-source relationship; it does not establish legal ownership of every account or authorship of every repository inside it.

See [Amazon/AWS account discovery](../organizations/amazon/ACCOUNT-DISCOVERY.md) for the complete list, sample public repositories used for account-level discovery checks, and attribution rules.
