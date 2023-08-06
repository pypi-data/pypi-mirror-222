# Synapsectl

A more convenient way than curl'ing into synapse admin API endpoints.

## Usage

First acquire an access token for an account with admin privileges:

```shell-session
$ synapsectl login martijn
or
$ synapsectl set-token [the token]
```

There's a few command to get information and statistics:

```shell-session
$ synapsectl version
Synapse version: 1.89.0

$ synapsectl user-list --order name
@user1:example.org (Example User 1)
@user2:example.org (Example User 2)
@user3:example.org (Example User 3)

$ synapsectl media-statistics
5.2GiB   @user1:example.org (Example User 1)
2.0GiB   @user3:example.org (Example User 3)
55.8MiB  @user2:example.org (Example User 2)
```

## Cleaning up synapse instances

For maintenance these commands exist:

```shell-session
Clean the stored events older than the specified amount of days. With the --all
flag it will also remove non-federated events causing data loss.
$ synapsectl purge-history --all --age 365
Cleaning history of 100 rooms...
 10%|████▏                                     | 10/100 [00:10<01:34,  1.05s/it]

Clean the cached remote media older than the specified amount of days.
$ synapsectl purge-media-cache --age 365
Removing files, this is a slow operation without feedback...
Removed 23518 files
```