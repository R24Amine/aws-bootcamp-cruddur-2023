# Week 1 — App Containerization
In this phase we need to start building our infrastructure for our application, we have a frontend created with nodejs and backend with python-flask

Technical Tasks

we are going to:
Launch the repo within a Gitpod workspace
Configure Gitpod.yml configuration, eg. VSCode Extensions
Clone the frontend and backend repo
Explore the codebases
Ensure we can get the apps running locally
Write a Dockerfile for each app
Ensure we get the apps running via individual container
Create a docker-compose file
Ensure we can orchestrate multiple containers to run side by side
Mount directories so we can make changes while we code

Challenges    

Run the dockerfile CMD as an external script
Push and tag a image to DockerHub (they have a free tier)
Use multi-stage building for a Dockerfile build
Implement a healthcheck in the V3 Docker compose file
Research best practices of Dockerfiles and attempt to implement it in your Dockerfile
Learn how to install Docker on your localmachine and get the same containers running outside of Gitpod / Codespaces
Launch an EC2 instance that has docker installed, and pull a container to demonstrate you can run your own docker processes. 
