# Contributing to Algorithm_Gen

First off, thank you for considering contributing to Algorithm_Gen! 

We are building a robust, high-performance engine for AI-generated and deterministic algorithms. To maintain a perfect project structure, please adhere to the following guidelines.

## Development Workflow
1. Fork the repository and create your branch from `main`.
2. If you've added code that should be tested, add unit tests.
3. Ensure your code passes all CI/CD pipeline checks (we use GitHub Actions for automated testing and code formatting).
4. Update documentation where necessary.

## Project Structure & Polish
* **Clean Code:** Ensure all Python and Rust code is properly documented and formatted (run `make format` before submitting a PR).
* **Badges:** If you are adding new sub-projects or major modules with their own documentation, ensure you include appropriate Shields.io badges at the top of the file to maintain a professional, unified aesthetic.
* **Security:** Never commit `.env` files or hardcode API keys.

## Pull Request Process
Ensure your PR description clearly describes the problem and solution. Include the relevant issue number if applicable. All submissions will be reviewed by the core maintainers before merging into the next release tag (e.g., preparing for v0.1.9).
