FROM ubuntu:14.04

# Update apt
RUN apt-get -qq update

# Install sudo
RUN apt-get -qq -y install sudo
RUN sudo -V

# Install python-pip
RUN apt-get -qq -y install python-pip
RUN pip --version

# Install ansible
RUN apt-get -qq -y install python-yaml python-jinja2 python-httplib2 python-keyczar python-paramiko python-setuptools python-pkg-resources git
RUN pip install ansible
RUN ansible --version

# Configure test user
RUN useradd --home /home/test_usr test_usr
RUN bash -c "echo 'test_usr ALL=(ALL) NOPASSWD:ALL' > /etc/sudoers.d/test_usr"
RUN mkdir -p /home/test_usr/.ansible/tmp
RUN chown root:root /home
RUN chmod 'u=rwx,go=rx' /home
RUN chown -R test_usr:test_usr /home/test_usr
RUN chmod -R 'u=rwx,go=rx' /home/test_usr
