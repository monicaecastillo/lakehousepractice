# Use the base image from VS Code's devcontainer images
FROM mcr.microsoft.com/vscode/devcontainers/base:ubuntu-20.04

# Install Java 8
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk && \
    apt-get clean && \
    update-alternatives --install /usr/bin/java java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java 1 && \
    update-alternatives --install /usr/bin/javac javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac 1 && \
    update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java && \
    update-alternatives --set javac /usr/lib/jvm/java-8-openjdk-amd64/bin/javac

# Set JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# Verify Java installation
RUN java -version
