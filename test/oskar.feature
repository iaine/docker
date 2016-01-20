Feature: I want to test an OSKAR file built from packages

As a system engineer
I want to test the Docker build file
So that I know that the packages are installed

Scenario: I want to know the Docker file exists
  Given that I have a build directory "../oskar"
  When I create "Dockerfile"
  Then I have the base installation file
