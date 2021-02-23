# YouTube Auto-Archive

Simple container, primarily designed to automatically download your YouTube "likes" playlist (Using youtube-dl).

To facilitiate this with two factor authentication, the container uses cookies for authentication.

## To setup

Mount the below mount location and ensure a cookies.txt is present.
Also ensure a targets.txt is present with content to download in the format:

`<url or playlist>, <directory>` on each line

## Mount locations

Container Path | Purpose
---------------|---------
/mount | Output, progress, and cookie directory.

## Environment variables

Environment variable | Purpose | Default
---------|---------|---------
SLEEPMIN | How many minutes to sleep for between scans | 240
