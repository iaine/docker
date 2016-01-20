Feature: I want to test an OSKAR file built from packages

As a system engineer
I want to test the Docker build file
So that I know that the packages are installed

Scenario: I want to know the Docker file exists
  Given that I have a build directory "../oskar"
  When I create "Dockerfile"
  Then I have the base installation file

Scenario: I want to know if a package is installed
   Given that I have a Docker image called "oskar"
   When I have installed the "oskar" package
   Then I can query the image to see that it is loaded
