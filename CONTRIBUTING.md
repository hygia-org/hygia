# Contributing guide  

## How to contribute?

Contributing to the project is very easy and every little bit counts! Just follow the following steps:

To contribute to this project, follow the next steps:

* *Fork* (just to external contributors)
* Create [*issues*](CONTRIBUTING.md#issues)
* Create [*branchs*](CONTRIBUTING.md#branches-policy)
* Follow the commit policy [*commits*](CONTRIBUTING.md#commit-policy)
* Submit [*Pull Request*](CONTRIBUTING.md#merges-and-pull-requests-policy)


### Commit Policy

The *issues* need title, description, at least one asigned, *labels*, *milestoner* (the *sprint* to conclude)

The Labels used in the project are described in the topic [Labels](https://github.com/PDA-FGA/Playground/labels).

To create a issue follow [task template](/.github/ISSUE_TEMPLATE/task.md) or [user history template](/.github/ISSUE_TEMPLATE/user-story.md)

### Branches Policy

#### *main*

The *main* is the production branch, where the stable version of the project will be. It will be closed for commits and for pushes.
See the merge policy in the topic [Merges para *master*](CONTRIBUTING.md#merges-to-main).


#### Branch Names  

The development branches will be created from the *main* branch with the default naming `x/issue_name`, where `x` represents the issue tracking code.

### Commits Policy

All commits must be mention the issue, for that, just add `#<issue_number>`.

```
 #21 Adding contributing guide
```

**By default, the `#` character defines a comment line in the commit message file. To resolve this issue, use the command:**
```
git config --local core.commentChar '!'
```

### Merges and Pull Requests Policy

#### Pull Requests

Pull requests must be made to the *main* branch following the rules and steps in the topic [*Merges to main*](CONTRIBUTING.md#merges-to-main). In the pull request content there should be a clear description of what was done.

Follow [template Pull Request](/.github/pull_request_template.md).


#### Tag's

| name | description |
| :--: | :---------: |
| documentation | Improve or additions to documentation |
| bug | Something isn't wrong |
| cli | Related to the command-line interface. |
| data preprocessing | Consists of all changing, cleaning and validating the data before running the model | 
| data-validation | Related to validating data. |
| duplicate | This issue or pull request already exists |
| enhancement | New feature or request |
| epic | Refers to a larger, high-level task or feature |
| feture-engineering | Related to creating or improving features used in the model|
| good first issue | Good for newcomers |
| help wanted | Extra attention is needed |
| invalid | This doesn't seem right |
| library | Related to a specific library used in the project |
| model | Related to the machine learning model|
| need-refinement | That issue need further refinement or improvement | 
| not-mapped |That issue have not been mapped to a specific category |
| prototype | Related to creating a prototype or proof-of-concept |
| question | Further information is requested |
| spike | Short-term tasks to investigate specific problems or technologies |
| tech viablity | Related to the feasibility of a technology used in the project |
| user-story | A description of a specific feature from a user's perspective |
| wontfix | This will not be worked on |
| yaml | Related to YAML configuration files |
