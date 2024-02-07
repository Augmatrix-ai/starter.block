FROM ubuntu:latest

# Set the timezone without interaction
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install necessary packages
RUN apt-get update && \
    apt-get install -y \
    python3-dev \
    python3-pip \
    python3-virtualenv \
    curl \
	git \
    screen && \
    DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata 
# Set the timezone without interaction
ENV TZ=UTC

# Copy all files local to image to created Directory 
RUN mkdir /app
COPY ./ /app/.
COPY /deployment/entrypoint.sh .

# Install Python packages which is requirement.txt file
RUN pip3 install -r /app/requirments.txt

# Set permissions and convert line endings
RUN chmod +x entrypoint.sh && \
    sed -i -e 's/\r$//' entrypoint.sh

# Set the entrypoint to run 
ENTRYPOINT ["./entrypoint.sh"]

# Default command to make image alive
CMD ["sleep", "infinity"]
