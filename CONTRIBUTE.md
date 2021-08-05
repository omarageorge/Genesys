# How To Contribute

The are step by step instructions on how to contribute to the project codebase.

## Steo 1: Fork the repository

By clicking the "Fork" button on the top most right corner, The repository shall be duplicated to your personal account.

## Step 2: Clone the repository

_HTTPS_

```sh
git clone https://github.com/omarageorge/Genesys.git
```

_SSH_

```sh
git clone git@github.com:omarageorge/Genesys.git
```

_Github CLI_

```sh
gh repo clone omarageorge/Genesys
```

## Step 3: Create an branch offline to work on

Here we create a branch called feature where we shall be making changes directly to.

```sh
git checkout -b feature
```

## Step 4: Commit your changes

```sh
git add <filename>
git commit -m "Commit message here"
```

## Step 5: Merge Branch

Merge the feature branch to the main branch after confirming that your code works well.

```sh
git checkout main
git merge feature
```

## Step 6: Push your Code to Github

```sh
git add <filename>
git push -u origin main
```

## Step 7: Create a pull request

- In the repository, click on the "Pull request" tab the is next to the issues tab.

- Click on a big green button "New pull request" on the right.
