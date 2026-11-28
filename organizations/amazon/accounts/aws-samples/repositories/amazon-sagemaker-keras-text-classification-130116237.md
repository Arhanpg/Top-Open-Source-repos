# aws-samples/amazon-sagemaker-keras-text-classification

- Company: Amazon
- GitHub account: [https://github.com/aws-samples](https://github.com/aws-samples)
- Mapping status: official-directory-listed
- Repository: [aws-samples/amazon-sagemaker-keras-text-classification](https://github.com/aws-samples/amazon-sagemaker-keras-text-classification)
- Default branch: master
- README: [Open upstream README](https://github.com/aws-samples/amazon-sagemaker-keras-text-classification/blob/master/README.md)
- README blob SHA: 215df68ef77ef265e50b90ee09d7518fb2b84866
- README bytes captured: 20357
- README truncated at capture limit: False
- Repository ID: 130116237
- Evidence state: evidence captured; manual review pending
- Manual review: manual technical interpretation pending

## Upstream description

A step-by-step guide that shows how to do text classification by run training/inference for a custom model in Amazon SageMaker

This is repository-owner metadata, not an independently verified technical summary.

## README capture

- Status: captured
- Unavailable reason: Not applicable
- Captured: 2026-11-28T05:00:41+00:00

### Short excerpt (up to 300 words)

> model.add(tf.keras.layers.Flatten()) model.add(tf.keras.layers.Dense(2, activation='relu')) #

### README headings

- AIM427-Take an ML from idea to production using Amazon SageMaker
- Use following url to sign in into an AWS Account. Use the hash provided as the login credential.
- Workshop Lab Guide
- LAB1: Dataset Exploration
- LAB 2: Building the SageMaker TensorFlow Container
- Build an image that can do training and inference in SageMaker
- Set up the program in the image
- Note: Slow down and read the below instruction very carefully. The next command(aws ecr get-login...) is a two step process. First, run the below command(aws ecr get-login...); Second, copy output of command(aws ecr get-login...) and run it as a command.
- LAB 3: Local Testing of Training & Inference Code
- Testing Training Code
- ------Architecture: MLP------------------------------
- model.add(tf.keras.layers.Dense(2, activation='relu')) # Try adding more layers uncommenting this line and changing the units
- Testing Inference Code
- Lab 4: Training & Deployment on Amazon SageMaker
- Lab 5: Distributed Training in Script Mode with Parameter Server Training Framework.
- A. SageMaker's Parameter Server Distributed Training Framework
- B. SageMaker's Script Mode.
- Lab Instructions:
- Citations
- License

## README section evidence excerpts

Short excerpts are selected from matching upstream README sections. They are source evidence, not generated or human-reviewed technical summaries.

### Architecture and design: ------Architecture: MLP------------------------------

> model.add(tf.keras.layers.Flatten()) model.add(tf.keras.layers.Dense(2, activation='relu')) #

## GitHub language statistics

GitHub's Languages API reports detected source-code bytes. It does not identify frameworks or architecture by itself.

| Language | Bytes |
|---|---:|
| Jupyter Notebook | 25,953 |
| Python | 17,533 |
| Shell | 3,174 |

## Build and dependency manifest paths

These paths were found in the default-branch tree. A manifest filename alone is not proof of a framework or runtime.

- No recognised manifests found or captured

- Manifest scan truncated by GitHub: False
- Manifest capture state: none_found

## Lifecycle metadata

- Archived: True
- Fork: False
- Disabled: False
- Licence SPDX: Apache-2.0
- Stars at capture: 108
- Forks at capture: 125
- Last updated: 2026-09-01T21:28:09Z
- Last pushed: 2020-01-24T23:59:30Z
- Topics: Not supplied

## Required manual review

Interpret the README's purpose and capabilities; confirm framework/library claims against manifests and relevant source; inspect architecture, tests, licence, security guidance, platform constraints and maintenance status. Only then change the manual review state to README reviewed.

## Upstream links

- [Repository](https://github.com/aws-samples/amazon-sagemaker-keras-text-classification)
- [README](https://github.com/aws-samples/amazon-sagemaker-keras-text-classification/blob/master/README.md)
- [Issues](https://github.com/aws-samples/amazon-sagemaker-keras-text-classification/issues)
- [Releases](https://github.com/aws-samples/amazon-sagemaker-keras-text-classification/releases)

Capture errors: None

*Generated evidence capture only. This page is not labelled README reviewed until a human has interpreted and checked the upstream material.*
