# YouTube Auto-Archive

Simple container, primarily designed to automatically download your YouTube "likes" playlist (Using youtube-dl).

To facilitiate this with two factor authentication, the container uses cookies for authentication.

## To setup

Mount the below mount location and ensure a cookies.txt is present.

## Mount locations

Container Path | Purpose
---------------|---------
/output | Output, progress, and cookie directory.

## Environment variables

Environment variable | Purpose | Default
---------|---------|---------
TODOWNLOAD | URL to download. "Likes" playlist by default. | https://www.youtube.com/playlist?list=LL
