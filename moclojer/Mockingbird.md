
# To Do
## 0.0.1 launching

- npm compile fix -> webpack bundle is being generated, yet, there are some minor issues while importing the code on another react/shadow-cljs+helix project
- target.css -> need to check if any difference has occurred in the now used file and the one from source at compile time, since for now, the css code generated from mockingbird is only copied to user project once (or when this file deleted)
- tailwind.config.js, postcss and these other config for the users. Now, people have to manually gather the config files from our codebase and it seems kind of a frustation to copy things that do not look at first necessary

## quality of life improvements

- another themes for mockingbird -> for now, we only have the default mockingbird theme, which is great, but it would be nicier to have the other 2 themes as intended before.|
- loading? state being updated at all components -> for now, even though some components can have its states changed during runtime, it do not mostly affects UI/UX
- style all the components
- aside fix

## for future
- make the code reusable in all React projects.
- make example page better, as a playground for new components
- tests

# Done

fixes #6 

1. **Release Automation Workflows:**
   - **npm Release Workflow (`.github/workflows/npm.yml`):**
     - Added a GitHub Actions workflow to automate the process of publishing the Node.js package to the npm registry.
     - Triggers on new tags matching the pattern `v*` or manual dispatch.
     - Sets up the Node.js environment with version 20 and runs build commands to compile the library.
     - Utilizes `JS-DevTools/npm-publish@v3.1.1` action for publishing, securely using the `NPM_TOKEN` secret.
   - **Clojars Release Workflow (`.github/workflows/release.yml`):**
     - Added a workflow to automate the release process to Clojars for the Clojure project.
     - Includes steps to set up both Clojure and Node.js environments.
     - Executes build and deployment commands, using `CLOJARS_USERNAME` and `CLOJARS_PASSWORD` secrets for authentication.

2. **Inclusion of Target CSS Code:**
   - Integrated the target CSS code essential for component styling.
   - Updated the build process to ensure CSS assets are properly compiled and included in releases.
   - Added instructions in the `README.md` to copy the `tailwind.config.js` file for Tailwind CSS configuration.

3. **Documentation Enhancements (`README.md` and `docs/`):**
   - **`README.md` Updates:**
     - Expanded the installation section to cover both Clojars and npm distributions.
     - Provided detailed usage examples, including importing components and passing arguments.
     - Added links and notes to improve clarity on prerequisites and setup steps.
   - **Documentation Revisions:**
     - Removed outdated items from `docs/Roadmap.md` to reflect current project focus.
     - Updated `docs/test.md` to streamline local testing instructions, including command adjustments.

4. **Node.js Integration and Build Scripts:**
   - Set up Node.js environment using version 20 in the release workflows.
   - Included build scripts (`npm ci`, `npm run release`) to compile the library and prepare it for release.

5. **Security and Credentials Management:**
   - Utilized GitHub Secrets for managing sensitive information:
     - `NPM_TOKEN` for npm publishing.
     - `CLOJARS_USERNAME` and `CLOJARS_PASSWORD` for Clojars deployment.
   - Ensured that all credentials are securely handled within workflows.

6. **Cleanup and Refinements:**
   - Removed deprecated components and animations from the roadmap to align with the current project direction.
   - Adjusted commands and scripts to improve build consistency and reliability.