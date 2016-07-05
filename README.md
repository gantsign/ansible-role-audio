Ansible Role: Audio
===================

Role to enable audio support.

Requirements
------------

* Ubuntu

Role Variables
--------------

The following variable will change the behavior of this role (default values
are shown below):

```yaml
# Users to add to the audio (and video) groups.
audio_users: []
```

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - { role: gantsign.audio, audio_users: [ 'vagrant' ] }
```

License
-------

MIT

Author Information
------------------

John Freeman

GantSign Ltd.
Company No. 06109112 (registered in England)
