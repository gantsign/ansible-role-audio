FROM ubuntu:14.04

# Install dependencies
RUN apt-get -qq update
RUN apt-get -qq -y install libffi-dev
RUN apt-get -qq -y install libssl-dev
RUN apt-get -qq -y install python-dev
RUN apt-get -qq -y install python-pip
RUN apt-get -qq -y install python-apt
RUN apt-get -qq -y install sudo
RUN pip install ansible

# Verify dependencies installed
RUN ansible --version
RUN sudo -V

# Configure test user
RUN useradd --home /home/test_usr test_usr
RUN bash -c "echo 'test_usr ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/test_usr"
RUN mkdir -p /home/test_usr/.ansible/tmp
RUN chown root:root /home
RUN chmod 'u=rwx,go=rx' /home
RUN chown -R test_usr:test_usr /home/test_usr
RUN chmod -R 'u=rwx,go=rx' /home/test_usr
